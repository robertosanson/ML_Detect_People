from video_utils import process_video
from clustering_estimator import estimate_crowd_density_frame

def main():
    video_path = "drone_footage.mp4"
    avg_people_kmeans = process_video(video_path, estimate_crowd_density_frame)
    print(f"Average number of people estimated using K-means: {avg_people_kmeans}")
if __name__ == "__main__":
    main()
