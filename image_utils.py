import cv2
import numpy as np
import io
import input_utils
import pytesseract
import re

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
game_name = ""  # for determine which folder to get image from
full_image = None
is_take_new_image = True

def set_game_name_for_image(n):
    global game_name
    game_name = n

def set_take_new_image(b):
    global is_take_new_image
    is_take_new_image = b

def take_new_image():
    global full_image
    full_image = input_utils.screencap()
    
def image_of_area(target):
    global full_image
    if is_take_new_image:
        full_image = input_utils.screencap()
    region = target.search_region or (0, 0, full_image.shape[1], full_image.shape[0])
    x, y, w, h = region
    w -= x
    h -= y
    return full_image[y:y+h, x:x+w]

def match_target_in_image(target, threshold=0.95) -> bool:
    """
    判断指定 target 是否在 full_image 中出现。
    自动读取模板图像并调用模板匹配。

    参数：
        target: Target 对象（含 name 和 search_region）
        threshold: 匹配阈值（默认 0.95）

    返回：
        target 在图片中的位置 + 自己的size的一半，也就是图片中间；或 None
    """
    template_path = f"images/{game_name}/{target.name}.png"
    template = cv2.imread(template_path)
    # cv2.imshow("f", template)
    # cv2.waitKey(0)
    
    if template is None:
        print(f"[ERROR] 模板文件不存在: {template_path}")
        return False

    search_area = image_of_area(target)
    # cv2.imshow("e", search_area)
    # cv2.waitKey(0)

    # result = cv2.matchTemplate(template, search_area, cv2.TM_CCOEFF_NORMED)
    result = cv2.matchTemplate(search_area, template, cv2.TM_CCOEFF_NORMED)
    _, max_val, _, max_loc = cv2.minMaxLoc(result)
    print("Threshold for", target.id, "is:", max_val)
    
    region = target.search_region or (0, 0, 0, 0)
    x, y, _, _ = region
    match_x = x + max_loc[0]
    match_y = y + max_loc[1]
    # print(match_x, match_y)
    
    if max_val >= threshold:
        match_x = x + max_loc[0] + template.shape[1] // 2
        match_y = y + max_loc[1] + template.shape[0] // 2
        return (match_x, match_y)
    else:
        return None
    
def parse_number(s):
    s = s.lower().replace(",", "").strip()
    if s.endswith('k'):
        if len(s) == 1:
            return 1000
        return int(float(s[:-1]) * 1000)
    elif s.endswith('m'):
        if len(s) == 1:
            return 10000
        return int(float(s[:-1]) * 1_000_000)
    else:
        return int(re.sub(r"[^\d]", "", s))  # 去掉非数字字符
    
def extract_digits(target, is_compare=False, no_second_chance=False, 
                   return_digit=0):
    count = 0
    while True:
        image = image_of_area(target)
        
        # cv2.imshow('s', image)
        # cv2.waitKey(0)
        # cv2.destroyAllWindows()
        scale_factor = count + 2
        image = cv2.resize(image, None, fx=scale_factor, fy=scale_factor, interpolation=cv2.INTER_CUBIC)

        config = r'--psm 6 -c tessedit_char_whitelist=0123456789kKmM/-'
        text = pytesseract.image_to_string(image, config=config)
        print(f"识别文本: {text}")
        
        if is_compare:
            match_fraction = re.match(r'([0-9kKmM.]+)\s*/\s*([0-9kKmM.]+)', text)
            if match_fraction:
                num = parse_number(match_fraction.group(1))
                den = parse_number(match_fraction.group(2))

                if return_digit == 0:
                    print(f"比较数字: {num}/{den}")
                    return num > den
                if return_digit == -1:  # return the ratio
                    print(f"比较数字: {num}/{den}")
                    return num / den
                elif return_digit == 1:
                    print(f"找到数字: {num}")
                    return num
                elif return_digit == 2:
                    print(f"找到数字: {den}")
                    return den

        else:
            match = re.search(r'\d+', text)
            print(f"找到数字: {match}")
            if match != None:
                return int(match.group())

        if no_second_chance:
            return -1
        
        count += 1
        if count >= 3:
            return -1
        take_new_image()
    
def read_hanzi(target, candidate_words=None, patch_pair=None):
    count = 0
    while True:
        image = image_of_area(target)
        # cv2.imshow("e", image)
        # cv2.waitKey(0)
        text = pytesseract.image_to_string(image, lang="chi_sim")
        text = re.sub(r"\s+", "", text)
        print(f"🈶 识别到的汉字内容：{text}")
        if candidate_words is None or text in candidate_words:
            break
        if patch_pair and patch_pair[0] in text:
            text = patch_pair[1]
            break

        count += 1
        if count > 5:
            return None
            
    return text

def read_english(target):
    image = image_of_area(target)
    text = pytesseract.image_to_string(image, lang="eng")  # 使用英文识别
    text = re.sub(r"\s+", "", text)  # 去掉所有空白字符
    print(f"🔤 识别到的英文内容：{text}")
        
    return text
    
if __name__ == "__main__":
    input_utils.set_is_using_adb(True)
    # input_utils.set_is_using_adb(False)
    # cv2.imwrite("images/screenshot.png", input_utils.screencap())
    # cv2.imwrite("images/arknights/screenshot.png", input_utils.screencap())
    # cv2.imwrite("images/blue archive/screenshot.png", input_utils.screencap())
    cv2.imwrite("images/azur lane/screenshot.png", input_utils.screencap())
    