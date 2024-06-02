# !pip3 install pillow
# !pip3 install webcolors

from PIL import Image
import numpy as np
from collections import Counter
import webcolors

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

def closest_color(requested_color):
    min_colors = {}
    for key, name in webcolors.CSS3_HEX_TO_NAMES.items():
        r_c, g_c, b_c = webcolors.hex_to_rgb(key)
        rd = (r_c - requested_color[0]) ** 2
        gd = (g_c - requested_color[1]) ** 2
        bd = (b_c - requested_color[2]) ** 2
        min_colors[(rd + gd + bd)] = name
    return min_colors[min(min_colors.keys())]

def get_color_name(requested_color):
    try:
        color_name = webcolors.rgb_to_name(requested_color)
    except ValueError:
        color_name = closest_color(requested_color)
    return color_name

def classify_top_colors(image_path, top_n=5):
    top_colors = get_top_colors(image_path, top_n)
    classified_colors = [(color, count, get_color_name(color)) for color, count in top_colors]
    
    return classified_colors


image_path = 'images/red_image.jpg'
classified_colors = classify_top_colors(image_path)
print("Top colors classified (in order of occurrence):")
for color, count, classification in classified_colors:
    print(f"Color: {color}, Count: {count}, Classified as: {classification}")


print()
print("Final result: " + classified_colors[0][2])