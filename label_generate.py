import os
import csv

# Directory path
data_dir = 'data'

# Sub-folder names
sub_folders = ['with_mask', 'without_mask']

# CSV file path
csv_file = 'dataset/data_labels.csv'

# Create a CSV file and write the header
with open(csv_file, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['filename', 'label'])

    # Iterate over the sub-folders
    for sub_folder in sub_folders:
        folder_path = os.path.join(data_dir, sub_folder)
        if sub_folder == 'with_mask':
            label = 1
        
        elif sub_folder == 'without_mask':
            label = 0

        # Iterate over the files in the sub-folder
        for filename in os.listdir(folder_path):
            file_path = os.path.join(folder_path, filename)
            writer.writerow([filename, label])
