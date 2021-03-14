import cv2 
import numpy as np
import matplotlib.pyplot as plt


def item_count(src: str, 
               gray_method: str, 
               blur_ksize: tuple, 
               blur_sigmaX: float, 
               bin_threshold: int,
               rm_noise_shape: str,
               rm_noise_ksize: tuple, 
               rm_noise_method: str, 
               find_mode: str, 
               find_method: str
               ):
    img = cv2.imread(src)

    if gray_method == 'COLOR_BGR2GRAY':
        gray = cv2.cvtColor(src=img, code=cv2.COLOR_BGR2GRAY)
    elif gray_method == 'COLOR_RGB2GRAY':
        gray = cv2.cvtColor(src=img, code=cv2.COLOR_RGB2GRAY)
    else:
        print('[Warnning] Undefined Method for Gray Process, using default method: COLOR_BGR2GRAY')
        gray = cv2.cvtColor(src=img, code=cv2.COLOR_BGR2GRAY)
    
    blur = cv2.GaussianBlur(src=gray,ksize=blur_ksize,sigmaX=blur_sigmaX)
    _, dst = cv2.threshold(blur, bin_threshold, 255, 0, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    if rm_noise_shape == 'MORPH_RECT':
        kernel = cv2.getStructuringElement(shape=cv2.MORPH_RECT, ksize=rm_noise_ksize)
    elif rm_noise_shape == 'MORPH_ELLIPSE':
        kernel = cv2.getStructuringElement(shape=cv2.MORPH_ELLIPSE, ksize=rm_noise_ksize)
    elif rm_noise_shape == 'MORPH_CROSS':
        kernel = cv2.getStructuringElement(shape=cv2.MORPH_CROSS, ksize=rm_noise_ksize)
    else: 
        print('[Warnning] Undefined Method for Removing Noise Element, using default method: MORPH_ELLIPSE')
        kernel = cv2.getStructuringElement(shape=cv2.MORPH_ELLIPSE, ksize=rm_noise_ksize)

    if rm_noise_method == 'MORPH_OPEN':
        rmnoise = cv2.morphologyEx(src=dst, op=cv2.MORPH_OPEN, kernel=kernel)
    elif rm_noise_method == 'MORPH_CLOSE':
        rmnoise = cv2.morphologyEx(src=dst, op=cv2.MORPH_CLOSE, kernel=kernel)
    else:
        print('[Warnning] Undefined Method for Removing Noise Method, using default method: MORPH_OPEN')
        rmnoise = cv2.morphologyEx(src=dst, op=cv2.MORPH_OPEN, kernel=kernel)

    if find_mode == 'RETR_LIST':
        if find_method == 'CHAIN_APPROX_NONE':
            contours, _ = cv2.findContours(image=rmnoise, mode=cv2.RETR_LIST, method=cv2.CHAIN_APPROX_NONE)
        elif find_method == 'CHAIN_APPROX_SIMPLE':
            contours, _ = cv2.findContours(image=rmnoise, mode=cv2.RETR_LIST, method=cv2.CHAIN_APPROX_SIMPLE)
        else:
            print('[Warnning] Undefined Method for Finding Method, using default method: CHAIN_APPROX_NONE')
            contours, _ = cv2.findContours(image=rmnoise, mode=cv2.RETR_LIST, method=cv2.CHAIN_APPROX_NONE)
    elif find_mode == 'RETR_TREE':
        if find_method == 'CHAIN_APPROX_NONE':
            contours, _ = cv2.findContours(image=rmnoise, mode=cv2.RETR_TREE, method=cv2.CHAIN_APPROX_NONE)
        elif find_method == 'CHAIN_APPROX_SIMPLE':
            contours, _ = cv2.findContours(image=rmnoise, mode=cv2.RETR_TREE, method=cv2.CHAIN_APPROX_SIMPLE)
        else:
            print('[Warnning] Undefined Method for Finding Method, using default method: CHAIN_APPROX_NONE')
            contours, _ = cv2.findContours(image=rmnoise, mode=cv2.RETR_TREE, method=cv2.CHAIN_APPROX_NONE)
    else:
        print('[Warnning] Undefined Method for Finding Mode, using default method: RETR_TREE')
        if find_method == 'CHAIN_APPROX_NONE':
            contours, _ = cv2.findContours(image=rmnoise, mode=cv2.RETR_TREE, method=cv2.CHAIN_APPROX_NONE)
        elif find_method == 'CHAIN_APPROX_SIMPLE':
            contours, _ = cv2.findContours(image=rmnoise, mode=cv2.RETR_TREE, method=cv2.CHAIN_APPROX_SIMPLE)
        else:
            print('[Warnning] Undefined Method for Finding Method, using default method: CHAIN_APPROX_NONE')
            contours, _ = cv2.findContours(image=rmnoise, mode=cv2.RETR_TREE, method=cv2.CHAIN_APPROX_NONE)

    return DrawItems(src=img, contours=contours, threshold=5)


def DrawItems(src, contours, threshold):
    count = 0

    for cont in contours:
        if cv2.contourArea(cont) < threshold: 
            continue
        count += 1 

        rect = cv2.boundingRect(cont)
        cv2.rectangle(src, rect, (0, 0, 0xff), 1)

        y = 10 if rect[1] < 10 else rect[1]
        cv2.putText(src, str(count), (rect[0], y), cv2.FONT_HERSHEY_COMPLEX, 0.4, (0, 255, 0), 1)
        
    return src, count