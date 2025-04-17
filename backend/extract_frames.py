import cv2, os

def extract_frames(video_dir, output_dir):
    os.makedirs(output_dir, exist_ok=True)
    for video in os.listdir(video_dir):
        cap = cv2.VideoCapture(os.path.join(video_dir, video))
        frame_count = 0
        while cap.isOpened():
            ret, frame = cap.read()
            if not ret: break
            if frame_count % 10 == 0:
                cv2.imwrite(os.path.join(output_dir, f"{video}_{frame_count}.jpg"), frame)
            frame_count += 1
        cap.release()
