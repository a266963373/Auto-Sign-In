import json
import os
from datetime import datetime

# printers
def log_info(message):
    print(f"\033[94m[INFO]\033[0m {message}")

def log_success(message):
    print(f"\033[92m[SUCCESS]\033[0m {message}")

def log_warning(message):
    print(f"\033[93m[WARNING]\033[0m {message}")

def log_error(message):
    print(f"\033[91m[ERROR]\033[0m {message}")


TASK_LOG_PATH = "task_log.json"

def _load_log():
    if os.path.exists(TASK_LOG_PATH):
        with open(TASK_LOG_PATH, "r") as f:
            return json.load(f)
    return {}

def _save_log(data):
    with open(TASK_LOG_PATH, "w") as f:
        json.dump(data, f, indent=2)

def mark_done(task_id: str):
    """标记任务为今天完成"""
    data = _load_log()
    data[task_id] = datetime.today().strftime("%Y-%m-%d")
    _save_log(data)

def is_done_today(task_id: str) -> bool:
    """判断任务今天是否完成"""
    data = _load_log()
    today = datetime.today().strftime("%Y-%m-%d")
    return data.get(task_id) == today

def get_pending_tasks(task_ids):
    """返回今天未完成的任务列表"""
    return [tid for tid in task_ids if not is_done_today(tid)]
