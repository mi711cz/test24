import os
import shutil

def organize_files(input_dir, output_dir):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    for filename in os.listdir(input_dir):
        if filename.endswith(".xml") and "-nfe" in filename:
            subdir_name = filename[:44]  # Ersten 44 Zeichen des Dateinamens
            subdir_path = os.path.join(output_dir, subdir_name)
            
            if not os.path.exists(subdir_path):
                os.makedirs(subdir_path)
            
            src_path = os.path.join(input_dir, filename)
            dest_path = os.path.join(subdir_path, filename)
            
            shutil.move(src_path, dest_path)
            print(f"Moved: {filename} -> {subdir_path}")

# Beispielaufruf
input_directory = "/home/mczochar/server/test_data/pnf"  # Ersetze mit dem tatsächlichen Pfad
output_directory = "/home/mczochar/server/test_data/pnf_output"  # Ersetze mit dem tatsächlichen Pfad

organize_files(input_directory, output_directory)