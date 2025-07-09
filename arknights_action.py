from action import *
from task_tracker import *
import selenium_utils as se
from time import sleep

public_recruit_tags = {"高级资深干员", "资深干员", "新手", "近卫干员", "狙击干员", "重装干员", 
 "医疗干员", "辅助干员", "术师干员", "特种干员", "先锋干员", "近战位", "远程位", 
 "支援机械", "控场", "爆发", "治疗", "支援", "费用回复", 
 "输出", "生存", "群攻", "防护", "减速", "削弱", "快速复活", 
 "位移", "召唤", "元素"}

def init():
    input_utils.set_is_using_adb(True)
    game_name = "arknights" # game name should have space, for easy folder access
    set_game_name_for_image(game_name)
    set_game_name_for_task(game_name)
    set_game_reset_hour(16)
    Target.prefix = game_name
    import arknights_target
    
def close_ads():
    count = 0
    while count < 5:
        if see("mumu_ads"):
            do("mumu_ads")  # exit
        sleep(1)
        count += 1

def login():
    # as the first mumu game to launch, close ads
    # close_ads() #TODO: open it when actually see ads
    log_info("开始登录《明日方舟》")
    set_sleep_duration(3)
    if not see("homepage"):
        if expect("arknights", max_count=2):
            do("arknights", find_it=True)
            log_success("成功点击《明日方舟》")
            sleep(10)

    while not see("homepage"):
        if see("event_announcement"):
            do("close_event_announcement")
        elif see("login_reward"):
            do("close_event_announcement")
        elif see("temporary_event"):
            do("temporary_event")
            expect("got_resource", threshold=0.85)
            do("bottom")
        else:
            do("login")
        slp()
    log_success("成功登录《明日方舟》")
    
def mail():
    if is_done_today("mail"): return
    
    set_sleep_duration(1)
    log_info("开始邮箱")
    expect("homepage")
    if not see("mail_notif", threshold=0.85): return
    
    while True:
        if see("homepage"):
            do("mail_enter")
            expect("mail")

        if see("mail"):
            do("mail")
            expect("got_resource")
            break

        slp()
        
    log_success("完成邮箱")
    mark_done("mail")
    expect("homepage", "top_left")

def infrastructure():
    """Overseeing range: from homepage to reception. Inside reception 
    clue board, it needs to exit and re-see.
    """
    set_sleep_duration(1)
    # expect to be at homepage first
    log_info("开始基建")
    
    # flag_exit = False
    flag_clue_done = False
    # flag_drone_done = False
    
    while True:
        if see("homepage"):    # if in homepage, enter infra
            do("infra_enter")
            expect("infra", max_count=5)    # wait for enter
            slp()

        if see("infra") and what_number("drone_number") >= 10:
            infra_use_drone()
            
        if see("infra_notif", threshold=0.85):
            do("infra_notif", threshold=0.85, find_it=True)
            expect("infra_pending_tasks", "infra_notif")
        elif see("infra"):  # in infra but no tasks!
            flag_clue_done = True
            
        if see("infra_pending_tasks"):
            while True:
                if see("clue_collection"):
                    # reception dealing
                    infra_reception()
                    flag_clue_done = True
                    break
                elif see("infra_notif_training"):
                    do("training_enter")
                    expect("training")
                    do("training_board_enter")
                    expect("infra_pending_tasks", "top_left")
                elif see("infra_notif_trust"):
                    infra_control()

                elif see("infra"):
                    flag_clue_done = True
                    break
                do("solve_infra_pending_tasks")
                
        if not flag_clue_done and see("reception"):
            infra_reception()
            flag_clue_done = True
        
        # if nothing, then I'm trapped!
        if not flag_clue_done:
            do("top_left")
        else:
            expect("homepage", "top_left")
            log_success("基建完成")
            break

def infra_reception():
    set_sleep_duration(1)
    do("reception_enter")
    expect("reception")
    
    while True: # experimental add
        if see("reception"):
            # reception dealing
            do("reception_open_clue")
            while not see("clue_exchange_summary") and not see("clue_board"):
                slp()
            
        if see("clue_exchange_summary"):
            do("top_left")
            expect("clue_board")
            
        sleep(2)    # to wait for message to go away
            
        if see("clue_from_self", threshold=0.85):
            do("clue_from_self")
            expect("clue_from_self_exit")   # wait for it to load
            do("clue_from_self_receive")
            expect("clue_board")

        if see("clue_from_friend"):
            do("clue_from_friend")
            expect("clue_from_friend_receive")
            do("clue_from_friend_receive")
            expect("clue_board", "left")
            
        if True:
            do("clue_give_enter")
            expect("clue_give")
            while not see("clue_give_empty"):
                do("clue_give_first")
                pos = see("clue_give_highlight", threshold=0.85, find_it=True)
                if pos:     # give button position
                    x, y = 1800, pos[1]
                    click(x, y)
                    slp()
                    do("clue_give_next_page")   # so don't give it to the same person
                    continue
                else:
                    do("clue_give_next_page")
            do("top_right")
            expect("clue_board")
            
        if see("clue_board"):
            # fill in the clues
                # click in one clue to change the view
            do("clue_clue_one")
            pos = expect("clue_fill_highlight", max_count=2, threshold=0.85, find_it=True)
            while pos:         # fill clue
                x, y = pos[0] - 50, pos[1] + 50
                click(x, y)
                sleep(0.5)
                do("clue_fill_first")
                slp()
                # next
                pos = expect("clue_fill_highlight", max_count=2, threshold=0.85, find_it=True)
            do("left")
            do("bottom")
            break

        # done clue collection!
        expect("infra", "top_left")

