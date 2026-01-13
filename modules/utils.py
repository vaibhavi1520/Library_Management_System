from datetime import datetime

def generate_id(prefix: str, existing_ids):
    """
    Generate incremental IDs like B001, I002 etc.
    """
    nums = []
    for i in existing_ids:
        try:
            nums.append(int(str(i).replace(prefix, "")))
        except:
            pass
    next_num = max(nums) + 1 if nums else 1
    return f"{prefix}{next_num:03d}"

def compute_fine(expected_return_date, actual_return_date, fine_per_day=5):
    """
    Overdue fine logic:
    - if actual_return_date > expected_return_date => fine_per_day * overdue_days
    """
    overdue_days = (actual_return_date - expected_return_date).days
    if overdue_days <= 0:
        return 0
    return overdue_days * fine_per_day
