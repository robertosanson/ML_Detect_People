from Frame_based.video_utils import extract_frames
from detection import detect_people_pifpaf
from Frame_based.frames import check_video_open, get_video_fps
import cv2

def main():
    # Path to the video file (after downloading the video from YouTube)
    video_path = "drone_footage.mp4"
    check_video_open(video_path)
    fps = get_video_fps(video_path)
    print(f"FPS of the video: {fps}")
    # Parameters for frame extraction
    fps = 25 
    start_time = 14  
    end_time = 32    
    
    # Step 1: Extract frames
    extract_frames(video_path, start_time, end_time, fps)
    
    # Step 2: Detect people in the extracted frames
    avg_people = detect_people_pifpaf("frames/")
    # avg_people = detect_people("frames/")
    print(avg_people)

if __name__ == "__main__":
    main()
