# ===== servers as the intermediate between actions and adb/pyautogui utils =====
import adb_utils as a
import pyautogui as p
import numpy as np
import cv2
import io

isUsingAdb = True   # False = use pyautogui
last_clicked_pos = (0, 0)

def click(x, y=None):
    global last_clicked_pos
    if y is None:
        x, y = x
    
    if isUsingAdb:
        a.click(x, y)
    else:
        p.click(x, y)

    last_clicked_pos = x, y
    
def click_last_clicked_pos():
    click(last_clicked_pos)
    
def repeat_click(x, y, repeat=2):
    for i in range(repeat):
        click(x, y)
        sleep(0.5)
    
def drag(x1, y1, x2, y2, duration=1000):
    if isUsingAdb:
        a.drag(x1, y1, x2, y2, duration)
    else:
        print("Non-ADB drag unimplemented!")
        
def hold(x, y, duration=1000):
    if isUsingAdb:
        a.hold(x, y, duration)
    else:
        print("Non-ADB hold unimplemented!")
        
def screencap():
    """
    Returns:
        cv2 type image.
    """
    if isUsingAdb:
        data = np.frombuffer(io.BytesIO(a.screencap()).getvalue(), dtype=np.uint8)
        return cv2.imdecode(data, cv2.IMREAD_COLOR)
    else:
        img = p.screenshot()
        return cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)
    
def message(text, and_enter=False):
    if isUsingAdb:
        a.message(text, and_enter=and_enter)
    else:
        print("Non-ADB message unimplemented!")
        
def close_foreground_app():
    if isUsingAdb:
        a.close_foreground_app()
    else:
        print("Non-ADB close_forground_app() unimplemented!")
    
# === settings ===
def set_is_using_adb(b):
    global isUsingAdb
    isUsingAdb = b
    if isUsingAdb:
        a.init_if_need()
