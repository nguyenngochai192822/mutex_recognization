"""
This code is responsible for getting optimum image width. If labels are long and the img_w is set to a small number, the
ctc-loss returns nan. To avoid this, run the following code to get optimal image width for your dataset.
For an eight-character to ten-character dataset a width of 100px is ok. I shall keep the same ratio for others.
"""
from argparse import ArgumentParser
from dataset import CRNNDataset


data_directory=r'E:\project_ai\Train\crnn_recognition\label\result_label_1'
alphabets='_#0123456789abcddefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ,.-%.'


def get_optimum_img_w(data_directory, alphabets):
    dataset = CRNNDataset(data_directory, alphabets)
    max_length = max(dataset.labels_length)
    optimal_width = (max_length // 8) * 100
    return max_length, optimal_width


if __name__ == '__main__':
    max_length, optimal_width = get_optimum_img_w(data_directory, alphabets)
    print(f'[INFO] max_length of this dataset is {max_length}, optimal img_w is: {optimal_width}')
