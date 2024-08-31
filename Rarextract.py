import patoolib
import os
import py7zr

def extract_rar_with_password(rar_file, extract_dir, password):
    try:
        patoolib.extract_archive(rar_file, outdir=extract_dir, password=password)
        print("Extraction successful.")
    except Exception as e:
        print("Error:", e)

def create_rar_with_password(input_dir, rar_file, password):
    try:
        with py7zr.SevenZipFile(rar_file, 'w', password=password) as rf:
            for root, dirs, files in os.walk(input_dir):
                for file in files:
                    rf.write(os.path.join(root, file), os.path.relpath(os.path.join(root, file), os.path.join(input_dir, '..')))
        print("RAR creation successful.")
    except Exception as e:
        print("Error:", e)

# Path to the RAR file you want to extract
rar_file_to_extract = r"D:\Files\Something.rar"

# Directory to extract the contents of the RAR file
extract_directory = r"C:\Users\Someone\Desktop\sth"

# Password for the RAR file
rar_password = "password"

# Extract the RAR file
extract_rar_with_password(rar_file_to_extract, extract_directory, rar_password)

# Path to the directory containing files to be RARed
input_directory_to_rar = r"C:\Users\someone\Desktop\sth\xxx"

# Path for the new RAR file
new_rar_file = r"C:\Users\someone\Desktop\test1.rar"

# New password for the new RAR file
new_rar_password = "123456"

# Create a new RAR file with a new password
create_rar_with_password(input_directory_to_rar, new_rar_file, new_rar_password)
