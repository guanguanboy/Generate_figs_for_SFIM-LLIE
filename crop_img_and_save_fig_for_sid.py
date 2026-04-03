from PIL import Image

from PIL import Image, ImageDraw,ImageOps
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
#image_name = '10106_05_0.1s_Input'
#image_name = '10106_05_0.1s_GT'
#image_name = '10106_05_0.1s_MIRNet'
image_name = '10106_05_0.1s_SNR_aware'
#image_name = '10106_05_0.1s_SMG_LLIE'
#image_name = '10106_05_0.1s_ours'

output_image_folder_name = 'SID_output' + '/' + image_name

output_folder_path = os.path.join('images', output_image_folder_name)
if not os.path.exists(output_folder_path):
    os.mkdir(output_folder_path)

# 打开图片
#img = Image.open('images/Out_2015_02682_degraded_comp_1_1.jpg') #In_2015_02485_degraded_comp_new_new_1_1
origin_img = Image.open('images/' + image_floder_name + '/' + image_name +'.png')

img = origin_img


#绘制红色框并crop其中的内容 
Image_width = 32

x1 = 10
x2 = x1+Image_width
y1 = 10
y2 = y1+Image_width

bbox = (x1, y1, x2, y2)

# 截取矩形区域
cropped_img = origin_img.crop(bbox)
# 保存截取后的图片
cropped_img.save(output_folder_path + '/'  + image_name + '_cropped_red.png')
#cropped_img.save('images/2015_02485_cropped.jpg')


#给截图后的图片上添加red边框并保存
# 定义边框宽度和颜色
border_width = 2
border_color = (255, 0, 0)  # 红色 RGB 值

# 添加边框
image_with_border = ImageOps.expand(cropped_img, border=border_width, fill=border_color)
image_with_border.save(output_folder_path + '/'  + image_name + '_cropped_red_with_border.png')

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


#继续绘制blue框并crop其中的内容 

#定义矩形区域
x1 = 128
x2 = x1+Image_width
y1 = 128
y2 = y1+Image_width

bbox = (x1, y1, x2, y2)
# 截取矩形区域
cropped_img = origin_img.crop(bbox)


# 保存截取后的图片
cropped_img.save(output_folder_path + '/'  + image_name + '_cropped_blue.png')
#cropped_img.save('images/2015_02485_cropped.jpg')

#给截图后的图片上添加red边框并保存
# 定义边框宽度和颜色
border_width = 2
border_color = (0, 0, 255)  # 红色 RGB 值

# 添加边框
image_with_border = ImageOps.expand(cropped_img, border=border_width, fill=border_color)
image_with_border.save(output_folder_path + '/'  + image_name + '_cropped_blue_with_border.png')

#在原始图片上绘制红色矩形框并保存
draw = ImageDraw.Draw(img)

# 绘制矩形框
blue_color=(0, 0, 256)
width=4
draw.rectangle(bbox, outline=blue_color, width=width)

# 保存图片
output_path = output_folder_path + '/'  + image_name +  '_full_rect.png'
#output_path = 'images/2015_02485_red_rect.jpg'
img.save(output_path)

