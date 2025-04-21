import numpy as np
from scipy.spatial import distance
import matplotlib.pyplot as plt

# Sample data points
point1 = np.array([1, 2])
point2 = np.array([4, 6])

# 1. Euclidean Distance
def euclidean_distance(p1, p2):
    return np.sqrt(np.sum((p1 - p2) ** 2))

# Alternative using numpy
def euclidean_distance_np(p1, p2):
    return np.linalg.norm(p1 - p2)

# 2. Manhattan Distance
def manhattan_distance(p1, p2):
    return np.sum(np.abs(p1 - p2))

# 3. Hamming Distance (for sequences of equal length)
def hamming_distance(s1, s2):
    # Make sure the inputs are of the same length
    assert len(s1) == len(s2), "Sequences must be of equal length"
    return sum(ch1 != ch2 for ch1, ch2 in zip(s1, s2))

# Calculate distances
euc_dist = euclidean_distance(point1, point2)
man_dist = manhattan_distance(point1, point2)

# Example for hamming distance
string1 = "1011101"
string2 = "1001001"
ham_dist = hamming_distance(string1, string2)

print(f"Point 1: {point1}, Point 2: {point2}")
print(f"Euclidean distance: {euc_dist:.2f}")
print(f"Manhattan distance: {man_dist}")
print(f"Hamming distance between {string1} and {string2}: {ham_dist}")

# Visualization
def plot_distances():
    fig, ax = plt.subplots(figsize=(10, 8))
    
    # Plot points
    ax.scatter(point1[0], point1[1], color='blue', s=100, label='Point 1')
    ax.scatter(point2[0], point2[1], color='red', s=100, label='Point 2')
    
    # Euclidean distance line
    ax.plot([point1[0], point2[0]], [point1[1], point2[1]], 'g-', linewidth=2, label='Euclidean')
    
    # Manhattan distance path
    ax.plot([point1[0], point2[0]], [point1[1], point1[1]], 'r--', linewidth=2)
    ax.plot([point2[0], point2[0]], [point1[1], point2[1]], 'r--', linewidth=2)
    ax.plot([point1[0], point2[0], point2[0]], [point1[1], point1[1], point2[1]], 'y-', linewidth=2, label='Manhattan')
    
    ax.set_xlim(0, 5)
    ax.set_ylim(0, 7)
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.grid(True)
    ax.legend()
    ax.set_title('Distance Metrics Visualization')
    
    # Display the plot
    # plt.show()
    # Note: In a real environment, use plt.show() to display the plot

plot_distances()
