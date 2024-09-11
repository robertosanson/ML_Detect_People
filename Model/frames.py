import cv2

def check_video_open(video_path):
    video = cv2.VideoCapture(video_path)
    if not video.isOpened():
        print("Error: Could not open video.")
    else:
        print("Video opened successfully.")
    video.release()


def get_video_fps(video_path):
    """
    Get the frames per second (FPS) of a video.
    
    :param video_path: Path to the video file.
    :return: The FPS of the video.
    """
    video = cv2.VideoCapture(video_path)
    fps = video.get(cv2.CAP_PROP_FPS)
    video.release()
    return fps

if __name__ == "__main__":
    video_path = "drone_footage.mp4"  # Replace this with the path to your video
    check_video_open(video_path)
    fps = get_video_fps(video_path)
    print(f"FPS of the video: {fps}")
