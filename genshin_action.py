from action import *
from task_tracker import *
import selenium_utils as se

def init():
    input_utils.set_is_using_adb(False)
    game_name = "genshin"
    set_game_name_for_image(game_name)
    set_game_name_for_task(game_name)
    Target.prefix = game_name
    # import limbus_company_target
    
def login():
    se.init_if_needed()
    se.open_url("genshin")
    se.click_red_point()

if __name__ == "__main__":
    login()
    