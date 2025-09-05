# glyph_607 – LOW_LIGHT_VISION
# Enhance image for low-light navigation

import cv2

def glyph_607(image_path):
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    return cv2.equalizeHist(img)
