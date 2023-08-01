import cv2
import os
def extract_frames(video_path, output_folder, frame_rate):
    # Đọc video
    video_capture = cv2.VideoCapture(video_path)
    total_frames = int(video_capture.get(cv2.CAP_PROP_FRAME_COUNT))

    # Tính số frame cần trích xuất
    frames_to_extract = int(total_frames / frame_rate)

    # Biến đếm frame
    frame_count = 0

    while video_capture.isOpened() and frame_count < frames_to_extract:
        # Đọc frame
        ret, frame = video_capture.read()

        if not ret:
            break

        # Lưu frame thành ảnh
        output_path = f"{output_folder}/frame_{frame_count}.jpg"
        cv2.imwrite(output_path, frame)

        # Di chuyển tới frame tiếp theo
        frame_count += 1
        video_capture.set(cv2.CAP_PROP_POS_FRAMES, frame_count * frame_rate)

    # Giải phóng tài nguyên
    video_capture.release()

# Thực hiện trích xuất
video_path = r"E:\project_ai\input\video_thaygui.mp4"  # Đường dẫn tới video
output_folder = r"E:\project_ai\extract_video\output_extract_1"  # Thư mục lưu trữ các ảnh trích xuất
frame_rate = 50  # Tần suất trích xuất150 (//giây/1 khung hình)

for file_name in os.listdir(output_folder):
    file_path = os.path.join(output_folder, file_name)
    if os.path.isfile(file_path):
        os.remove(file_path)

extract_frames(video_path, output_folder, frame_rate)
