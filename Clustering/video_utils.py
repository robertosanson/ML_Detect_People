import cv2

def process_video(video_path, process_frame_function, start_time=14, end_time=32):
    """
    Process the video frame by frame from start_time to end_time and apply the given frame processing function.
    
    :param video_path: Path to the video file
    :param process_frame_function: A function to apply on each frame (e.g., K-means, ROI, or blob detection)
    :param start_time: Start time in seconds (default is 14 seconds)
    :param end_time: End time in seconds (default is 32 seconds)
    :return: Aggregated results across the specified frame range
    """
    cap = cv2.VideoCapture(video_path)
    total_estimated_people = 0
    frame_count = 0

    # Check if video opened successfully
    if not cap.isOpened():
        print(f"Error: Could not open video {video_path}")
        return None

    # Get the video's frames per second (FPS)
    fps = cap.get(cv2.CAP_PROP_FPS)
    if fps == 0:
        print("Error: Could not retrieve FPS from video.")
        return None
    print("fps:", fps)
    # Calculate frame numbers for the specified time range
    start_frame = int(start_time * fps)
    end_frame = int(end_time * fps)

    current_frame = 0

    while True:
        ret, frame = cap.read()
        if not ret:
            break 

        if current_frame >= start_frame and current_frame <= end_frame:
            # Process the current frame with the provided function
            estimated_people = process_frame_function(frame)
            total_estimated_people += estimated_people
            frame_count += 1

        current_frame += 1
        print("current Frame: ", current_frame)
        # Stop processing if we go beyond the end_frame
        if current_frame > end_frame:
            break

    cap.release()
    
    # Return the average number of people estimated across the specified frames
    if frame_count > 0:
        return total_estimated_people / frame_count
    else:
        return 0
