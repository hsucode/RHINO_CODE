
import os

def merge_txt_files(folder_path, output_file):
    with open(output_file, 'w', encoding='utf-8') as outfile:
        for root, dirs, files in os.walk(folder_path):
            for file in files:
                if file.endswith('.vb'):
                    file_path = os.path.join(root, file)
                    with open(file_path, 'r', encoding='utf-8') as infile:
                        content = infile.read()
                        outfile.write(content)
                        outfile.write('')

folder_path = 'G:\CODE\CATIA-AUTOMATION-CODE\V5_DoNet\新建文件夹'
output_file = '合并后的文件名.txt'
merge_txt_files(folder_path, output_file)
