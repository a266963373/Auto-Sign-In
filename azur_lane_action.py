from action import *
from task_tracker import *
import selenium_utils as se
from time import sleep

def init():
    input_utils.set_is_using_adb(True)
    game_name = "azur lane"
    set_game_name_for_image(game_name)
    set_game_name_for_task(game_name)
    set_game_reset_hour(12)
    Target.prefix = game_name
    import azur_lane_target

def login():
    log_info("开始登录《碧蓝航线》")
    set_sleep_duration(1)
    if not see("homepage"):
        if expect("azur_lane", max_count=2):
            do("azur_lane", find_it=True)
            log_success("成功点击《蔚蓝档案》")
            sleep(10)

    while True:  # after seeing "homepage", 
        # later will appear event announcemtn
        if see("homepage"):
            sleep(1)
            if not see("event_announcement") and see("homepage"):
                break
            
        if see("event_announcement"):
            do("event_announcement_exit")
            
        if see("event_list"):
            do("top_right")
            
        if see("login_update"):
            do("login_update")
            sleep(60)

        else:
            do("bottom_middle")
        slp()
    log_success("成功看见 homepage")
    
def notif():
    log_info("开始 notif")
    set_sleep_duration(1)
    is_what = False
    is_received_oil = False

    while True:
        if see("homepage"):
            do("notif_enter")
            expect("notif")

        if see("notif"):
            if not is_received_oil:
                do("notif_receive_oil")
                do("notif_receive_gold")
                do("notif_receive_book")
                is_received_oil = True
            
            # do in reversed order, because receive resource will block img
            if see("notif_techacademy_complete"):
                do("notif_techacademy_complete")
                slp()
                expect("notif", "notif_enter")
            techacademy()

            if see("notif_tactics_complete"):
                tactics()
                
            if see("notif_delegation_complete"):
                do("notif_delegation_complete")
                expect("notif", "notif_enter")
            delegation()
            
            break
        slp()
    
    log_success("成功 notif")
    expect("homepage", "right")
    
def delegation():
    do("notif_delegation_complete")
    log_info("开始 Delegation")
    expect("delegation")
    
    do("delegation_emergency")
    if not see("delegation_available"):
        do("delegation_daily")

    max_times = 5
    while what_number("delegation_number") != 0:
        match_pos = see("delegation_available", find_it=True)
        if match_pos:
            click(match_pos)
            sleep(0.5)
            do("delegation_advice")
            do("delegation_start")
            if not see("delegation") and see("general_confirm"):
                do("general_confirm")
                sleep(0.5)
            do("left_middle")
            expect("delegation")
        else:
            do("delegation_daily")

        slp()
        max_times -= 1
        if max_times <= 0: break
    expect("notif", "top_left")
    log_success("成功 Delegation")

def tactics():
    do("notif_tactics_complete")
    log_info("开始 Tactics")

    while True:
        if expect("general_confirm"):
            do("general_confirm")
            do("tactics_good_book", threshold=0.8, find_it=True)
            do("tactics_start_class")
            do("general_confirm")
            break
        slp()

    log_success("成功 Tactics")
    expect("notif", "top_left")

