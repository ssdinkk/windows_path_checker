from data.file_reader import read_file
from business.search_service import find_paths


file_path = "data/example.txt"

text = read_file(file_path)

if text:
    print("Содержимое файла:")
    print(text)

    found_paths = find_paths(text)

    print("Найденные пути:")
    for path in found_paths:
        print(path)

    print(f"\nВсего найдено: {len(found_paths)}")