from target import *

Target(
    id="arknights",
    name="arknights_icon",
)

Target(
    id="homepage",
    name="purchase_center_button",
    search_region=(1119, 632, 1393, 822),
)

Target(
    id="login",
    click_pos=(962, 765),
)

Target(
    id="infra_enter",
    click_pos=(1534, 940),
)

Target(
    id="infra",
    name="station_overview",
    search_region=(26, 121, 356, 237),
)

Target(
    id="infra_notif",
    name="infra_notif",
    search_region=(1759, 103, 1860, 278),
)

Target(
    id="solve_infra_pending_tasks",
    click_pos=(342, 1030),
)

Target(
    id="infra_pending_tasks",
    name="infra_pending_tasks",
    search_region=(0, 1004, 220, 1080),
)

Target(
    id="clue_collection",
    search_region=(247, 1002, 444, 1082),
)

Target(
    id="reception_enter",
    click_pos=(1742, 356),
)

Target(
    id="reception",
    name="reception",
    search_region=(571, 20, 843, 96),
)

Target(
    id="reception_open_clue",
    click_pos=(405, 995),
)

Target(
    id="clue_board",
    name="clue_board_clue_button",
    search_region=(1744, 852, 1860, 1003)
)

Target(
    id="clue_from_self",
    name="clue_new_notif",
    search_region=(1814, 199, 1886, 242),
    click_pos=(1798, 276),
)

Target(
    id="clue_from_self_exit",
    name="clue_from_self_exit",
    search_region=(1435, 97, 1530, 201)
)

Target(
    id="clue_from_self_receive",
    click_pos=(1209, 865),
)

Target(
    id="clue_from_friend",
    name="clue_new_notif",
    search_region=(1814, 358, 1886, 405),
    click_pos=(1798, 430),
)

Target(
    id="clue_from_friend_receive",
    name="clue_from_friend_receive",
    search_region=(1453, 985, 1720, 1063)
)

Target(
    id="clue_give_enter",
    click_pos=(1798, 584),
)

Target(
    id="clue_give",
    name="clue_give_top_left",
    search_region=(24, 22, 262, 89)
)

Target(
    id="clue_give_empty",
    name="clue_give_empty",
    search_region=(147, 547, 498, 608)
)

Target(
    id="clue_give_first",
    click_pos=(300, 367)
)

Target(
    id="clue_give_highlight",
    name="clue_give_highlight",
    search_region=(1272, 129, 1730, 886)
)

Target(
    id="clue_give_next_page",
    click_pos=(1814, 1019)
)

Target(
    id="top_right",
    click_pos=(1865, 60)
)

Target(
    id="top_left",
    click_pos=(70, 60)
)

Target(
    id="clue_clue_one",
    click_pos=(581, 343)
)

Target(
    id="clue_fill_highlight",
    name="clue_fill_highlight",
    search_region=(190, 170, 1184, 697)
)

Target(
    id="clue_fill_first",
    click_pos=(1581, 362)
)

Target(
    id="clue_exchange_summary",
    name="clue_exchange_summary",
    search_region=(30, 125, 340, 200)
)

Target(
    id="bottom",
    click_pos=(1000, 1000)
)

Target(
    id="left",
    click_pos=(60, 520)
)

Target(
    id="drone_number",
    search_region=(1158, 35, 1226, 72)
)

Target(
    id="trade_station_enter",
    name="trade_station_enter",
    search_region=(0, 555, 1032, 1000)
)

Target(
    id="trade_station",
    name="trade_station",
    search_region=(570, 24, 761, 90)
)

Target(
    id="trade_order_board",
    name="trade_order_board",
    search_region=(1438, 889, 1719, 1019)
)

Target(
    id="craft_station_enter",
    name="craft_station_enter",
    search_region=(480, 377, 1032, 540)
)

Target(
    id="craft_station",
    name="craft_station",
    search_region=(570, 20, 761, 90)
)

Target(
    id="craft_order_board",
    name="craft_order_board",
    search_region=(1532, 873, 1845, 1051)
)

Target(
    id="use_drone_craft",
    click_pos=(1833, 811)
)

Target(
    id="use_drone_help",
    name="use_drone_help",
    search_region=(402, 674, 1716, 795)
)

Target(
    id="use_drone_most",
    click_pos=(1439, 500)
)

Target(
    id="use_drone_confirm",
    click_pos=(1439, 862)
)

Target(
    id="friend_enter",
    click_pos=(540, 864)
)

Target(
    id="friend_list",
    name="friend_list",
    search_region=(30, 277, 324, 392)
)

Target(
    id="visit_first_friend",
    click_pos=(1629, 256)
)

Target(
    id="visit_next_friend",
    name="visit_next_friend",
    search_region=(1638, 865, 1917, 1022)
)

Target(
    id="visit_friend_limited",
    name="visit_friend_limited",
    search_region=(1719, 95, 1917, 238)
)

Target(
    id="visit_friend_gray",
    name="visit_friend_gray",
    search_region=(1638, 865, 1917, 1022)
)

Target(
    id="event_announcement",
    name="event_announcement",
    search_region=(516, 135, 833, 225)
)

Target(
    id="close_event_announcement",
    click_pos=(1808, 110)
)

Target(
    id="top_menu",
    click_pos=(402, 51)
)

Target(
    id="homepage_enter",
    click_pos=(140, 411)
)

Target(
    id="credit_shop",
    search_region=(1648, 120, 1880, 195)
)

Target(
    id="receive_credit",
    search_region=(1422, 30, 1620, 90)
)

Target(
    id="top",
    click_pos=(960, 50)
)

