import uuid

from ultralytics import YOLO
from PIL import Image
from iou_caculator import *
import cv2
import os
import matplotlib.pyplot as plt


class Yolov8Mutex(object):
    def __init__(self, model_path):
        self.model = YOLO(model_path)
        self.thresh_score = 0.5

    def predict(self, img):
        results = self.model.predict(source=img, save=False)
        list_box_rs = []
        for result in results:
            box_list = result.boxes.xyxy.tolist()
            score_list = result.boxes.conf.tolist()
            for i, score in enumerate(score_list):
                if score >= self.thresh_score:
                    list_box_rs.append([int(item) for item in box_list[i]])
        return list_box_rs
# model_path = r'E:\project_ai\yolo\weight\best.pt'
# yolov8 = Yolov8Mutex(model_path)
# img_path=r"E:\project_ai\extract_video\output_extract\frame_1.jpg"
# im1 = cv2.imread(img_path)
# list_box_rs_all = yolov8.predict(im1)
# # img_path=r"E:\project_ai\extract_video\output_extract\frame_1.jpg"
# # im1 = cv2.imread(img_path)
# for box in list_box_rs_all:
#     cv2.rectangle(im1, (box[0], box[1]), (box[2], box[3]), (0, 0, 255), thickness=2)
#
# cv2.imshow("test.jpg", im1)
# cv2.waitKey(0)
# iou_matrix = calculate_iou_for_boxes(list_box_rs_all)

def filter_box(list_box_rs_all):
    # iou_matrix = calculate_iou_for_boxes(list_box_rs_all)
    # for i in range(len(list_box_rs_all)):
    #     for j in range(i+1,len(list_box_rs_all)):
    filtered_boxes = []
    for box in list_box_rs_all:
        if len(filtered_boxes) == 0:
            filtered_boxes.append(box)
        else:
            prev_box = filtered_boxes[-1]
            iou = calculate_iou(prev_box, box)
            if iou > 0.8:
                if calculate_area(box) > calculate_area(prev_box):
                    filtered_boxes[-1] = box
            else:
                filtered_boxes.append(box)
    return filtered_boxes

def sort_box(filtered_box):
    sortted_xmin = sorted(filtered_box, key=lambda box: box[1])
    lines = []

    if len(sortted_xmin) > 0:
        first_box = sortted_xmin[0]
        ymin = first_box[1]
        ymax = first_box[3]
        y_center = (ymin + ymax) / 2
        lines.append([first_box])

        for box in sortted_xmin[1:]:
            ymin = box[1]
            ymax = box[3]

            if ymin <= y_center:
                lines[-1].append(box)
            else:
                lines.append([box])
                y_center = (ymin + ymax) / 2

    lines_final = []
    for line in lines:
        line = sorted(line, key=lambda x: x[0])
        lines_final.append(line)
    return lines_final

def crop_image(im1, list_box_rs_all):
    cropped_images = []
    for lines in list_box_rs_all:
        for box in lines:
            xmin, ymin, xmax, ymax = box[0], box[1], box[2], box[3]
            cropped_image = im1.crop((xmin, ymin, xmax, ymax))
            cropped_images.append(cropped_image)
    return cropped_images




input_folder = r'E:\project_ai\extract_video\output_extract_1'
file_list = sorted(os.listdir(input_folder))
model_path = r'E:\project_ai\yolo\weight\best.pt'
yolov8 = Yolov8Mutex(model_path)

path_folder_save = "save_img_crop_1"
for file_name in os.listdir(path_folder_save):
    file_path = os.path.join(path_folder_save, file_name)
    if os.path.isfile(file_path):
        os.remove(file_path)

for file_name in file_list:
    if file_name.endswith('.jpg') or file_name.endswith('.png'):
        input_path = os.path.join(input_folder, file_name)

        im1 = Image.open(input_path)
# model_path = r'C:\Users\Hi\Downloads\data_train_box\best.pt'
# im1 = Image.open(img_path)
# Create an instance of the YoloV8_mutex class
# yolov8 = Yolov8Mutex(model_path)
# Perform object detection on the image
        list_box_rs_all = yolov8.predict(im1)
        iou_matrix = calculate_iou_for_boxes(list_box_rs_all)
        filtered_box = filter_box(list_box_rs_all)

        sort = sort_box(list_box_rs_all)
        # path_folder_save = "save_img_crop"
        if not os.path.exists(path_folder_save):
            os.mkdir(path_folder_save)
        cropped_images = crop_image(im1, sort)
        name_save =  uuid.uuid4().hex
        # name = "image"
        for i, img in enumerate(cropped_images):
            img.save(os.path.join(path_folder_save,name_save+ str(i) + ".jpg"))

# print(list_box_rs_all)
# im1 = cv2.imread(img_path)
# for box in list_box_rs_all:
#     cv2.rectangle(im1, (box[0], box[1]), (box[2], box[3]), (0, 0, 255), thickness=2)
#
# cv2.imshow("test.jpg", im1)
# cv2.waitKey(0)
# iou_matrix = calculate_iou_for_boxes(list_box_rs_all)


# for i in range(len(list_box_rs_all)):
#     for j in range(i+1,len(list_box_rs_all)):
#         print(f"IoU between box {i+1} and box {j+1}: {iou_matrix[i][j]}")
#
# def filter_box(list_box_rs_all):
#     # iou_matrix = calculate_iou_for_boxes(list_box_rs_all)
#     # for i in range(len(list_box_rs_all)):
#     #     for j in range(i+1,len(list_box_rs_all)):
#     filtered_boxes = []
#     for box in list_box_rs_all:
#         if len(filtered_boxes) == 0:
#             filtered_boxes.append(box)
#         else:
#             prev_box = filtered_boxes[-1]
#             iou = calculate_iou(prev_box, box)
#             if iou > 0.8:
#                 if calculate_area(box) > calculate_area(prev_box):
#                     filtered_boxes[-1] = box
#             else:
#                 filtered_boxes.append(box)
#     return filtered_boxes
#
#
# filtered_box = filter_box(list_box_rs_all)


# def sort_box(filtered_box):
#     sortted_xmin = sorted(filtered_box, key=lambda box: box[1])
#     lines = []
#
#     if len(sortted_xmin) > 0:
#         first_box = sortted_xmin[0]
#         ymin = first_box[1]
#         ymax = first_box[3]
#         y_center = (ymin + ymax) / 2
#         lines.append([first_box])
#
#         for box in sortted_xmin[1:]:
#             ymin = box[1]
#             ymax = box[3]
#
#             if ymin <= y_center:
#                 lines[-1].append(box)
#             else:
#                 lines.append([box])
#                 y_center = (ymin + ymax) / 2
#
#     lines_final = []
#     for line in lines:
#         line = sorted(line, key=lambda x: x[0])
#         lines_final.append(line)
#     return lines_final


# sort = sort_box(list_box_rs_all)
# for i in sort:
#     print(i)





# path_folder_save = "save_img_crop"
# if not os.path.exists(path_folder_save):
#     os.mkdir(path_folder_save)
# cropped_images = crop_image(im1, sort)
# name_save = uuid.uuid4().hex
# for i, img in enumerate(cropped_images):
#     img.save(os.path.join(path_folder_save, name_save + str(i) + ".jpg"))
