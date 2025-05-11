from target import *
from image_utils import *
from adb_utils import *
import arknights_target

sleep_duration = 1

def set_sleep_duration(new_value):
    """sleep_duration is the default sleep duration.
    If not specified in a function, this value will 
    be used for sleep time.
    """
    global sleep_duration
    sleep_duration = new_value
    
def slp():
    sleep(sleep_duration)

def do(target_id, end_target=None):
    """Give a target, this function will find the target and click it. 
    It will wait until the target image disappears, and proceed to the 
    next action.
    """
    target = Target.registry[target_id]
    match_pos = match_target_in_image(target)
    if (match_pos):
        click(target.click_pos or match_pos)
        print("Doing:", target.id)
    else:
        print("'Do' did not match target.")
        return
    
    # wait
    slp()
    
    # check if proceeded
    match_pos = match_target_in_image(target)
    while (match_pos != None):
        print("Waiting for", target_id, "to disappear.")
        slp()
        match_pos = match_target_in_image(target)

def expect(until_target_id, click_target_id=None):
    """Click target A repeatedly until we see target B.
    """
    until_target = Target.registry[until_target_id]
    if click_target_id: click_target = Target.registry[click_target_id]
    match_pos = match_target_in_image(until_target)
    
    count = 1
    while match_pos == None:
        if click_target_id: click(click_target.click_pos)
        print(f"Expecting: {until_target_id}, {count}", end="\r")
        slp()
        match_pos = match_target_in_image(until_target)
        count += 1
        