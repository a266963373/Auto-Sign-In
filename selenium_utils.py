import time
import socket
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile


        
# 配置信息
# target_url = "https://prts.wiki/w/公招计算"
url_dict = {"arknights" : "https://prts.wiki/w/公招计算", 
            "genshin" : "https://act.hoyolab.com/ys/event/signin-sea-v3/index.html?act_id=e202102251931481"}
driver = None

# 启动 Firefox
def start_firefox():
    options = Options()
    profile_path = r"C:\Users\a2669\AppData\Roaming\Mozilla\Firefox\Profiles\itka62gz.default-release"
    profile = FirefoxProfile(profile_path)
    options.profile = profile
    
    driver = webdriver.Firefox(options=options)
    return driver

# 判断是否已有目标标签页
def is_url_open(url_keyword):
    for handle in driver.window_handles:
        driver.switch_to.window(handle)
        if url_keyword in driver.current_url:
            return True
    return False

# 打开指定页面（如果还没打开）
def open_target_if_needed(url):
    if not is_url_open(url.split('/')[2]):  # 只检查“prts.wiki”是否在 URL 中
        driver.execute_script(f'''window.open("{url}");''')
    print("🌐 已打开目标页面")

def get_first_result_tags():
    # 找所有表格行
    rows = driver.find_elements(By.CSS_SELECTOR, "table tr.row")
    if not rows:
        return []

    # 找第一行的左边 td 里的 .tag 标签
    first_row = rows[0]
    tag_divs = first_row.find_elements(By.CSS_SELECTOR, "td:first-child .tag")
    return [tag.text.strip() for tag in tag_divs]

# === Init ===
def init_if_needed():
    global driver
    if driver == None:
        print("Opening Firefox...")
        driver = start_firefox()
        print("Firefox opened.")

def open_url(game_name):
    # open_target_if_needed(url_dict[game_name])    # ！会让 driver 在 blank 页面
    driver.get(url_dict[game_name])
    
# ===== click =====
def click_xpath(xpath):
    try:
        tag_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, xpath))
        )
        # tag_element.click()
        driver.execute_script("arguments[0].click();", tag_element)
        print(f"🟢 已点击 xpath：{xpath}")
    except Exception as e:
        print(f"🔴 点击 xpath 失败：{xpath}，错误：{e}")
    
# ===== Arknights ======
def click_tag(tag_text):
    try:
        tag_xpath = f"//div[contains(@class, 'checkbox-container') and text()='{tag_text}']"
        tag_element = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, tag_xpath))
        )
        tag_element.click()

        print(f"🟢 已点击标签：{tag_text}")
    except Exception as e:
        print(f"🔴 点击失败：{tag_text}，错误：{e}")

def click_tags(tag_group):
    for tag in tag_group:
        click_tag(tag)

def click_reset_tags():
    try:
        tag_xpath = f"//button[contains(@class, 'btn') and text()='清除']"
        reset_buttons = driver.find_elements(By.XPATH, tag_xpath)
        for btn in reset_buttons:
            btn.click()
        print(f"🟢 已重置标签")
    except Exception as e:
        print(f"🔴 重置失败，错误：{e}")

# ===== Genshin ======
# def click_red_point():
#     click_xpath(f"//div[contains(@class, 'actived-day')]//span[contains(@class, 'red-point')]")

def click_red_point():
    try:
        # 等 div 出现
        WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'actived-day')]//span[contains(@class, 'red-point')]"))
        )
        # 再找 div，点div
        tag_element = driver.find_element(By.XPATH, "//div[contains(@class, 'actived-day')]")
        driver.execute_script("arguments[0].click();", tag_element)
        print("🟢 成功点击红点外层div")
    except Exception as e:
        print(f"🔴 点击红点外层div失败：{e}")

def driver_quit():
    if driver:
        driver.quit()

def debug():
    html = driver.page_source
    if "red-point" in html:
        print("🟢 发现 red-point 出现在页面里！")
    else:
        print("🔴 页面源码里根本没有 red-point，找不到")

# === 主程序 ===
if __name__ == "__main__":
    init_if_needed()
    # open_url("genshin")
    # time.sleep(10)
    # debug()
    
    open_url("arknights")
    print(driver.current_url)
    click_tag("先锋")
    