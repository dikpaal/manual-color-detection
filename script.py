# first !pip install pillow

from PIL import Image
import numpy as np
from collections import Counter
from scipy.spatial import distance

def image_to_rgb_array(image_path):
    
    with Image.open(image_path) as img:
        img = img.convert('RGB')
        img_array = np.array(img)
    return img_array

def get_top_colors(image_path, top_n=5):
    
    rgb_array = image_to_rgb_array(image_path)
    reshaped_array = rgb_array.reshape(-1, 3)
    color_counts = Counter(map(tuple, reshaped_array))
    top_colors = color_counts.most_common(top_n)
    
    return top_colors

def classify_color(color):
    red = np.array([255, 0, 0])
    blue = np.array([0, 0, 255])
    green = np.array([0, 255, 0])
    
    color = np.array(color)
    distances = {
        'red': distance.euclidean(color, red),
        'blue': distance.euclidean(color, blue),
        'green': distance.euclidean(color, green)
    }
    
    return min(distances, key=distances.get)

def classify_top_colors(image_path, top_n=5):
    top_colors = get_top_colors(image_path, top_n)
    classified_colors = [(color, count, classify_color(color)) for color, count in top_colors]
    
    return classified_colors

image_path = 'images/ubcor.png'
classified_colors = classify_top_colors(image_path)
print("Top colors classified (in order of occurrence):")
for color, count, classification in classified_colors:
    print(f"Color: {color}, Count: {count}, Classified as: {classification}")


print()
print("Final result: " + classified_colors[0][2])
