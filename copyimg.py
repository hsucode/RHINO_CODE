import os
import shutil
from PIL import Image

def is_image(file_path):
    try:
        with Image.open(file_path) as img:
            return True
    except IOError:
        return False

def copy_images_to_d_drive(src_dir, dest_folder):
    if not os.path.exists(dest_folder):
        os.makedirs(dest_folder)

    for root, dirs, files in os.walk(src_dir):
        for file in files:
            file_path = os.path.join(root, file)
            if is_image(file_path):
                shutil.copy(file_path, dest_folder)

# src_dir = "C:\\Users\\username\\Documents" # 替换为要遍历的目录路径
# dest_folder = "D:\\images" # 替换为要将图片复制到的目标文件夹路径
# copy_images_to_d_drive(src_dir, dest_folder)


if( __name__ == "__main__" ):
    src_dir = 'F:\\wallpaper\\BingWallpaper\\BingImage'
    dest_folder = 'C:\\Users\\user\\Pictures\\wallpaper'
    copy_images_to_d_drive(src_dir, dest_folder)