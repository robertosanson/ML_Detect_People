# ML_Detect_People

Clustering Folder: 
    This project estimates the number of people in a video by applying K-means clustering on each video frame. It processes the video from 0:14 to 0:32 seconds and averages the number of people detected across the frames. This method works by grouping pixels into clusters and approximating the number of people in the densest clusters.
    The video is processed between 0:14 and 0:32 seconds only. This time range is configurable but has been chosen based on your project requirements.
    Each frame is extracted and resized to make the computation faster.
    The frames per second (FPS) of the video is used to determine the corresponding frame numbers for this time interval.
    Each frame is converted into a grayscale image, reducing the complexity of the data.
    The grayscale values are clustered into a set number of clusters (default is 5) using the K-means algorithm. This divides the image into different groups of similar pixel intensities.
    The largest cluster is assumed to represent the most densely populated region (i.e., where people are located).
    The number of pixels in the largest cluster is divided by a people-per-pixel factor to estimate the number of people in the frame.

Model Folder:
    This folder contains a failed attempt on estimating the amount of people that appear in the video. I tried using some models that should have been able to detect people in each frame and then divide by the frame count to get the average. This approach did not work since the resolution was terrible and the people couldn't be detected. I tried using other models that were supposedly better at detecting people but they didn't work either. This is the reason I went with the clustering method. 