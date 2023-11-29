import math
import numpy as np
import time

color_list = [
    (240, 240, 240),
    (242, 178, 51),
    (229, 127, 216),
    (153, 178, 242),
    (222, 222, 108),
    (127, 204, 25),
    (242, 178, 204),
    (76, 76, 76),
    (153, 153, 153),
    (76, 153, 178),
    (178, 102, 229),
    (51, 102, 204),
    (127, 102, 76),
    (87, 166, 78),
    (204, 76, 76),
    (17, 17, 17),
]
color_array = np.array(color_list)


def get_closest_color(given_rgb):
    min_distance = float("inf")
    closest_color = None
    for color_id in range(len(color_list)):
        distance = math.sqrt(
            sum((c - g) ** 2 for c, g in zip(color_list[color_id], given_rgb))
        )
        if distance < min_distance:
            min_distance = distance
            closest_color = color_id
    return closest_color


def get_closest_color_np(given_rgb):
    distances = np.sqrt(np.sum((color_array - given_rgb) ** 2, axis=1))
    return np.argmin(distances)


start = time.time()
for r in range(255):
    for g in range(255):
        for b in range(10):
            get_closest_color((r, g, b))
print(time.time() - start)

start = time.time()
for r in range(255):
    for g in range(255):
        for b in range(10):
            get_closest_color_np(np.array([r, g, b]))
print(time.time() - start)
