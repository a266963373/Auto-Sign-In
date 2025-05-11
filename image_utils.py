import cv2
import numpy as np
import io
import adb_utils

def cv2_screenshot():
    """
    将 BytesIO 类型的截图数据流转换为 OpenCV 的 BGR 图像（numpy.ndarray）
    """
    data = np.frombuffer(io.BytesIO(adb_utils.screencap()).getvalue(), dtype=np.uint8)
    return cv2.imdecode(data, cv2.IMREAD_COLOR)

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
    full_image = cv2_screenshot()
    template_path = f"images/{target.name}.png"
    template = cv2.imread(template_path)
    # cv2.imshow("f", template)
    # cv2.waitKey(0)
    
    if template is None:
        print(f"[ERROR] 模板文件不存在: {template_path}")
        return False

    region = target.search_region or (0, 0, full_image.shape[1], full_image.shape[0])
    x, y, w, h = region
    search_area = full_image[y:y+h, x:x+w]
    # cv2.imshow("e", search_area)
    # cv2.waitKey(0)

    # result = cv2.matchTemplate(template, search_area, cv2.TM_CCOEFF_NORMED)
    result = cv2.matchTemplate(search_area, template, cv2.TM_CCOEFF_NORMED)
    _, max_val, _, max_loc = cv2.minMaxLoc(result)
    # print("Threshold for", target.id, "is:", max_val)
    match_x = x + max_loc[0]
    match_y = y + max_loc[1]
    # print(match_x, match_y)
    
    if max_val >= threshold:
        match_x = x + max_loc[0] + template.shape[1] // 2
        match_y = y + max_loc[1] + template.shape[0] // 2
        return (match_x, match_y)
    else:
        return None
    
if __name__ == "__main__":
    cv2.imwrite("images/screenshot.png", cv2_screenshot())
    
