import subprocess
from ppadb.client import Client as AdbClient
from time import sleep
import psutil
import re

device = None

def init_if_need():
    global device
    # 打开 MuMu
    emulator_path = r"C:\Program Files\Netease\MuMu Player 12\shell\MuMuPlayer.exe"
    is_just_opened = False

    for proc in psutil.process_iter(['name']):
        if proc.info['name'] == "MuMuPlayer.exe":
            print("Emulator is open.")
            break
    else:
        print("Emulator is not open. Opening.")    
        subprocess.Popen(emulator_path)
        is_just_opened = True

    # 连接到 ADB 服务器
    print("ADB connecting...")
    subprocess.run(["adb", "start-server"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    # in case of "device offline"
    result = subprocess.run(["adb", "devices"], capture_output=True, text=True)
    while "offline" in result.stdout:
        result = subprocess.run(["adb", "kill-server"], capture_output=True, text=True)
        sleep(3)

    result = subprocess.run(["adb", "connect", "127.0.0.1:16384"], capture_output=True, text=True)
    while not result.stdout or "connected" not in result.stdout:
        sleep(5)
        result = subprocess.run(["adb", "connect", "127.0.0.1:16384"], capture_output=True, text=True)

    client = AdbClient(port=5037)
    print("ADB connected.")
    if is_just_opened:      # give some time for device to setup
        sleep(3)

    # 获取设备列表
    devices = client.devices()
    # print("Device[0]:", devices[0])

    # 如果有设备连接，列出设备
    if devices:
        device = devices[0]
        # print(f"Device connected: {device}")
        # for i in devices:
        #     print(device)
    else:
        print("No devices connected")

def click(x, y):
    device.shell(f"input tap {x} {y}")
    
def drag(x1, y1, x2, y2, duration=1000):
    device.shell(f"input swipe {x1} {y1} {x2} {y2} {duration}")
    
def hold(x, y, duration=1000):
    drag(x, y, x, y, duration)
    
def screencap():
    return device.screencap()
    
def zoom_in():
    device.shell(f"input swipe 100 500 400 500 1000 &\
                   input swipe 800 500 500 500 1000")
    
def zoom_out():
    device.shell(f"input swipe 400 500 100 500 1000 &\
                   input swipe 500 500 800 500 1000")

def message(text, and_enter=False):
    device.shell(f"input text '{text}'")
    sleep(len(text) * 0.02)
    if and_enter:
        device.shell(f"input keyevent 66")
        
def get_current_focus_window():
    raw = device.shell("dumpsys activity activities")
    for line in raw.splitlines():
        if "mCurrentFocus=" in line and "null" not in line:
            match = re.search(r' ([a-zA-Z0-9_.]+)/', line)
            if match:
                return match.group(1)
    return None

def close_foreground_app():
    package = get_current_focus_window()
    if package:
        if "mumu" not in package:
            print(f"🚫 正在关闭前台应用：{package}")
            device.shell(f"am force-stop {package}")
        else:
            print("✔ 已经在主页面，无须关闭当前前台应用")
    else:
        print("⚠️ 未找到当前前台窗口（可能是无焦点、切换中或模拟器 bug）")

def command(cmd):
    return device.shell(cmd)

if __name__ == "__main__":
    init_if_need()
    # close_foreground_app()

"""
In case of "daemon cannot start"
Just open the Command Prompt or PowerShell as Administrator, and type the
following commands there:

net stop winnat
net start winnat
"""
