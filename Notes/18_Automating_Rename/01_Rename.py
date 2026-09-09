import os

target_folder = 'D:/02_Deep Python/18_Automating_Rename/Lectures'

def rename():
    for filename in os.listdir(target_folder):
        file_n, file_ext = os.path.splitext(filename)

        lec_name, lec_type, lec_num = file_n.split('-')

        lec_type = lec_type.strip()

        lec_num = lec_num.strip()

        lec_num = lec_num[1:]

        lec_num = lec_num.zfill(2) # 1 ---> 01

        new_name = f"{lec_num} - {lec_name}- {lec_type}{file_ext}"

        old_path = os.path.join(target_folder, filename)
        new_path = os.path.join(target_folder, new_name)
        os.rename(old_path, new_path)

rename()

