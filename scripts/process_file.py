import argparse
import os
import json
import sys
from pathlib import Path

# Add the project root to sys.path so 'core' can be found when run from anywhere
base_dir = str(Path(__file__).parent.parent)
if base_dir not in sys.path:
    sys.path.insert(0, base_dir)

from core.extractor import extract_account_memo
from core.agent_builder import build_agent_spec
from core.differ import generate_changelog
from core.models import AccountMemo

def process_pipeline(input_file: str, call_type: str, output_dir: str = "outputs"):
    """
    Orchestrates the Clara Answers data pipeline.
    """
    file_path = Path(input_file)
    if not file_path.exists():
        print(f"Error: {file_path} not found.")
        return

    account_id = "unknown_account"
    previous_memo = None
    
    if call_type.lower() == "onboarding":
        print("Extracting identity to match with previous records...")
        temp_memo = extract_account_memo(str(file_path))
        account_id = temp_memo.account_id
        
        v1_path = Path(output_dir) / "accounts" / account_id / "v1" / "memo.json"
        
        if v1_path.exists():
            print(f"Found existing v1 memo for {account_id}. Using it as base.")
            try:
                with open(v1_path, "r") as f:
                    v1_data = json.load(f)
                    previous_memo = AccountMemo.model_validate(v1_data)
            except Exception as e:
                print(f"Warning: Could not load v1 memo for {account_id}: {e}")
        else:
            print(f"Warning: No v1 memo found for {account_id}. Creating fresh v2 anyway.")

    # Main Extraction
    print("Running main LLM extraction...")
    memo = extract_account_memo(str(file_path), previous_memo=previous_memo)
    account_id = memo.account_id
    
    # Create Agent Spec
    print("Building Agent Spec...")
    version = "v2" if call_type.lower() == "onboarding" else "v1"
    agent_spec = build_agent_spec(memo, version=version)
    
    # Prepare output directories
    ver_dir = Path(output_dir) / "accounts" / account_id / version
    ver_dir.mkdir(parents=True, exist_ok=True)
    
    # Save Outputs
    memo_path = ver_dir / "memo.json"
    spec_path = ver_dir / "agent_spec.json"
    
    with open(memo_path, "w") as f:
        f.write(memo.model_dump_json(indent=2))
        
    with open(spec_path, "w") as f:
        f.write(agent_spec.model_dump_json(indent=2))
    
    print(f"Saved {version} Memo -> {memo_path}")
    print(f"Saved {version} Agent Spec -> {spec_path}")

    # Automate Retell API Integration (Real or Mocked)
    from core.retell_client import RetellClient
    retell = RetellClient()
    spec_dict = json.loads(agent_spec.model_dump_json())
    meta_path = Path(output_dir) / "accounts" / account_id / "retell_meta.json"
    
    if version == "v1":
        print("Pushing preliminary configuration to Retell API...")
        agent_id = retell.create_agent(spec_dict)
        with open(meta_path, "w") as f:
            json.dump({"retell_agent_id": agent_id}, f, indent=2)
    else:
        print("Pushing onboarding updates to existing Retell Agent...")
        if meta_path.exists():
            with open(meta_path, "r") as f:
                meta = json.load(f)
            agent_id = meta.get("retell_agent_id")
            if agent_id:
                retell.update_agent(agent_id, spec_dict)
        else:
            print("  [WARNING] No existing Retell Agent found to update.")

    # Generate Differ Changelog
    if call_type.lower() == "onboarding" and previous_memo:
        changelog = generate_changelog(previous_memo, memo)
        changelog_path = Path(output_dir) / "accounts" / account_id / "changelog.md"
        
        # Append to changelog
        mode = "a" if changelog_path.exists() else "w"
        with open(changelog_path, mode) as f:
            f.write(f"\n\n{changelog}\n\n")
            
        print(f"Saved Changelog -> {changelog_path}")

    print("Success!")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Clara Answers Pipeline CLI")
    parser.add_argument("input_file", help="Path to transcript or audio file.")
    parser.add_argument("--type", choices=["demo", "onboarding"], required=True, help="Type of call (demo or onboarding)")
    parser.add_argument("--out", default="outputs", help="Output directory")
    
    args = parser.parse_args()
    
    process_pipeline(args.input_file, args.type, args.out)
