from action import *
from task_tracker import *
from selenium_utils import *

def init():
    input_utils.set_is_using_adb(False)
    game_name = "zenless"
    set_game_name_for_image(game_name)
    set_game_name_for_task(game_name)
    Target.prefix = game_name
    # import limbus_company_target
    
def login():
    init_if_needed()
    open_url("zenless")
    selenium_receive_daily_rewards()
    
def selenium_receive_daily_rewards():
    driver = get_driver()
    # 等待奖励列表加载完成
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "components-pc-assets-__prize-list_---list---26M_YG"))
    )
    print("Presence of element located.")
    sleep(5) # 载入约 5 秒后才会刷新至正确签到情况

    # 获取所有奖励项
    items = driver.find_elements(By.CLASS_NAME, "components-pc-assets-__prize-list_---item---F852VZ")

    for item in items:
        # 跳过已领取的
        received = item.find_elements(By.CLASS_NAME, "components-pc-assets-__prize-list_---received---tOZ4Gy")
        if received:
            print("continue")
            continue

        # 找到第一个未领取的，点击它
        item.click()
        print("已点击第一个未签到的奖励。")
        break
    else:
        print("所有奖励都已领取。")

if __name__ == "__main__":
    login()
    