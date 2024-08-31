# Automat-Compress-Extract
With this Python Script you can Export and then recompress Folders with new password

RAR File Extraction and Creation Script with Password Protection
This Python script allows you to extract and create RAR files with password protection. It leverages the patool library for extracting RAR files and the py7zr library for creating RAR files. The script is designed to handle password-protected RAR files, making it useful for secure file management tasks.

Features
Extract RAR Files with Password: Securely extract the contents of a RAR file using a specified password.
Create RAR Files with Password: Compress files or directories into a RAR archive with password protection.
Prerequisites
Before using the script, ensure that the following Python libraries are installed:

bash
Code kopieren
pip install patool py7zr
Usage
Extracting a RAR File
To extract a password-protected RAR file, use the extract_rar_with_password function. Provide the path to the RAR file, the directory where you want the contents to be extracted, and the password for the RAR file.

python
Code kopieren
# Example usage
rar_file_to_extract = r"D:\path\to\your\file.rar"
extract_directory = r"C:\path\to\extract\directory"
rar_password = "your_password"

extract_rar_with_password(rar_file_to_extract, extract_directory, rar_password)
Creating a Password-Protected RAR File
To create a new RAR file with password protection, use the create_rar_with_password function. Provide the path to the directory or files you want to compress, the desired output path for the RAR file, and the password.

python
Code kopieren
# Example usage
input_directory_to_rar = r"C:\path\to\directory\to\compress"
new_rar_file = r"C:\path\to\output\file.rar"
new_rar_password = "your_new_password"

create_rar_with_password(input_directory_to_rar, new_rar_file, new_rar_password)
Script Breakdown
extract_rar_with_password(rar_file, extract_dir, password): This function extracts a password-protected RAR file to the specified directory.

rar_file: The path to the RAR file.
extract_dir: The directory where the contents will be extracted.
password: The password for the RAR file.
create_rar_with_password(input_dir, rar_file, password): This function creates a password-protected RAR file from a specified directory or set of files.

input_dir: The directory or files to be compressed into the RAR file.
rar_file: The path for the new RAR file.
password: The password to protect the RAR file.
Performance Considerations
Please note that the performance of this script might be influenced by the size of the files being processed, the compression level, and the speed of your system's CPU and disk. If you are processing large files or directories, the script may take some time to complete.

License
This script is open-source and available under the MIT License.
