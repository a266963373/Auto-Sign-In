from action import *
from task_tracker import *
import selenium_utils as se
from time import sleep

def init():
    input_utils.set_is_using_adb(True)
    game_name = "blue archive"
    set_game_name_for_image(game_name)
    set_game_name_for_task(game_name)
    set_game_reset_hour(15)
    Target.prefix = game_name
    import blue_archive_target

def login():
    log_info("开始登录《蔚蓝档案》")
    set_sleep_duration(3)
    # if not see("homepage"):
    while "blue" not in a.get_current_focus_window():
        if expect("blue_archive", max_count=2):
            do("blue_archive", find_it=True)
            log_success("成功点击《蔚蓝档案》")
            sleep(10)

    while True:  # after seeing "homepage", 
        # later will appear event announcemtn
        if see("homepage"):
            sleep(5)
            if not see("event_announcement") and see("homepage"):
                break
            
        if see("event_announcement"):
            do("top_right")
            break
        
        if see("login_maintenance"):
            do("bottom_left")
            return -1
        
        # if see("login_update"):
        #     do("general_confirm")
        #     sleep(60)
        #     set_sleep_duration(30)
        
        else:
            do("bottom_left")
        slp()
    log_success("成功看见 homepage")
    set_sleep_duration(1)
    return 0
    
def mail():
    if is_done_today("mail"): return
    log_info("Start mail.")
    set_sleep_duration(1)
    expect("homepage")
    
    while True:
        if see("homepage"):
            do("mail_enter")
            expect("homepage", to_disappear=True)
            do("bottom_right", shift=(-100, 0))
            break
        slp()

    log_success("Finished mail.")
    mark_done("mail")
    expect("homepage", "top_left")
    
def cafe():
    log_info("开始 cafe")
    set_sleep_duration(1)
    is_cafe_entered = False

    while True:
        if see("homepage"):
            do("cafe_enter")
            sleep(3)
            expect("homepage", to_disappear=True)
            expect("cafe", "left_middle")
            while True:
                if see("cafe_visiting_student_confirm"):
                    do("cafe_visiting_student_confirm") # it's actually "exit"
                    break
                elif see("cafe"):
                    break
                slp()
                
        if see("cafe"):
            is_cafe_entered = True
            
        if see("cafe_invitation"):
            do("cafe_invitation")
            expect("cafe_invitation_entered")
            do("cafe_invite_first")
            do("general_confirm")
            do("cafe_invite_exit")
            
        while see("cafe_interactable", threshold=0.8):
            do("cafe_interactable", threshold=0.8, find_it=True, shift=(80, 0))
            sleep(3)
            expect("cafe", "general_confirm")
            
        if not is_done_today("cafe_earnings", 20):
            do("cafe_earnings")
            expect("cafe_earnings")
            do("cafe_earnings_claim")
            expect("cafe_earnings_claim")
            mark_done("cafe_earnings")
            expect("cafe_earnings", "bottom", to_disappear=True)
        
        if is_cafe_entered:
            expect("homepage", "top_left")
            break

        slp()
    
    log_success("成功 cafe")

    #TODO: how to confirm student clickable?

def lesson():
    if is_done_today("lesson", 15): return

    log_info("开始 lesson")
    is_last_lesson_ticket = False
    set_sleep_duration(1)

    while True:
        if see("homepage"):
            do("lesson_enter")
            expect("lesson")

        if see("lesson"):
            do("lesson_enter_first_location")
            expect("lesson_all_locations_enter")

        if see("lesson_all_locations_enter"):   # main loop, start at when in a location
            while True:
                do("lesson_all_locations_enter")
                expect("lesson_all_locations")

                while see("lesson_heart"):
                    do("lesson_heart", threshold=0.85, find_it=True)

                    if what_number("lesson_ticket_number") == 1:
                        is_last_lesson_ticket = True

                    if what_number("lesson_ticket_number") == 0:
                        # exit
                        is_last_lesson_ticket = True
                        expect("lesson_all_locations", "top_left")    
                        break
                        
                    do("lesson_start_lesson")
                    sleep(2.5)
                    expect("lesson_all_locations", "lesson_start_lesson")   # confirm    

                    if is_last_lesson_ticket: break
                do("bottom")
                expect("lesson_all_locations_enter")

                if is_last_lesson_ticket: break

                # to next location
                do("right")
                slp()
                
        if is_last_lesson_ticket: break
        slp()
        
    mark_done("lesson")
    log_success("成功 lesson")
    expect("homepage", "top_left")