def techacademy():
    do("notif_techacademy_complete")
    log_info("开始 Techacademy")
    expect("techacademy")

    if not see("techacademy_list_is_full", threshold=0.9):
    
        is_do_it_last_time = False
        preferred_digit = 2
        i = 0
        do("middle")
        
        while True:
            set_take_new_image(True)
            expect("techacademy_option_entered", "middle")

            do("right")
            sleep(2)
            take_new_image()
            set_take_new_image(False)
            
            print(f"preferred digit: {preferred_digit}")
            
            if see("techacademy_option_stop"):
                set_take_new_image(True)
                do("techacademy_add_to_list")
                expect("general_confirm", max_count=2)
                do("general_confirm")
                
            else:
                if see("techacademy_cubic") and preferred_digit < 5:
                    i += 1
                    continue
                
                num = what_number(f"techacademy_time")

                if see("techacademy_no_requirement") and what_number("techacademy_cost_number") == -1:
                    print("pass due to one.")
                    pass
                elif num > preferred_digit \
                    or not what_number("techacademy_cost_number", is_compare=True) \
                    or what_number("techacademy_cost_number", is_compare=True, return_digit=1) == -1:
                    # selected_index = i
                    i += 1
                    if i > 5:
                        i = 1
                        preferred_digit += 2
                        if preferred_digit > 12:
                            preferred_digit = 0
                        print(f"preferred_digit: {preferred_digit}")
                    continue

                set_take_new_image(True)
                
                do("techacademy_confirm_research")
                slp()
                
                if see("techacademy_option_stop"):
                    do("techacademy_add_to_list")
                    expect("general_confirm", max_count=2)
                    do("general_confirm")
                    
                elif expect("general_confirm", max_count=2):
                    do("general_confirm")
                    slp()
                    do("techacademy_add_to_list")
                    expect("general_confirm", max_count=2)
                    do("general_confirm")

                else:
                    continue
            
            if preferred_digit > 2: preferred_digit = 2 # fix if special case
            preferred_digit = 3 - preferred_digit
            
            # if is_do_it_last_time: break
            # elif see("techacademy_list_is_full"): is_do_it_last_time = True
            if see("techacademy_list_is_full", threshold=0.9): break   # so if there's only max 5,
                                    # no need to enter and add the last project

            slp()
        
    set_take_new_image(True)
    expect("notif", "top_left")
    log_success("成功 Techacademy")

def living_area():
    log_info("开始生活区")
    set_sleep_duration(1)
    
    while True:
        if see("homepage"):
            do("living_area_enter")
            expect("living_area")
            
        if see("living_area"):
            dorm()
            catlodge()
            break
        
        slp()
        
    expect("homepage", "top_left")
    log_success("完成生活区")
    pass

def dorm():
    log_info("开始宿舍")
    do("dorm_enter")
    slp()
    see("dorm") # just to delay, in case see it and see "dorm entered confirm"
    if see("dorm_entered_confirm", threshold=0.8):
        do("dorm_entered_confirm")

    expect("dorm", "left")
    do("dorm_collect")
    do("dorm_food_enter")
    expect("dorm_food")
    stay("dorm_food", 3000)

    log_success("完成宿舍")
    expect("homepage", "top_left")
    do("living_area_enter")
    expect("living_area")

    pass

def catlodge():
    if is_done_today("catlodge"): return
    log_info("开始指挥喵")
    do("catlodge_enter")
    expect("catlodge", "catlodge")
    
    do("catlodge_nest_enter")
    expect("catlodge_nest")
    expect("catlodge", "catlodge_nest_play", in_hurry=True)
    
    do("catlodge_purchase_enter")
    expect("catlodge_purchase")
    do("catlodge_purchase_confirm")
    expect("catlodge", "catlodge_nest_play", in_hurry=True)

    log_success("完成指挥喵")
    mark_done("catlodge")
    expect("homepage", "top_left")
    
def clear_ships():
    dock()
    
def dock():
    log_info("开始船坞")
    do("dock_enter")
    expect("dock")
    if not see("dock_common"):
        do("dock_common")

    do("dock_middle_ship")
    expect("page_entered")
    do("ship_enhance")
    is_quit_next_time = False

    while True:
        slp()
        do("ship_enhance_advice")
        do("ship_enhance_confirm")
        sleep(0.5)
        if see("ship_enhance_result_confirm"):
            do("ship_enhance_result_confirm")
            expect("page_entered", "bottom")
        else:
            # quit if continuous 2 ships cannot be upgraded
            if is_quit_next_time: break
            is_quit_next_time = True
            drag(800, 500, 300, 500, 500)
    
    log_success("完成船坞")
    expect("homepage", "top_left")
    
