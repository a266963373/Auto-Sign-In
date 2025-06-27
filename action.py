from target import *
from image_utils import *
from input_utils import *
from time import sleep
from operator import add
import winsound

sleep_duration = 1
cur_id = None        # record current id so no need to expect a scene every time

def reset_init():
    global cur_id
    cur_id = None 

def set_sleep_duration(new_value):
    """sleep_duration is the default sleep duration.
    If not specified in a function, this value will 
    be used for sleep time.
    """
    global sleep_duration
    sleep_duration = new_value
    # print("Sleep duration is", sleep_duration)
    
def slp():
    sleep(sleep_duration)
    
def target_click(target, shift=None):
    if isinstance(target.click_pos, tuple):  # is single pos
        _pos = target.click_pos
        if shift: _pos = tuple(map(add, target.click_pos, shift))
        click(_pos)
        sleep(0.5)
    else:
        for _pos in target.click_pos:
            if shift: _pos = tuple(map(add, _pos, shift))
            click(_pos)
            sleep(0.5)

def do(target_id, threshold=0.95, find_it=False, shift=None):
    """Give a target, this function will find the target and click it. 
    """
    target = Target.get(target_id)

    if not find_it:
        # act as only click()
        target_click(target, shift=shift)
        print("Doing:", target.id)
        return
    
    # otherwise, find it and click
    match_pos = match_target_in_image(target, threshold=threshold)
    while not match_pos:
        slp()
        match_pos = match_target_in_image(target, threshold=threshold)
    if shift: match_pos = tuple(map(add, match_pos, shift))
    click(match_pos)
    sleep(0.5)
    print("Doing:", target.id)

def expect(until_target_id, click_target_id=None, max_count=13, threshold=0.95, 
           find_it=False, to_disappear=False, in_hurry=False):
    """Click target A repeatedly until we see target B.
    Update cur_id afterwards.
    """
    global cur_id
    
    if not find_it and not to_disappear \
        and until_target_id == cur_id: return True     # stage successfully expected
    
    until_target = Target.get(until_target_id)
    if click_target_id: click_target = Target.get(click_target_id)
    match_pos = match_target_in_image(until_target, threshold)
    
    count = 0
    while True:
        if to_disappear:
            if match_pos == None:
                cur_id = None
                return None
        else:
            if match_pos: break

        count += 1
        if count >= max_count:
            print(f"Stop expecting {until_target_id}.")
            if max_count == 13:
                print("Script is wrong. Exiting.")
                winsound.Beep(1000, 500)
                exit()
            return None
        
        if click_target_id: 
            if in_hurry:
                target_click(click_target)
                target_click(click_target)
            target_click(click_target)
        elif count > 0 and count % 2 == 0: click_last_clicked_pos()   # if loading caused missing input

        print(f"Expecting: {until_target_id}, {count}", end="\r")
        slp()
        print("Sleep duration is", sleep_duration)

        match_pos = match_target_in_image(until_target, threshold)

    cur_id = until_target.id
    # print(match_pos)
    return match_pos

def stay(target_id, duration=1000):     # don't want to overlap name with "hold"
    target = Target.get(target_id)
    x, y = target.click_pos
    input_utils.hold(x, y, duration)

def see(until_target_id, threshold=0.95, find_it=False):
    return expect(until_target_id, max_count=1, threshold=threshold, find_it=find_it)

def see_what(*target_id_list):
    take_new_image()
    set_take_new_image(False)
    for target_id in target_id_list:
        if see(target_id):
            set_take_new_image(True)
            return target_id
    set_take_new_image(True)
    return None

def what_number(target_id, is_compare=False, no_second_chance=False, 
                return_digit=0):
    target = Target.get(target_id)
    return extract_digits(target, is_compare, no_second_chance, return_digit)

def what_hanzi(target_id, candidate_words=None, patch_pair=None):
    target = Target.get(target_id)
    return read_hanzi(target, candidate_words, patch_pair)

def what_english(target_id):
    target = Target.get(target_id)
    return read_english(target)
    