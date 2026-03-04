from .models import AccountMemo

def generate_changelog(v1_memo: AccountMemo, v2_memo: AccountMemo) -> str:
    """
    Compares two AccountMemos and returns a markdown formatted changelog.
    """
    
    changes = []
    
    v1_dict = v1_memo.model_dump()
    v2_dict = v2_memo.model_dump()
    
    for key, v2_val in v2_dict.items():
        v1_val = v1_dict.get(key)
        
        if v1_val != v2_val:
            changes.append(f"### {key.replace('_', ' ').title()}\n")
            changes.append(f"**Old (v1):**\n```\n{v1_val}\n```\n")
            changes.append(f"**New (v2):**\n```\n{v2_val}\n```\n")

    if not changes:
        return "# Changelog\n\nNo changes detected between v1 and v2."
    
    return "# Changelog (v1 -> v2)\n\n" + "\n".join(changes)
