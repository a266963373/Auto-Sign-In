import subprocess
import time
from action import *
from task_tracker import *
import os

def init():
    input_utils.set_is_using_adb(False)
    game_name = "limbus company"
    set_game_name_for_image(game_name)
    set_game_name_for_task(game_name)
    Target.prefix = game_name
    import limbus_company_target
    
def login():
    window = gw.getWindowsWithTitle("LimbusCompany")  # 找到第一个匹配的窗口
    if not window:
        subprocess.Popen(["start", "steam://run/1973530"], shell=True)
        print("🟢 正在启动《边狱公司》...")
        time.sleep(10)  # 等待游戏加载
    maximize_and_move("LimbusCompany")
    set_sleep_duration(5)
    do("login")
    time.sleep(10)
    set_sleep_duration(1)
    expect("homepage", "homepage")
    slp()
    expect("homepage", "homepage")
    
import pygetwindow as gw
import pyautogui
import time

def maximize_and_move(window_title, screen=1):
    try:
        window = gw.getWindowsWithTitle(window_title)[0]  # 找到第一个匹配的窗口
        window.activate()  # 激活到前台
        time.sleep(0.5)  # 稍微等一下

        # 移动到主屏幕左上角 (0,0) 或第1屏
        # 只改位置，不改大小
        window.moveTo(0, 0)
        print(f"🖥️ 窗口已移动到屏幕 {screen}")
        
        # 最大化窗口
        if not window.isMaximized:
            window.maximize()
            print("🖥️ 窗口已最大化")

    except IndexError:
        print("🔴 没找到指定窗口")
    except Exception as e:
        print(f"🔴 操作出错：{e}")
    
def convert_energy():
    expect("energy", "login")
    do("energy")
    do("max_energy_conversion")
    do("confirm")
    
def exit_game():
    os.system('taskkill /F /IM LimbusCompany.exe')
    print("🛑 已强制结束 Limbus Company 游戏进程")
    
def auto_everything():
    init()
    login()
    convert_energy()
    exit_game()

if __name__ == "__main__":
    init()
    # maximize_and_move("LimbusCompany")
    # expect("energy", "login")
    see("homepage")
