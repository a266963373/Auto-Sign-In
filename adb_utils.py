import subprocess
from ppadb.client import Client as AdbClient
from time import sleep

# 连接到 ADB 服务器
print("Connecting...")
subprocess.run(["adb", "start-server"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
subprocess.run(["adb", "connect", "127.0.0.1:16384"], stdout=subprocess.DEVNULL)
client = AdbClient(port=5037)
print("Connected.")

# 获取设备列表
devices = client.devices()
# print("Device[0]:", devices[0])

# 如果有设备连接，列出设备
if devices:
    device = devices[0]
    # for i in devices:
    #     print(device)
else:
    print("No devices connected")

def click(x, y=None):
    if y is None:
        x, y = x
    device.shell(f"input tap {x} {y}")
    
def repeat_click(x, y, repeat=2):
    for i in range(repeat):
        click(x, y)
        sleep(0.5)
    
def drag(x1, y1, x2, y2, duration=1000):
    device.shell(f"input swipe {x1} {y1} {x2} {y2} {duration}")
    
def screencap():
    return device.screencap()
    
if __name__ == "__main__":
    # click(1107, 883)
    click(100, 100)
    print("Clicked 100, 100 in main")