def build():
    if is_done_today("build"): return
    log_info("开始建造")
    
    while True:
        if see("homepage"):
            do("build_enter")
            expect("page_entered")

        if see("page_entered"):
            do("build_list", find_it=True)
            do("build_list_batch")
            slp()
            expect("page_entered", "bottom", find_it=True)
            do("build_build")
            do("build_start_building")
            # do("build_add_more")
            # do("build_add_more")
            do("general_confirm")
            break
        
        slp()

    log_success("完成建造")
    mark_done("build")
    expect("homepage", "top_left")

def fleet():
    if is_done_today("fleet"): return
    
    log_info("开始大舰队")
    while True:
        if see("homepage"):
            do("fleet_enter")
            expect("page_entered")

        if see("page_entered"):
            do("fleet_logistics")
            while what_number("fleet_logistics_available_number") > 0:
                maximum = 0
                ret_i = 0
                for i in range(3):
                    ret = what_number(f"fleet_logistics_number_{i}", is_compare=True, 
                                return_digit=-1)
                    if ret > maximum: 
                        maximum = ret
                        ret_i = i
                do(f"fleet_logistics_number_{ret_i}", shift=(0, 120))
                do("general_confirm")
                slp()
                expect("page_entered", "bottom", find_it=True)
            break
                
        if see("page_entered"):
            pass
        
        slp()
        expect("homepage", "top_left")

    log_success("完成大舰队")
    mark_done("fleet")
    expect("homepage", "top_left")

def practice():
    if is_done_today("practice"): return
    log_info("开始演习")
    
    while True:
        if see("homepage"):
            do("homepage")
            expect("weigh_anchor")

        if see("weigh_anchor"):
            do("practice_enter")
            expect("practice")
            
        if see("practice"):
            while what_number("practice_number"):
                minimum = 20000
                min_i = 0
                set_take_new_image(False)
                for i in range(4):
                    power_number = what_number(f"practice_power_number_{i}")
                    if power_number < minimum:
                        minimum = power_number
                        min_i = i
                set_take_new_image(True)
                # go challange min_i
                do(f"practice_power_number_{min_i}")
                slp()
                do("practice_start")
                slp()
                do("weigh_anchor_confirm")
                sleep(40)
                set_sleep_duration(10)
                expect("in_battle", max_count=20, to_disappear=True)
                sleep(3)
                set_sleep_duration(1)
                if see("battle_lose", threshold=0.8):
                    battle_lose()
                else:
                    battle_win()
                expect("practice")

            break
        
        slp()
        do("top_left")

    log_success("完成演习")
    mark_done("practice")
    expect("homepage", "top_left")
    
def battle_lose():
    expect("bottom_right_confirm", "bottom_right")
    expect("bottom_right_confirm", "bottom_right", to_disappear=True)
    do("bottom_middle")
    
def battle_win():
    expect("bottom_right_confirm", "bottom_right")
    expect("bottom_right_confirm", "bottom_right", to_disappear=True)

def missions():
    log_info("开始任务")
    flag_exit = False
    
    while True:
        if see("homepage"):
            do("missions_enter")
            expect("page_entered")

        if see("page_entered"):
            missions_collect_page()
            flag_exit = True
        
        if see("missions_weekly_excla_mark"):
            do("missions_weekly_excla_mark")
            missions_collect_page()

        if flag_exit: break

        slp()

    log_success("完成任务")
    expect("homepage", "top_left")
    
def missions_collect_page():
    while see("missions_receive_all"):
        do("missions_receive_all")
        slp()
        expect("page_entered", "missions_receive_all", in_hurry=True)
    while see("missions_receive_one"):
        do("missions_receive_one")
        slp()
        expect("page_entered", "missions_receive_one", in_hurry=True)
        
def play_stage():
    if see("stage_immediate_start"):
        do("stage_immediate_start")
        expect("stage")
    
    if see("stage"):
        while True:
            pass

def auto_everything():
    init()
    login()
    notif()
    fleet()
    living_area()
    build()
    dock()
    practice()
    missions()

if __name__ == "__main__":
    init()
    # auto_everything()
    # techacademy()
    # what_number("stage_ammo_number")
    # build()
    fleet()
    
    pass
