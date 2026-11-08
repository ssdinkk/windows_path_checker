import pytest

from business.validator import validate_path


@pytest.mark.parametrize("path", [
    r"C:\Users\Diana\Documents\report.txt",
    r"D:\Projects\Python\main.py",
    r"\\Server\Shared\file.docx",
])

def test_valid_paths(path):
    assert validate_path(path) is True


@pytest.mark.parametrize("path", [
    "Documents\\file.txt",
    r"C:\Folder\fi*le.txt",
    r"C:\Folder.\file.txt",
    "",
])

def test_invalid_paths(path):
    assert validate_path(path) is False