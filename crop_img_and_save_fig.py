from PIL import Image

from PIL import Image, ImageDraw
import os

def draw_rectangle(image, output_path, bbox, color=(255, 0, 0), width=3):    
    # 创建ImageDraw对象
    draw = ImageDraw.Draw(image)
    
    # 绘制矩形框
    draw.rectangle(bbox, outline=color, width=width)
    
    # 保存图片
    image.save(output_path)

# 示例
"""
image_path = "input.jpg"  # 输入图片路径
output_path = "output.jpg"  # 输出图片路径
bbox = (50, 50, 150, 150)  # 矩形框左上角和右下角坐标 (x1, y1, x2, y2)


draw_rectangle(image_path, output_path, bbox)
"""
image_floder_name = 'SID'
image_name = '10106_05_0.1s_Input'
#image_name = 'DoveNet_2020_09_30_22_36_08_133_degraded_comp_full_2_1_1'
#image_name = 'D-HT_Out_2020_09_30_22_36_08_133_degraded_comp_full_1_1'
#image_name = 'H-CDM_2020_09_30_22_36_08_133_degraded_comp_full_2_1_1_harmonized'

# 打开图片
#img = Image.open('images/Out_2015_02682_degraded_comp_1_1.jpg') #In_2015_02485_degraded_comp_new_new_1_1
img = Image.open('images/' + image_floder_name + '/' + image_name +'.png')
# 定义矩形区域
"""
x1 = 140
x2 = x1+600
y1 = 240
y2 = y1+360
"""

x1 = 10
x2 = x1+80
y1 = 10
y2 = y1+80

bbox = (x1, y1, x2, y2)
# 截取矩形区域
cropped_img = img.crop(bbox)

output_image_folder_name = 'SID_output'

output_folder_path = os.path.join('images', output_image_folder_name)

if not os.path.exists(output_folder_path):
    os.mkdir(output_folder_path)


# 保存截取后的图片
cropped_img.save(output_folder_path + '/'  + image_name + '_cropped.png')
#cropped_img.save('images/2015_02485_cropped.jpg')

#在原始图片上绘制红色矩形框并保存
draw = ImageDraw.Draw(img)

# 绘制矩形框
color=(255, 0, 0)
width=4
draw.rectangle(bbox, outline=color, width=width)

# 保存图片
output_path = output_folder_path + '/'  + image_name +  '_red_rect.png'
#output_path = 'images/2015_02485_red_rect.jpg'
img.save(output_path)
