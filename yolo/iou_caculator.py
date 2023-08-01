def calculate_iou(box1, box2):

    xmin_inter = max(box1[0], box2[0])
    ymin_inter = max(box1[1], box2[1])
    xmax_inter = min(box1[2], box2[2])
    ymax_inter = min(box1[3], box2[3])


    intersection = max(0, xmax_inter - xmin_inter + 1) * max(0, ymax_inter - ymin_inter + 1)


    area_box1 = (box1[2] - box1[0] + 1) * (box1[3] - box1[1] + 1)
    area_box2 = (box2[2] - box2[0] + 1) * (box2[3] - box2[1] + 1)
    union = area_box1 + area_box2 - intersection


    iou = intersection / union #iou caculator

    return iou


def calculate_iou_for_boxes(boxes):
    num_boxes = len(boxes)
    iou_matrix = [[0] * num_boxes for _ in range(num_boxes)]  # Ma trận lưu kết quả IoU

    for i in range(num_boxes):
        for j in range(num_boxes):
            iou = calculate_iou(boxes[i], boxes[j])
            iou_matrix[i][j] = iou

    return iou_matrix
def calculate_area(box):
    width = box[2] - box[0]
    height = box[3] - box[1]
    area = width * height
    return area

def check_duplicate_frames(frames):
    num_frames = len(frames)
    if num_frames < 2:
        return frames

    # Lấy 4 hộp giới hạn đầu tiên của hai khung hình liên tiếp
    box_count = min(4, len(frames[0][1]), len(frames[1][1]))
    boxes1 = frames[0][1][:box_count]
    boxes2 = frames[1][1][:box_count]

    # Tính IoU trung bình của các cặp giới hạn tương ứng
    total_iou = sum(calculate_iou(box1, box2) for box1, box2 in zip(boxes1, boxes2)) / box_count

    if total_iou > 0.8:
        # Nếu IoU trung bình lớn hơn 0.8, loại bỏ khung hình thứ hai và nội dung tương ứng
        return [frames[0]] + check_duplicate_frames(frames[2:])
    else:
        # Nếu không, giữ cả hai khung hình và kiểm tra tiếp các khung hình còn lại
        return [frames[0]] + check_duplicate_frames(frames[1:])