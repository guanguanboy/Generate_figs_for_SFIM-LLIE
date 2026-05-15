import os
from PIL import Image

def resize_images(input_dir, output_dir, target_size=(600, 400)):
    # 如果输出文件夹不存在，则创建
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        print(f"创建输出目录: {output_dir}")

    # 支持的图片格式
    valid_extensions = ('.jpg', '.jpeg', '.png', '.bmp', '.webp', '.tiff')

    # 遍历文件夹
    for filename in os.listdir(input_dir):
        if filename.lower().endswith(valid_extensions):
            img_path = os.path.join(input_dir, filename)
            
            try:
                with Image.open(img_path) as img:
                    # 使用 Image.Resampling.LANCZOS 获得高质量的缩放效果
                    resized_img = img.resize(target_size, Image.Resampling.LANCZOS)
                    
                    # 保存到输出目录
                    save_path = os.path.join(output_dir, filename)
                    resized_img.save(save_path)
                    
                    print(f"已处理: {filename} -> {target_size}")
            except Exception as e:
                print(f"处理文件 {filename} 时出错: {e}")

if __name__ == "__main__":
    # --- 请在此处修改你的路径 ---
    input_folder = 'images/SID'   # 源图片文件夹
    output_folder = 'images/SID-resized' # 处理后的存放文件夹
    
    resize_images(input_folder, output_folder)
    print("\n所有图片处理完成！")