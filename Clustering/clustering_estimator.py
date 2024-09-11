import cv2
import numpy as np
from sklearn.cluster import KMeans

def estimate_crowd_density_frame(frame, num_clusters=5):
    """
    Estimate crowd density using K-means clustering on the current frame.
    """
    # Resize for faster computation
    frame = cv2.resize(frame, (640, 360)) 

    # Convert to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Reshape image into 2D pixel array
    pixel_values = gray.reshape((-1, 1))
    pixel_values = np.float32(pixel_values)

    # Apply K-means clustering
    kmeans = KMeans(n_clusters=num_clusters, random_state=42)
    labels = kmeans.fit_predict(pixel_values)

    # Reshape labels back into image dimensions
    clustered = labels.reshape(gray.shape)

    # Count the pixels in the densest cluster
    unique, counts = np.unique(clustered, return_counts=True)
    max_cluster_size = np.max(counts)

    # Approximate number of people based on a person-per-pixel factor
    people_per_pixel_factor = 15 
    estimated_people = max_cluster_size / people_per_pixel_factor

    return estimated_people