for i in range(10):
    Target(
        id=f"purchase_item_{i}",
        click_pos=(200 + 375 * (i%5), 417 + 350 * (i//5))
    )

Target(
    id="purchase_item",
    search_region=(1194, 823, 1557, 914)
)

for i in range(10):
    Target(
        id=f"purchase_item_out_of_stock_{i}",
        name="purchase_item_out_of_stock",
        search_region=(
            20 + 380 * (i%5), 380 + 380 * (i//5), 
            107 + 380 * (i%5), 500 + 380 * (i//5)
        )
    )
    
Target(
    id="no_enough_credit",
    search_region=(1414, 95, 1887, 256)
)

Target(
    id="terminal_enter",
    click_pos=(1430, 240)
)

Target(
    id="terminal",
    search_region=(65, 945, 251, 1061)
)

Target(
    id="terminal_last_battle",
    click_pos=(1675, 880)
)

Target(
    id="terminal_battle_chosen",
    search_region=(1268, 13, 1352, 93)
)

Target(
    id="current_energy",
    search_region=(1698, 28, 1789, 88)
)

Target(
    id="energy_per_battle",
    search_region=(1789, 1016, 1830, 1051)
)

for i in range(7):
    Target(
        id=f"choose_battle_times_{i}",  # 0 is open the menu
        click_pos=(1504, 891 - 93 * i)
    )

Target(
    id="bottom_right",
    click_pos=(1844, 1000)
)

Target(
    id="right",
    click_pos=(1844, 540)
)

Target(
    id="operation_start",
    search_region=(1554, 549, 1757, 967)
)

Target(
    id="got_resource",
    search_region=(856, 32, 1056, 268)
)

# Target(
#     id="still_in_battle",
#     search_region=(495, 929, 735, 1029)
# )

Target(
    id="operation_finish",
    search_region=(0, 80, 94, 530)
)

Target(
    id="task_reward_enter",
    click_pos=(1170, 908)
)

Target(
    id="daily_task",
    search_region=(670, 16, 974, 112)
)

Target(
    id="receive_all_task_reward",
    click_pos=(1683, 196)
)

Target(
    id="weekly_task",
    search_region=(1084, 16, 1379, 112)
)

Target(
    id="login_reward",
    search_region=(1551, 508, 1671, 634)
)

for i in range(5):
    Target(
        id=f"occupation_requirement_{i}",
        search_region=(
            564 + 10 + 250 * (i%3), 540 + 10 + 109 * (i//3), 
            776 - 10 + 250 * (i%3), 610 - 10 + 109 * (i//3))
    )

Target(
    id="public_recruit_enter",
    click_pos=(1506, 769)
)

Target(
    id="public_recruit",
    search_region=(185, 150, 370, 256)
)

Target(
    id="public_recruit_ticket_number",
    search_region=(592, 992, 615, 1027)
)

for i in range(4):
    Target(
        id=f"start_recruit_{i}",
        click_pos=(486 + 1000 * (i%2), 435 + 400 * (i//2))
    )

Target(
    id="public_recruit_specification",
    search_region=(340, 295, 588, 778)
)

for i in range(4):  # 0 is add 1 hour, 1 is add 10 minutes
    Target(
        id=f"public_recruit_time_button_{i}",
        click_pos=(677 + 250 * (i%2), 225 + 220 * (i//2))
    )

Target(
    id="public_recruit_confirm",
    click_pos=(1469, 874)
)

Target(
    id="public_recruit_ended",
    search_region=(337, 505, 1659, 1058)
)

for i in range(4):  # 0 is add 1 hour, 1 is add 10 minutes
    Target(
        id=f"public_recruit_doing_{i}",
        name="public_recruit_doing", 
        search_region=(
            343 + 946 * (i%2), 369 + 415 * (i//2), 
            489 + 946 * (i%2), 519 + 415 * (i//2))
    )

Target(
    id="refresh_tags",
    search_region=(1399, 552, 1524, 680)
)

Target(
    id="general_confirm",
    click_pos=(1266, 740)
)

Target(
    id="temporary_event",
    search_region=(352, 230, 534, 562), 
    click_pos=(1495, 771)
)

Target(
    id="infra_notif_training",
    search_region=(227, 980, 444, 1072),
)

Target(
    id="training_enter",
    click_pos=(1646, 708),
)

Target(
    id="training",
    search_region=(568, 23, 649, 95)
)

Target(
    id="training_enter",
    click_pos=(1646, 708),
)

Target(
    id="training_board_enter",
    click_pos=(424, 918),
)

Target(
    id="skill_ready",
)

Target(
    id="skill_use",
    click_pos=(1270, 605)
)

Target(
    id="mail_notif",
    name="clue_fill_highlight",
    search_region=(305, 5, 365, 60)
)

Target(
    id="mail_enter",
    click_pos=(295, 57)
)

Target(
    id="mail",
    search_region=(1535, 946, 1895, 1058)
)

Target(
    id="normal_affairs",
    search_region=(1029, 924, 1227, 1074)
)

Target(
    id="middle_middle",
    click_pos=(960, 510)
)

Target(
    id="normal_affairs_switch",
    search_region=(1621, 982, 1761, 1055)
)

Target(
    id="normal_affairs_specific_battle",
    search_region=(1066, 37, 1698, 1067)
)

Target(
    id="normal_affairs_orundum_number",
    search_region=(155, 957, 324, 1018)
)

Target(
    id="normal_affairs_prts",
    search_region=(1469, 848, 1576, 926)
)

Target(
    id="operation_start_enter",
    search_region=(1671, 926, 1877, 1015)
)

Target(
    id="resource",
    search_region=(709, 945, 879, 1057)
)

Target(
    id="resource_exp_battle",
    search_region=(1433, 200, 1702, 311)
)
