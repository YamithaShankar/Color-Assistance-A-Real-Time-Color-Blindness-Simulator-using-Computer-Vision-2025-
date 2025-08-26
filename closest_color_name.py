import webcolors
from webcolors import CSS3_NAMES_TO_HEX, hex_to_rgb

def closest_color_name(rgb_tuple):
    try:
        return webcolors.rgb_to_name(rgb_tuple)
    except ValueError:
        min_colors = {}
        for name, hex_code in CSS3_NAMES_TO_HEX.items():
            r_c, g_c, b_c = hex_to_rgb(hex_code)
            rd = (r_c - rgb_tuple[0]) ** 2
            gd = (g_c - rgb_tuple[1]) ** 2
            bd = (b_c - rgb_tuple[2]) ** 2
            min_colors[(rd + gd + bd)] = name
        return min_colors[min(min_colors.keys())]
