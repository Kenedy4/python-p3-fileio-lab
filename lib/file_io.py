# lib/file_io.py

def write_file(file_name, file_content):
    # Ensure the file name has the .txt extension
    file_name = f"{file_name}.txt"
    # Open the file in write mode ('w') and write the content
    with open(file_name, 'w') as file:
        file.write(file_content)

def append_file(file_name, append_content):
    # Ensure the file name has the .txt extension
    file_name = f"{file_name}.txt"
    # Open the file in append mode ('a') and append the content
    with open(file_name, 'a') as file:
        file.write(append_content)

def read_file(file_name):
    # Ensure the file name has the .txt extension
    file_name = f"{file_name}.txt"
    # Open the file in read mode ('r') and read the content
    with open(file_name, 'r') as file:
        content = file.read()
    return content