def tasks():
    log_info("开始 tasks")
    set_sleep_duration(1)

    while True:
        if see("homepage"):
            do("tasks_enter")
            expect("tasks")

        if see("tasks"):
            while not see("tasks_claim_all_gray"):
                do("bottom_right")
                slp()
            if see("tasks_claim_gem_yellow"):
                do("tasks_claim_gem_yellow")
                expect("tasks_claim_gem_yellow", to_disappear=True)

            break
        
        slp()

    log_success("成功 tasks")
    expect("homepage", "top_left")
    
def social():
    if is_done_today("social", 15): return
    
    log_info("开始 social")
    set_sleep_duration(1)

    while True:
        if see("homepage"):
            do("social_enter")
            expect("social_club")

        if see("social_club"):
            do("social_club")
            slp()
            expect("social_club_send")
            
        if see("social_club_send"):
            expect("social_club_send", "bottom", to_disappear=True)
            message(get_message_for_today("yuuka"), True)
            slp()
            break
            
        do("top_left")
        slp()

    mark_done("social")
    log_success("成功 social")
    expect("homepage", "top_left")

def spend_energy():
    set_sleep_duration(1)
    log_info("开始消费能量")
    while True:
        if see("homepage"):
            do("campaign_enter")
            expect("campaign")

        if see("campaign") and not is_done_today("bounty"):
            bounty()
            mark_done("bounty")
            
        if see("campaign") and not is_done_today("scrimmage"):
            scrimmage()
            mark_done("scrimmage")
            
        if see("campaign"):
            do("mission_enter")
            expect("mission_multi_sweep_enter")
            do("mission_multi_sweep_enter")
            expect("mission_multi_sweep")

            i = 0
            while i <= 2:
                do(f"mission_multi_sweep_list_{i}")
                if see("mission_multi_sweep_highlight"):
                    do("mission_multi_sweep_max")
                    do("mission_multi_sweep_highlight")
                    slp()
                    do("mission_multi_sweep_confirm")
                    expect("mission_multi_sweep", "left_middle")
                
                else:
                    i += 1
            break
        slp()
        
    expect("homepage", "top_left")
    log_success("成功消费能量")

def bounty():
    do("bounty_enter")
    expect("bounty")
    if what_number("bounty_ticket") == 0: return
    do("bounty_enter_first")
    expect("bounty_overpass")
    drag(1350, 250, 1350, 950, 200)
    slp()
    do("stage_enter_third")
    sleep(0.5)
    do("stage_sweep_max")
    do("stage_sweep_start")
    do("general_confirm")
    slp()
    set_sleep_duration(0.5)
    expect("campaign", "top_left", max_count=30)
    set_sleep_duration(1)

def scrimmage():
    do("scrimmage_enter")
    expect("scrimmage")
    if what_number("bounty_ticket") == 0: return
    do("bounty_enter_first")
    expect("scrimmage_trinity")
    do("stage_enter_first")
    sleep(0.5)
    do("stage_sweep_max")
    do("stage_sweep_start")
    do("general_confirm")
    slp()
    set_sleep_duration(0.5)
    expect("campaign", "top_left", max_count=30)
    set_sleep_duration(1)

def auto_everything():
    init()
    if login() == -1:
        return -1
    
    mail()
    cafe()
    lesson()
    tasks()
    social()
    spend_energy()
    tasks()

if __name__ == "__main__":
    init()

    auto_everything()

    # tasks()
    # cafe()
    # social()
    
    pass
