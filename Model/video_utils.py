import cv2
import os

def extract_frames(video_path, start_time, end_time, fps, output_dir="frames/"):
    """
    Extract frames from a video between start_time and end_time and save them as images.
    
    :param video_path: Path to the video file.
    :param start_time: Start time in seconds.
    :param end_time: End time in seconds.
    :param fps: Frames per second of the video.
    :param output_dir: Directory where frames will be saved.
    """
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    video = cv2.VideoCapture(video_path)
    current_frame = 0
    start_frame = int(start_time * fps)
    end_frame = int(end_time * fps)

    while video.isOpened():
        ret, frame = video.read()
        if not ret or current_frame > end_frame:
            break

        if start_frame <= current_frame <= end_frame:
            cv2.imwrite(f"{output_dir}/frame_{current_frame}.jpg", frame)

        current_frame += 1
    video.release()
    print(f"Frames extracted from {start_time} to {end_time} seconds.")
