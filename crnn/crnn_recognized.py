from argparse import ArgumentParser
import cv2
import os
from PIL import Image
from deep_utils import CRNNInferenceTorch, split_extension, Box
import time


def predict(image, model):
    model = CRNNInferenceTorch(model)
    img = cv2.imread(image)
    tic = time.time()
    prediction = model.infer(image)
    prediction = "".join(prediction)
    toc = time.time()
    return prediction

input_folder = r'E:\project_ai\yolo\save_img_crop_1'
file_txt = "output_1.txt"
model= r"E:\project_ai\Train\crnn_recognition\train\haiii\output\exp_7\best.ckpt"
valid_img = []
file_list = sorted(os.listdir(input_folder))

all_predictions =[]
for file_name in file_list:
    if file_name.endswith('.jpg') or file_name.endswith('.png'):
        input_path = os.path.join(input_folder, file_name)
# im1=r"C:\Users\Hi\Downloads\toan.jpg"
        pre=predict(input_path,model)
        # all_predictions =[]
        all_predictions.append(pre)

        # output_strings = []
        # output_strings.append(out)

with open("output_1.txt", "a") as file:
    word_count = 0  # Biến đếm số từ

    for string in all_predictions:
        words = string.split()  # Tách các từ trong chuỗi

        for word in words:
            file.write(word + " ")
            word_count += 1

            if word_count % 30 == 0:  # Kiểm tra số từ đã ghi vào file
                file.write("\n")  # Thêm ký tự xuống dòng

    file.close()

print(all_predictions)