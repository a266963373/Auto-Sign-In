from target import *

Target(
    id="blue_archive",
    name="blue_archive_icon"
)

Target(
    id="bottom_left",
    click_pos=(69, 1016)
)

Target(
    id="bottom_right",
    click_pos=(1884, 1016)
)

Target(
    id="event_announcement",
    search_region=(44, 111, 122, 459)
)

Target(
    id="top_right",
    click_pos=(1857, 71)
)

Target(
    id="homepage",
    search_region=(1712, 786, 1877, 862)
)

Target(
    id="cafe_enter",
    click_pos=(139, 986)
)

Target(
    id="cafe",
    search_region=(50, 850, 900, 1100)
)

Target(
    id="cafe_visiting_student_confirm",
    search_region=(841, 642, 1095, 727),
    click_pos=(1387, 280)
)

Target(
    id="cafe_invitation",
    search_region=(1250, 900, 1400, 1050)
)

Target(
    id="cafe_invitation_entered",
    search_region=(610, 98, 899, 183)
)

Target(
    id="cafe_interactable",
)

Target(
    id="cafe_invite_first",
    click_pos=(1179, 335)
)

Target(
    id="general_confirm",
    click_pos=(1148, 751)
)

Target(
    id="cafe_invite_exit",
    click_pos=(1277, 175)
)

Target(
    id="cafe_earnings",
    search_region=(783, 162, 1150, 284),
    click_pos=(1725, 973)
)

Target(
    id="cafe_earnings_claim",
    search_region=(779, 712, 1149, 866),
    click_pos=(961, 792)
)

Target(
    id="bottom",
    click_pos=(1000, 1000)
)

Target(
    id="top_left",
    click_pos=(50, 50)
)

Target(
    id="lesson_enter",
    click_pos=(315, 986)
)

Target(
    id="lesson",
    search_region=(1695, 116, 1860, 363)
)

Target(
    id="lesson_enter_first_location",
    click_pos=(1373, 297)
)

Target(
    id="lesson_all_locations_enter",
    search_region=(1602, 950, 1887, 1047)
)

Target(
    id="lesson_heart",
    search_region=(188, 415, 1739, 921)
)

Target(
    id="lesson_all_locations",
    search_region=(790, 137, 1126, 234)
)

Target(
    id="lesson_start_lesson",
    click_pos=(962, 822)
)

Target(
    id="lesson_ticket_number",
    search_region=(1085, 738, 1106, 770)
)

Target(
    id="right",
    click_pos=(1858, 540)
)

Target(
    id="tasks_enter",
    click_pos=(100, 350)
)

Target(
    id="tasks",
    search_region=(719, 79, 927, 219)
)

Target(
    id="tasks_claim_all_gray",
    search_region=(1615, 965, 1842, 1046)
)

Target(
    id="tasks_claim_gem_yellow",
    search_region=(1393, 959, 1532, 1042)
)

Target(
    id="social_enter",
    click_pos=(840, 980)
)

Target(
    id="social_club",
    search_region=(277, 453, 590, 579)
)

Target(
    id="social_club_send",
    search_region=(1708, 956, 1813, 1039)
)

Target(
    id="campaign_enter",
    click_pos=(1789, 847)
)

Target(
    id="campaign",
    search_region=(1480, 208, 1819, 513)
)

Target(
    id="bounty_enter",
    click_pos=(1098, 616)
)

Target(
    id="bounty",
    search_region=(1553, 955, 1818, 1035)
)

Target(
    id="bounty_ticket",
    search_region=(367, 140, 384, 167)
)

Target(
    id="bounty_enter_first",
    click_pos=(1135, 305)
)

Target(
    id="stage_enter_third",
    click_pos=(1685, 581)
)

Target(
    id="bounty_overpass",
    name="bounty",
    search_region=(616, 858, 886, 936)
)

Target(
    id="stage_sweep_max",
    click_pos=(1626, 451)
)

Target(
    id="stage_sweep_start",
    click_pos=(1404, 604)
)

Target(
    id="scrimmage_enter",
    click_pos=(1055, 887)
)

Target(
    id="scrimmage",
    search_region=(73, 110, 365, 216)
)

Target(
    id="scrimmage_trinity",
    search_region=(136, 426, 224, 520)
)

Target(
    id="stage_enter_first",
    click_pos=(1671, 279)
)

Target(
    id="mission_enter",
    click_pos=(1222, 366)
)

Target(
    id="mission_multi_sweep_enter",
    search_region=(699, 844, 901, 921)
)

Target(
    id="mission_multi_sweep",
    search_region=(790, 116, 1125, 204)
)

Target(
    id="mission_multi_sweep_highlight",
    search_region=(1459, 804, 1688, 957)
)

Target(
    id="mission_multi_sweep_max",
    click_pos=(1262, 882)
)

for i in range(7):
    Target(
        id=f"mission_multi_sweep_list_{i}",
        click_pos=(187 + i * 238, 244)
    )

Target(
    id="left_middle",
    click_pos=(208, 540)
)

Target(
    id="mission_multi_sweep_confirm",
    click_pos=(1150, 876)
)

Target(
    id="login_maintenance",
    search_region=(400, 150, 1600, 900)
)

Target(
    id="login_update",
    search_region=(400, 600, 1600, 900)
)

Target(
    id="mail_enter",
    click_pos=(1720, 58)
)
