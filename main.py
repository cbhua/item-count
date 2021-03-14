import os
import cv2
import configparser
from src.item_count import item_count

config = configparser.ConfigParser()
config.read('config.ini')

for root, dirs, files in os.walk('./data/input'):
    for file in files:
        if not file.endswith('.png') and not file.endswith('.jpg'):
            continue
        output, result = item_count(src=os.path.join(root, file), 
                                    gray_method=config['default']['gray_method'], 
                                    blur_ksize=(int(config['default']['blur_ksize_horizontal']), int(config['default']['blur_ksize_vertical'])), 
                                    blur_sigmaX=float(config['default']['blur_sigmaX']), 
                                    bin_threshold=int(config['default']['bin_threshold']), 
                                    rm_noise_shape=config['default']['rmnoise_shape'], 
                                    rm_noise_ksize=(int(config['default']['rmnoise_ksize_horizontal']), int(config['default']['rmnoise_ksize_vertical'])), 
                                    rm_noise_method=config['default']['rmnoise_method'], 
                                    find_mode=config['default']['find_mode'], 
                                    find_method=config['default']['find_method']
                                    )
        
        print('[Successfully] Processed {}, total count: {}'.format(file, result))
        cv2.imwrite('data/output/' + file, output)
    
    print('[DONE]')