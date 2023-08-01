"""
This code is responsible for getting unique characters to be used as outputs of CTC loss.
"""
import os
from argparse import ArgumentParser
from dataset import CRNNDataset

data_directory=r'C:\Users\Hi\Downloads\haiiiiiiiiiiii\train'


def get_unique_characters(data_directory):
    unique_characters = set()
    for name in os.listdir(data_directory):
        unique_characters |= set(CRNNDataset.get_label(name))
    unique_characters = "".join(sorted(unique_characters))
    return unique_characters


if __name__ == '__main__':
    characters = get_unique_characters(data_directory)
    print(f'[INFO] characters: {characters}')
