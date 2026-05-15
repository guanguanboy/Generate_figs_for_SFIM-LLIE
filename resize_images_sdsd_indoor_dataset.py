import os
from PIL import Image

def resize_images_recursive(input_root, output_root, target_size=(960, 512)):
    # 支持的图片格式
    valid_extensions = ('.jpg', '.jpeg', '.png', '.bmp', '.webp', '.tiff')

    # 使用 os.walk 遍历所有子目录
    for root, dirs, files in os.walk(input_root):
        # 计算当前处理的目录相对于输入根目录的路径
        relative_path = os.path.relpath(root, input_root)
        
        # 构建对应的输出目录路径
        target_dir = os.path.join(output_root, relative_path)

        # 遍历当前目录下的文件
        for filename in files:
            if filename.lower().endswith(valid_extensions):
                # 确保输出子目录存在，如果不存在则创建
                if not os.path.exists(target_dir):
                    os.makedirs(target_dir)
                    print(f"创建目录: {target_dir}")

                img_path = os.path.join(root, filename)
                save_path = os.path.join(target_dir, filename)
                
                try:
                    with Image.open(img_path) as img:
                        # 使用 LANCZOS 获得高质量缩放
                        resized_img = img.resize(target_size, Image.Resampling.LANCZOS)
                        
                        # 保存图片
                        resized_img.save(save_path)
                        print(f"已处理: {os.path.join(relative_path, filename)} -> {target_size}")
                except Exception as e:
                    print(f"处理文件 {filename} 时出错: {e}")

if __name__ == "__main__":
    # --- 路径配置 ---
    # 源根目录
    input_folder = 'D:/Datasets/sdsd_png/sdsd_png/outdoor_static_png/GT'
    # 目标根目录
    output_folder = 'D:/Datasets/sdsd_png/sdsd_png/outdoor_static_png-resized/GT'
    
    print("开始递归处理图片...")
    resize_images_recursive(input_folder, output_folder)
    print("\n所有图片及子文件夹处理完成！")