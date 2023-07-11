import os
import shutil

# Folder paths
data_dir = 'data'
with_mask_dir = os.path.join(data_dir, 'with_mask')
without_mask_dir = os.path.join(data_dir, 'without_mask')

# Move images from with_mask sub-folder
for filename in os.listdir(with_mask_dir):
    src = os.path.join(with_mask_dir, filename)
    dst = os.path.join(data_dir, filename)
    shutil.move(src, dst)

# Move images from without_mask sub-folder
for filename in os.listdir(without_mask_dir):
    src = os.path.join(without_mask_dir, filename)
    dst = os.path.join(data_dir, filename)
    shutil.move(src, dst)