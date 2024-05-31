import os
import shutil

def remove_pycache_folders(root_dir):
    for dirpath, dirnames, filenames in os.walk(root_dir):
        if '__pycache__' in dirnames:
            pycache_path = os.path.join(dirpath, '__pycache__')
            print(f'Siliniyor: {pycache_path}')
            shutil.rmtree(pycache_path)

# Proje klasörünün yolunu buraya yazın
project_directory = 'C:/Users/PC_5185/Desktop/private-gpt_GPU/private-gpt'
remove_pycache_folders(project_directory)
