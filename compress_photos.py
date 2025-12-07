from PIL import Image
import os, sys

if __name__ == "__main__":
    # 配置参数
    input_dir = sys.argv[1] if len(sys.argv) > 1 else "photos"
    output_dir = sys.argv[2] if len(sys.argv) > 2 else "compressed"
    quality = int(sys.argv[3]) if len(sys.argv) > 3 else 80
    max_size = int(sys.argv[4]) if len(sys.argv) > 4 else 1200
    
    # 创建输出文件夹
    os.makedirs(output_dir, exist_ok=True)
    
    # 处理图片
    for f in os.listdir(input_dir):
        if f.lower().endswith(('.jpg', '.jpeg', '.png', '.bmp', '.webp', '.heic')):
            try:
                img = Image.open(os.path.join(input_dir, f))
                img.thumbnail((max_size, max_size))
                out_name = f"{os.path.splitext(f)[0]}.jpg"
                img.save(os.path.join(output_dir, out_name), "JPEG", quality=quality)
                print(f"✓ {f}")
            except:
                pass