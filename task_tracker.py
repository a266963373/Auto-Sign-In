import json
import os
from datetime import datetime, timedelta

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
game_name = ""  # for determine which folder to get image from
game_reset_hour = 16

def set_game_name_for_task(n):
    global game_name
    game_name = n

def set_game_reset_hour(n):
    global game_reset_hour
    game_reset_hour = n
    
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
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    key = game_name + ":" + task_id
    data[key] = now
    _save_log(data)
    
def is_done_recently(task_id: str, hours: int = 8) -> bool:
    data = _load_log()
    key = game_name + ":" + task_id
    ts_str = data.get(key)
    if not ts_str:
        return False

    try:
        done_time = datetime.strptime(ts_str, "%Y-%m-%d %H:%M:%S")
    except ValueError:
        return False  # 旧数据不兼容，或格式错误
    
    return datetime.now() - done_time <= timedelta(hours=hours)

def is_done_today(task_id: str, reset_hour: int = -1) -> bool:
    if reset_hour == -1: reset_hour = game_reset_hour
    
    data = _load_log()
    key = game_name + ":" + task_id
    ts_str = data.get(key)
    if not ts_str:
        return False

    try:
        done_time = datetime.strptime(ts_str, "%Y-%m-%d %H:%M:%S")
    except ValueError:
        return False

    now = datetime.now()

    # 今日重置点
    if now.hour >= game_reset_hour:
        today_reset = now.replace(hour=game_reset_hour, minute=0, second=0, microsecond=0)
    else:
        today_reset = (now - timedelta(days=1)).replace(hour=game_reset_hour, minute=0, second=0, microsecond=0)

    return done_time >= today_reset

from datetime import datetime, timedelta

def is_done_this_week(task_id: str, reset_hour: int = -1) -> bool:
    if reset_hour == -1:
        reset_hour = game_reset_hour  # 例如 4 表示凌晨 4 点重置

    data = _load_log()
    key = game_name + ":" + task_id
    ts_str = data.get(key)
    if not ts_str:
        return False

    try:
        done_time = datetime.strptime(ts_str, "%Y-%m-%d %H:%M:%S")
    except ValueError:
        return False

    now = datetime.now()

    # 本周一的重置点（如果当前时间还没到本周一的 reset_hour，则往前推一周）
    weekday = now.weekday()  # 周一是 0，周日是 6
    monday_reset = now - timedelta(days=weekday)
    monday_reset = monday_reset.replace(hour=reset_hour, minute=0, second=0, microsecond=0)

    if now < monday_reset:
        # 说明当前仍属于上周的周期，需要再往前推一周
        monday_reset -= timedelta(days=7)

    return done_time >= monday_reset

def get_pending_tasks(task_ids, within_hours=8):
    """返回最近未完成的任务列表"""
    return [tid for tid in task_ids if not is_done_recently(tid, hours=within_hours)]

def get_message_for_today(file_name):
    today = datetime.now().day  # 获取当前是几号（1~31）
    
    with open(f"texts/{file_name}.txt", 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    # 去除每行末尾换行符，并保证不超过31天
    lines = [line.strip() for line in lines]
    
    print(len(lines))
    
    if 1 <= today <= len(lines):
        return lines[today - 1]  # 索引从0开始
    else:
        return f"😿 今天是 {today} 号，但文本只有 {len(lines)} 行"

if __name__ == "__main__":
    print(get_message_for_today("yuuka"))
    