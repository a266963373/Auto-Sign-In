from action import *
from task_tracker import *

def login():
    set_sleep_duration(3)
    do("arknights")
    sleep(10)
    log_success("成功点击《明日方舟》")
    expect("purchase_center", "login")
    log_success("成功期待“采购中心”")

def intrastructure():
    # expect to be at homepage first
    expect("purchase_center", "login")
    