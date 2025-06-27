import arknights_action
import blue_archive_action
import azur_lane_action
import genshin_action
import zenless_action
import limbus_company_action
import input_utils
import action
from image_utils import set_game_name_for_image
from task_tracker import *
from selenium_utils import driver_quit
from time import sleep

def auto_arknights():
    set_game_name_for_task("")
    if not (is_done_today("arknights", 8) and is_done_recently("arknights", 8)):
        arknights_action.auto_everything()
        set_game_name_for_task("")
        mark_done("arknights")
        return True
    return False

def auto_blue_archive():
    set_game_name_for_task("")
    if not (is_done_today("blue archive", 8) and is_done_recently("blue archive", 8)):
        blue_archive_action.auto_everything()
        set_game_name_for_task("")
        mark_done("blue archive")
        return True
    return False
        
def auto_azur_lane():
    set_game_name_for_task("")
    if not (is_done_today("azur lane", 8) and is_done_recently("azur lane", 8)):
        azur_lane_action.auto_everything()
        set_game_name_for_task("")
        mark_done("azur lane")
        
def auto_genshin():
    set_game_name_for_task("")
    if not is_done_today("genshin", 12):
        genshin_action.init()
        genshin_action.login()
        set_game_name_for_task("")
        mark_done("genshin")
        
def auto_zenless():
    set_game_name_for_task("")
    if not is_done_today("zenless", 12):
        zenless_action.init()
        zenless_action.login()
        set_game_name_for_task("")
        mark_done("zenless")
        
def auto_limbus_company():
    set_game_name_for_task("")
    if not is_done_recently("limbus company", 6):
        limbus_company_action.auto_everything()
        set_game_name_for_task("")
        mark_done("limbus company")

def auto_everything():
    auto_genshin()
    sleep(10)
    auto_zenless()
    auto_limbus_company()

    if auto_arknights():
        input_utils.close_foreground_app()
        action.reset_init()
        sleep(1)
        
    if auto_blue_archive():
        input_utils.close_foreground_app()
        action.reset_init()
        sleep(1)
        
    auto_azur_lane()
    
    driver_quit()


if __name__ == "__main__":
    # mark_done("limbus company")
    # mark_done("arknights")
    # mark_done("blue archive")
    print("I am executed!")
    auto_everything()
    # genshin_action.init()
    # genshin_action.login()
    # sleep(10)
    # zenless_action.init()
    # zenless_action.login()
