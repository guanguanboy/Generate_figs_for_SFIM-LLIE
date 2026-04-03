from PIL import Image

from PIL import Image, ImageDraw,ImageOps
import os

def save_images(image_floder_name, image_name, location1=[], location2=[]):
    # --- 1. 路径准备 ---
    output_father_foloder_path = os.path.join('images', image_floder_name + '_output')
    if not os.path.exists(output_father_foloder_path):
        os.makedirs(output_father_foloder_path) # 使用 makedirs 更安全
        
    output_folder_path = os.path.join(output_father_foloder_path, image_name)
    if not os.path.exists(output_folder_path):
        os.makedirs(output_folder_path)

    # 打开图片
    origin_img_path = os.path.join('images', image_floder_name, image_name + '.png')
    img = Image.open(origin_img_path).convert('RGB')
    
    # 定义目标尺寸
    TARGET_SIZE = (292, 128)
    BORDER_WIDTH = 8  # 边框宽度，可根据 256*128 的比例适当加粗
    
    # --- 2. 处理红色区域 (Location 1) ---
    x1, y1 = location1
    # 原始脚本定义：Image_width=32, Image_height=16
    bbox_red = (x1, y1, x1 + 32, y1 + 16)
    
    # Crop -> Resize (256x128)
    cropped_red = img.crop(bbox_red).resize(TARGET_SIZE, Image.Resampling.LANCZOS)
    
    # 添加红色边框并保存
    red_with_border = ImageOps.expand(cropped_red, border=BORDER_WIDTH, fill=(255, 0, 0))
    red_with_border.save(os.path.join(output_folder_path, f"{image_name}_red_256x128.png"))

    # --- 3. 处理蓝色区域 (Location 2) ---
    x2, y2 = location2
    bbox_blue = (x2, y2, x2 + 32, y2 + 16)
    
    # Crop -> Resize (256x128)
    cropped_blue = img.crop(bbox_blue).resize(TARGET_SIZE, Image.Resampling.LANCZOS)
    
    # 添加蓝色边框并保存
    blue_with_border = ImageOps.expand(cropped_blue, border=BORDER_WIDTH, fill=(0, 0, 255))
    blue_with_border.save(os.path.join(output_folder_path, f"{image_name}_blue_256x128.png"))

    # --- 4. 在原图上画框并保存 (可视化对比图) ---
    draw = ImageDraw.Draw(img)
    draw.rectangle(bbox_red, outline=(255, 0, 0), width=2)
    draw.rectangle(bbox_blue, outline=(0, 0, 255), width=2)
    
    # 粘贴放大后的图到原图角落（可选，如果需要 Final 图的话）
    # 这里演示将两个 256x128 的图横向拼接到原图下方或者单独保存
    img.save(os.path.join(output_folder_path, f"{image_name}_full_rect.png"))
    
    print(f"Finished: {image_name}")


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

    save_images(image_floder_name, image_name[:-4], location1 = [32,128], location2=[320,64])