def infra_control():
    do("control_enter")
    expect("control_assistant_enter")
    do("control_assistant_enter")
    expect("control_assistant")
    do("control_assistant_operator")
    expect("operators_list_confirm")
    do("operators_list_second_operator")
    do("operators_list_confirm")
    expect("infra_pending_tasks", "top_left")

def infra_use_drone(is_craft=True):
    if is_craft:
        while not see("craft_station"):
            do("craft_station_enter", threshold=0.90, find_it=True)
            slp()
        do("reception_open_clue")
        expect("craft_order_board")
        
        do("use_drone_craft")
        do("use_drone_most")
        do("use_drone_confirm")
    else:
        while not see("trade_station"):
            do("trade_station_enter", threshold=0.90, find_it=True)
            slp()
        do("reception_open_clue")
        expect("trade_order_board")
        use_drone_count = 0
        while what_number("drone_number") >= 5:
            do("use_drone_help", find_it=True)
            do("use_drone_most")
            do("use_drone_confirm")
            expect("trade_order_board")
            use_drone_count += 1
            if use_drone_count > 3: break
    expect("infra", "top_left")

def visit_friends():
    if is_done_today("visit_friends"): return
    
    set_sleep_duration(1)
    if see("homepage"):
        do("friend_enter")
        expect("friend_list")
    
    if see("friend_list"):
        do("friend_list")
        expect("visit_next_friend", "visit_first_friend")
        
    while True:
        if see("visit_friend_gray") or see("visit_friend_limited"):
            break
        if see("visit_next_friend", threshold=0.9, find_it=True):
            do("visit_next_friend")
            sleep(3)
        slp()
    log_success("成功访问好友")
    mark_done("visit_friends")
    do("top_menu")
    do("homepage_enter")
    expect("homepage")

def spend_credit():
    set_sleep_duration(1)
    if see("homepage"):
        do("homepage")
        expect("credit_shop", "credit_shop")

    if see("receive_credit"):
        do("receive_credit")
        expect("got_resource", "top")
        expect("credit_shop", "top")
    # from 1st to last
    for i in range(10):
        if see(f"purchase_item_out_of_stock_{i}"): continue
        do(f"purchase_item_{i}")
        expect("purchase_item")
        do("purchase_item")
        if see("no_enough_credit"):
            break
        else:
            expect("got_resource")
        expect("credit_shop", "top")
        slp()
    log_success("成功消费信用")
    do("top_menu")
    do("homepage_enter")
    expect("homepage")

def battle_till_the_end():
    battle_times = 1
    while battle_times > 0:
        if see("terminal_battle_chosen"):
            do("choose_battle_times_0")
            do("choose_battle_times_1")
            current_energy = what_number("current_energy")
            energy_per_battle = what_number("energy_per_battle")
            battle_times = current_energy // energy_per_battle
            battle_times = min(battle_times, 6)
            if battle_times > 0:
                do("choose_battle_times_0")
                do(f"choose_battle_times_{battle_times}")
                do("bottom_right")
                expect("operation_start")
                do("operation_start")
                
                sleep(80)
                set_sleep_duration(20)
                expect("operation_finish", max_count=30)
                set_sleep_duration(2)
                # expect("terminal_battle_chosen", "top_left")
                expect("terminal_battle_chosen", "right")
                set_sleep_duration(1)
        slp()
    
def spend_energy_on_last_battle():
    do("terminal_last_battle")
    expect("terminal_battle_chosen")
    battle_till_the_end()
        
def spend_energy_on_earn_orundum():
    do("normal_affairs")
    expect("normal_affairs")
    expect("normal_affairs_switch", "middle_middle")
    do("normal_affairs_switch")
    expect("normal_affairs_specific_battle")
    do("normal_affairs_specific_battle", find_it=True)
    expect("operation_start_enter")

    while what_number("current_energy") > what_number("energy_per_battle"):
        if what_number("normal_affairs_orundum_number") >= 1800:
            mark_done("earn_orundum")
            return
        
        if not see("normal_affairs_prts"):
            return
        
        do("bottom_right")
        slp()
        do("bottom_right")
        sleep(3)
        do("bottom_right")
        expect("operation_start_enter", find_it=True)

