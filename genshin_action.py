from action import *
from task_tracker import *
from selenium_utils import *

def init():
    input_utils.set_is_using_adb(False)
    game_name = "genshin"
    set_game_name_for_image(game_name)
    set_game_name_for_task(game_name)
    Target.prefix = game_name
    # import limbus_company_target
    
def login():
    init_if_needed()
    open_url("genshin")
    selenium_receive_daily_rewards()
    
def selenium_receive_daily_rewards():
    driver = get_driver()
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


if __name__ == "__main__":
    login()
    