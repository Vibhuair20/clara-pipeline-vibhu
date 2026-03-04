import os
import subprocess
from pathlib import Path

def run_batch():
    """
    Looks for files in inputs/demo/ and inputs/onboarding/
    Runs the pipeline on all demo files first to create v1.
    Then runs the pipeline on all onboarding files to create v2.
    """
    
    base_dir = Path(__file__).parent.parent
    inputs_dir = base_dir / "inputs"
    demo_dir = inputs_dir / "demo"
    onboarding_dir = inputs_dir / "onboarding"
    
    process_script = base_dir / "scripts" / "process_file.py"
    
    if not demo_dir.exists() or not onboarding_dir.exists():
        print("Please create inputs/demo and inputs/onboarding folders and place your recordings/transcripts in them.")
        return

    # Process all demos (v1)
    print("=== Processing DEMO calls (v1) ===")
    demo_files = list(demo_dir.glob("*"))
    for f in demo_files:
        if f.is_file() and not f.name.startswith("."):
            cmd = ["python", str(process_script), str(f), "--type", "demo"]
            print(f"\nRunning: {' '.join(cmd)}")
            subprocess.run(cmd)
            
    # Process all onboarding updates (v2)
    print("\n=== Processing ONBOARDING calls (v2) ===")
    onboarding_files = list(onboarding_dir.glob("*"))
    for f in onboarding_files:
        if f.is_file() and not f.name.startswith("."):
            cmd = ["python", str(process_script), str(f), "--type", "onboarding"]
            print(f"\nRunning: {' '.join(cmd)}")
            subprocess.run(cmd)

    print("\nBatch processing complete. Check outputs/accounts/ directory.")

if __name__ == "__main__":
    run_batch()
