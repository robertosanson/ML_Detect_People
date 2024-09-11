from ultralytics import YOLO
import os

def detect_people(frame_dir):
    """
    Detect people in each frame and return the count of people detected.
    
    :param frame_dir: Directory where the frames are saved.
    :param model_path: Path to the YOLO model.
    :return: Average number of people detected across all frames.
    """
    model = YOLO('yolov8x.pt')
    total_people = 0
    frame_count = 0

    for frame_file in os.listdir(frame_dir):
        if frame_file.endswith(".jpg"):
            frame_path = os.path.join(frame_dir, frame_file)
            results = model(frame_path, conf=0.1)  
            
            # Loop through detections in results
            people_count = 0
            for result in results:
                for detection in result.boxes:
                    if detection.cls == 0:  
                        people_count += 1
            
            total_people += people_count
            frame_count += 1

    avg_people = total_people / frame_count if frame_count else 0
    print(f"Average number of people detected: {avg_people}")
    return avg_people
