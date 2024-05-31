# first !pip install pillow

from PIL import Image
import numpy as np
from collections import Counter

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

image_path = 'images/ubcor.png'
top_colors = get_top_colors(image_path)
print("Top 5 most appearing colors (in RGB):")
for color, count in top_colors:
    print(f"Color: {color}, Count: {count}")