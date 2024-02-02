import math
import colorsys

from colormath import color_objects
from colormath import color_conversions


def hsl2rgb(hsl_color):
    return [round(i * 255) for i in colorsys.hls_to_rgb(hsl_color.hsl_h, hsl_color.hsl_l, hsl_color.hsl_s)]


blenderd_listA = []
blenderd_listB = []


for i in range(12):
    my_hsl_color = color_objects.HSLColor(i * 30.0 + 15, 1.0, 0.5)
    my_lab_color = color_conversions.convert_color(my_hsl_color,color_objects.LabColor)
    my_lab_color.lab_l = 40
    my_hsl_color = color_conversions.convert_color(my_lab_color, color_objects.HSLColor)     
        
    #print(my_hsl_color)

    my_hsl_color.hsl_h = my_hsl_color.hsl_h / 360.0        
    my_rgb_color = hsl2rgb(my_hsl_color)        
    #print(my_rgb_color)
    blenderd_listA.append(my_rgb_color)


for i in range(12):
    my_lab_color = color_objects.LabColor(
        40,
        math.cos(math.pi * i / 6.0) * 100,
        math.sin(math.pi * i / 6.0) * 100        
        )

    #print(my_lab_color)

    my_hsl_color = color_conversions.convert_color(my_lab_color, color_objects.HSLColor)        
        
    #print(my_hsl_color)

    my_hsl_color.hsl_h = my_hsl_color.hsl_h / 360.0
    
    my_rgb_color = hsl2rgb(my_hsl_color)


    #print(my_rgb_color)

    blenderd_listB.append(my_rgb_color)

    pass



for i in range(12):
    r = blenderd_listA[i][0] + blenderd_listB[i][0]
    g = blenderd_listA[i][1] + blenderd_listB[i][1]
    b = blenderd_listA[i][2] + blenderd_listB[i][2]
    new_rgb = [r//2, g//2, b//2]
    print(new_rgb)
