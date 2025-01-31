import os
import shutil
import zipfile
from collections import defaultdict

def organize_files(input_dir, output_dir):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    file_groups = defaultdict(list)
    
    for filename in os.listdir(input_dir):
        if filename.endswith(".xml") and "-nfe" in filename:
            subdir_name = filename[:44]  # Ersten 44 Zeichen des Dateinamens
            file_groups[subdir_name].append(filename)
    
    for subdir_name, files in file_groups.items():
        subdir_path = os.path.join(output_dir, subdir_name)
        if not os.path.exists(subdir_path):
            os.makedirs(subdir_path)
        
        for filename in files:
            src_path = os.path.join(input_dir, filename)
            dest_path = os.path.join(subdir_path, filename)
            shutil.move(src_path, dest_path)
            print(f"Moved: {filename} -> {subdir_path}")
        
        # Erstelle eine ZIP-Datei für die Gruppe
        zip_path = os.path.join(output_dir, f"{subdir_name}.zip")
        with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
            for filename in files:
                file_path = os.path.join(subdir_path, filename)
                zipf.write(file_path, filename)
        
        # Lösche das Verzeichnis nach dem Zippen
        shutil.rmtree(subdir_path)
        print(f"Created ZIP: {zip_path}")

# Beispielaufruf
input_directory = "/home/mczochar/server/test_data/pnf/Inbound_NF-es_Nov_01_2024"  # Ersetze mit dem tatsächlichen Pfad
output_directory = "/home/mczochar/server/test_data/pnf_output_zip"  # Ersetze mit dem tatsächlichen Pfad

organize_files(input_directory, output_directory)
