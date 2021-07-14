import argparse
import logging
from typing import Tuple

import torch
import os
from os.path import dirname as path_up
import matplotlib.pyplot as plt
import numpy as np
import imageio
from PIL import Image, ImageSequence
import test_simple
from glob import glob
from torch import nn
from datetime import datetime
import logging

def parse_args():
    parser = argparse.ArgumentParser(
        description='Simple testing funtion for Monodepthv2 models.')

    parser.add_argument('--image_path', type=str,
                        help='path to a test image or folder of images', required=True)
    parser.add_argument('--ext', type=str,
                        help='image extension to search for in folder', default="jpg")
   

    return parser.parse_args()


def create_gif(img_frames_path, gif_path, gif_name):
    png_dir = img_frames_path
    images = []
    for file_name in sorted(os.listdir(png_dir)):
        if file_name.endswith('.png'):
            file_path = os.path.join(png_dir, file_name)
            images.append(imageio.imread(file_path))
    imageio.mimsave(gif_path + "/" + gif_name, images)

def combine_gifs(gif_path):
    gif1 = imageio.get_reader(gif_path + "/" + "actualgif.gif")
    gif2 = imageio.get_reader(gif_path + "/" + "depthgif.gif")

    #If they don't have the same number of frame take the shorter
    number_of_frames = min(gif1.get_length(), gif2.get_length())

    #Create writer object
    new_gif = imageio.get_writer(gif_path + "/" + 'output.gif')

    for frame_number in range(number_of_frames):
        img1 = gif1.get_next_data()
        img2 = gif2.get_next_data()
        h1, w1, c1 = img1.shape
        h2, w2, c2 = img2.shape
        img1 = Image.fromarray(img1).resize((min(w1, w2), min(h1, h2)))
        img2 = Image.fromarray(img2).resize((min(w1, w2), min(h1, h2)))
        #here is the magic
        new_image = np.vstack((img1, img2))
        new_gif.append_data(new_image)

    gif1.close()
    gif2.close()
    new_gif.close()

if __name__ == '__main__':
    args = parse_args()
    test_simple.test(args)

    original_path = args.image_path
    directory = "assets/output"

    latest_subdir = max(glob(os.path.join(directory, '*/')), key=os.path.getmtime)
    disp_path = latest_subdir


    gif_path = os.path.join("assets/gifs",datetime.now().strftime('%Y-%m-%d_%H-%M-%S'))
    os.makedirs(gif_path)

    create_gif(original_path, gif_path, "actualgif.gif")
    create_gif(disp_path, gif_path, "depthgif.gif")
    combine_gifs(gif_path)