def spend_energy_on_earn_resource():
    do("resource")
    expect("resource")
    do("middle_middle")
    expect("resource_exp_battle")
    do("resource_exp_battle")
    expect("operation_start_enter")
    battle_till_the_end()
    
def spend_energy():
    log_info("Start spending energy.")
    is_do_last_battle = False
    
    while True:
        if see("homepage"):
            do("terminal_enter")
            expect("terminal")
            
            if not is_done_this_week("earn_orundum"):
                spend_energy_on_earn_orundum()
                expect("normal_affairs", "top_left")

            if is_do_last_battle:
                spend_energy_on_last_battle()
            else:
                spend_energy_on_earn_resource()
            break

        slp()
            
    log_success("Finished spending energy")
    expect("homepage", "top_left")

def receive_task_reward():
    expect("homepage")
    do("task_reward_enter")
    expect("daily_task")
    do("receive_all_task_reward")
    # expect("got_resource")
    expect("weekly_task", "weekly_task", threshold=0.9)
    do("receive_all_task_reward")
    expect("homepage", "top_left")

def public_recruit():
    set_sleep_duration(1)
    log_info("开始公开招募")
    se.init_if_needed()
    se.open_url("arknights")
    
    if see("homepage"):
        do("public_recruit_enter")
        expect("public_recruit")
        
    if see("public_recruit"):
        while expect("public_recruit_ended", max_count=2):
            do("public_recruit_ended", find_it=True)
            sleep(3)
            expect("public_recruit", "top_right")

        i = 0
        is_in_recruit_page = False
        while i < 4:
            if see(f"public_recruit_doing_{i}"):
                i += 1
                continue
            if not is_in_recruit_page:
                do(f"start_recruit_{i}")
                expect("public_recruit_specification")
            if what_number("public_recruit_ticket_number") <= 0 \
                and not see("refresh_tags"):
                break
            
            occupation_requirements = []
            double_break_flag = False
            
            for j in range(5):
                res = what_hanzi(f"occupation_requirement_{j}", 
                    public_recruit_tags, patch_pair=("高级资深", "高级资深干员"))
                if res == None:
                    is_in_recruit_page = False
                    double_break_flag = True
                    break
                    
                if "资深" not in res:
                    res = res.replace("干员", "")
                occupation_requirements.append(res)
            if double_break_flag: continue

            special_tag = "支援机械"
            somewhat_special_tag = "资深干员"
            very_special_tag = "高级资深干员"

            if special_tag in occupation_requirements:
                index = occupation_requirements.index(special_tag)
                do(f"occupation_requirement_{index}")
                do("public_recruit_time_button_0")
                do("public_recruit_time_button_0")
                do("public_recruit_time_button_0")
                do("public_recruit_time_button_3")
                log_error("获得机械干员选项！你自己来看看吧！")
                se.click_tags(occupation_requirements)
                exit()
                
            elif somewhat_special_tag in occupation_requirements or \
                very_special_tag in occupation_requirements:
                log_error("获得资深干员选项！你自己来看看吧！")
                se.click_tags(occupation_requirements)
                exit()
            
            else:
                se.click_reset_tags()
                se.click_tags(occupation_requirements)
                requirements_to_click = se.get_first_result_tags()
                print(f"职业选择最优组合：{requirements_to_click}")
                # use refresh
                if len(requirements_to_click) == 1 and \
                    requirements_to_click[0] not in ("控场", "位移", "特种", "召唤", "快速复活") and \
                    "资深" not in requirements_to_click[0] and \
                    "机械" not in requirements_to_click[0]:
                    if see("refresh_tags", find_it=True):
                        print("刷新下吧。")
                        do("refresh_tags")
                        do("general_confirm")
                        sleep(3)
                        is_in_recruit_page = True
                        continue
                    
                for tag in requirements_to_click:
                    index = occupation_requirements.index(tag)
                    do(f"occupation_requirement_{index}")
                do("public_recruit_time_button_2")
                
            do("public_recruit_confirm")
            expect("public_recruit", "top_left")
            i += 1
            is_in_recruit_page = False

    log_success("成功公开招募")
    expect("homepage", "top_left")

def auto_everything():
    init()
    login()
    mail()
    infrastructure()
    visit_friends()
    spend_credit()
    public_recruit()
    spend_energy()
    receive_task_reward()

def auto_use_skill():
    set_sleep_duration(5)
    while True:
        if see("skill_ready", threshold=0.85):
            do("skill_ready",threshold=0.85, find_it=True, shift=(0, 130))
            do("skill_use")
        else:
            slp()

if __name__ == "__main__":
    init()
    # auto_everything()
    # spend_energy()
    receive_task_reward()
    # see("weekly_task")

    # infrastructure()
    # auto_use_skill()
