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

def save_images(image_floder_name, image_name,location1=[],location2=[]):

    output_father_foloder_path = os.path.join('images', image_floder_name + '_output')
    if not os.path.exists(output_father_foloder_path):
        os.mkdir(output_father_foloder_path)
    output_image_folder_name = os.path.join(image_floder_name + '_output', image_name)

    output_folder_path = os.path.join('images', output_image_folder_name)
    if not os.path.exists(output_folder_path):
        os.mkdir(output_folder_path)

    # 打开图片
    origin_img_path = os.path.join('images', image_floder_name, image_name +'.png')
    origin_img = Image.open(origin_img_path)

    img = origin_img


    #绘制红色框并crop其中的内容 
    Image_width = 32
    Image_height = 16
    x1 = location1[0]
    x2 = x1+Image_width
    y1 = location1[1]
    y2 = y1+Image_height

    bbox = (x1, y1, x2, y2)

    # 截取矩形区域
    cropped_img_red = origin_img.crop(bbox)
    # 保存截取后的图片
    cropped_img_red.save(output_folder_path + '/'  + image_name + '_cropped_red.png')
    #cropped_img.save('images/2015_02485_cropped.jpg')


    #给截图后的图片上添加red边框并保存
    # 定义边框宽度和颜色
    border_width = 1
    border_color = (255, 0, 0)  # 红色 RGB 值

    # 添加边框
    cropped_img_red_with_border = ImageOps.expand(cropped_img_red, border=border_width, fill=border_color)
    cropped_img_red_with_border.save(output_folder_path + '/'  + image_name + '_cropped_red_with_border.png')

    #在原始图片上绘制红色矩形框并保存
    draw = ImageDraw.Draw(img)

    # 绘制矩形框
    color=(255, 0, 0)
    width=2
    draw.rectangle(bbox, outline=color, width=width)

    # 保存图片
    output_path = output_folder_path + '/'  + image_name +  '_red_rect.png'
    #output_path = 'images/2015_02485_red_rect.jpg'
    img.save(output_path)


    #继续绘制blue框并crop其中的内容 

    #定义矩形区域
    x1 = location2[0]
    x2 = x1+Image_width
    y1 = location2[1]
    y2 = y1+Image_height

    bbox = (x1, y1, x2, y2)
    # 截取矩形区域
    cropped_img_blue = origin_img.crop(bbox)


    # 保存截取后的图片
    cropped_img_blue.save(output_folder_path + '/'  + image_name + '_cropped_blue.png')
    #cropped_img.save('images/2015_02485_cropped.jpg')

    #给截图后的图片上添加red边框并保存
    # 定义边框宽度和颜色
    border_width = 1
    border_color = (0, 0, 255)  # 红色 RGB 值

    # 添加边框
    cropped_img_blue_with_border = ImageOps.expand(cropped_img_blue, border=border_width, fill=border_color)
    cropped_img_blue_with_border.save(output_folder_path + '/'  + image_name + '_cropped_blue_with_border.png')

    #在原始图片上绘制红色矩形框并保存
    draw = ImageDraw.Draw(img)

    # 绘制矩形框
    blue_color=(0, 0, 256)
    width=2
    draw.rectangle(bbox, outline=blue_color, width=width)

    # 保存图片
    output_path = output_folder_path + '/'  + image_name +  '_full_rect.png'
    #output_path = 'images/2015_02485_red_rect.jpg'
    img.save(output_path)


    scale_value = 3
    cropped_img_red_with_border_resized = cropped_img_red_with_border.resize((cropped_img_red_with_border.width*scale_value, cropped_img_red_with_border.height*scale_value))
    cropped_img_red_with_border_width = cropped_img_red_with_border_resized.width
    cropped_img_red_with_border_height = cropped_img_red_with_border_resized.height

    cropped_img_blue_with_border_resized = cropped_img_blue_with_border.resize((cropped_img_blue_with_border.width*scale_value, cropped_img_blue_with_border.height*scale_value))
    cropped_img_blue_with_border_width = cropped_img_blue_with_border_resized.width
    cropped_img_blue_with_border_height = cropped_img_blue_with_border_resized.height

    big_img_width = img.width
    big_img_height = img.height

    # 将小图1粘贴到大图的左下角
    img.paste(cropped_img_red_with_border_resized, (0, big_img_height - cropped_img_red_with_border_height))

    # 将小图2粘贴到大图的右下角
    img.paste(cropped_img_blue_with_border_resized, (big_img_width - cropped_img_blue_with_border_width, big_img_height - cropped_img_blue_with_border_height))

    # 保存合并后的图片
    output_path = output_folder_path + '/'  + image_name +  '_final.png'

    img.save(output_path)


# 示例
"""
image_path = "input.jpg"  # 输入图片路径
output_path = "output.jpg"  # 输出图片路径
bbox = (50, 50, 150, 150)  # 矩形框左上角和右下角坐标 (x1, y1, x2, y2)


draw_rectangle(image_path, output_path, bbox)
"""
image_floder_name = 'LOLv2-real'

image_floder_path = os.path.join('images', image_floder_name)
# 遍历文件夹中的所有文件名
file_names = []
for root, dirs, files in os.walk(image_floder_path):
    for file in files:
        file_names.append(file)

for image_name in file_names:
    #save_images(image_floder_name, image_name[:-4], location1 = [50,120], location2=[190,50])
    #save_images(image_floder_name, image_name[:-4], location1 = [50,90], location2=[200,120])

    save_images(image_floder_name, image_name[:-4], location1 = [4,105], location2=[116,160])
