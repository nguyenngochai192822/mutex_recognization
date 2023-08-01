""" Get all the required stats
"""
from argparse import ArgumentParser
from dataset import get_mean_std
from get_optimum_img_w import get_optimum_img_w
from get_character_sets import get_unique_characters



data_directory=r'E:\project_ai\Train\crnn_recognition\label\result_label_1'
batch_size=9
img_h=32

if __name__ == '__main__':
    alphabets = get_unique_characters(data_directory)
    max_length, optimal_width = get_optimum_img_w(data_directory, alphabets)
    mean, std = get_mean_std(data_directory, alphabets, batch_size, img_h, optimal_width)
    print(f"[INFO] Stats: alphabets: {alphabets}, img_w: {optimal_width}, mean: {mean}, std: {std}")

