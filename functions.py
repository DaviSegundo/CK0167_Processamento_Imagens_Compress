import os
import time
import numpy as np
from rle import encode, decode
from alive_progress import alive_bar

def generate_hw(fator, shape):
    h = shape[1]
    w = shape[0]
    height = int(np.floor(h * fator))
    width = int(np.floor(w * fator))
    return height, width

def split_channels(small_image):
    ch0 = small_image[:, :, 0]
    ch1 = small_image[:, :, 1]
    ch2 = small_image[:, :, 2]

    s_blue = np.array(ch0)
    s_green = np.array(ch1)
    s_red = np.array(ch2)
    return s_blue, s_green, s_red

def encode_arrays(s_blue, s_green, s_red):
    sencoded_blue = np.array(encode(s_blue), dtype=np.uint8)
    sencoded_green = np.array(encode(s_green), dtype=np.uint8)
    sencoded_red = np.array(encode(s_red), dtype=np.uint8)

    sencrypted_array = [sencoded_red, sencoded_green, sencoded_blue]
    sencrypted_array = np.array(sencrypted_array, dtype=object)

    with alive_bar(300, force_tty=True) as bar:
        for i in range(300):
            time.sleep(0.003)
            bar()

    return sencrypted_array

def decode_arrays(sloaded, width, height):
    srl, sgl, sbl = sloaded[0], sloaded[1], sloaded[2]

    received_red = decode(srl, (width, height))
    received_green = decode(sgl, (width, height))
    received_blue = decode(sbl, (width, height))

    completed_img = np.zeros((width, height, 3)).astype(np.uint8)
    completed_img[:, :, 0] = received_blue
    completed_img[:, :, 1] = received_green
    completed_img[:, :, 2] = received_red

    with alive_bar(300, force_tty=True) as bar:
        for i in range(300):
            time.sleep(0.003)
            bar()


    return completed_img

def bar_generate_view():
    with alive_bar(200, force_tty=True) as bar:
        for i in range(200):
            time.sleep(0.003)
            bar()

def calculate_stats(file_path, output_path):
    normal_file = os.path.getsize(file_path)
    compress_file = os.path.getsize(output_path)
    percentage = (compress_file*100)/normal_file

    print("#### General stats about compression ####")
    print(f"The size of ORIGINAL file is:    {normal_file/1024:.2f} KB")
    print(f"The size of COMPRESSED file is:  {compress_file/1024:.2f} KB")
    print(f"The COMPRESSION percentage is:   {100-percentage:.2f}%\n")
