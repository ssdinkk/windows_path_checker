
from business.validator import validate_path


paths = [
    r"C:\Users\Diana\Documents\report.txt",
    r"D:\Projects\Python\main.py",
    r"\\Server\Shared\file.docx",
    r"Documents\file.txt",
    r"C:\Folder\fi*le.txt",
    r"C:\Folder.\file.txt"
]

for path in paths:
    print(f"{path} -> {validate_path(path)}")
