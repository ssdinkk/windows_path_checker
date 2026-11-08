from data.web_reader import read_web_page
from business.search_service import find_paths


url = "https://example.com"

text = read_web_page(url)

if text:
    print("Страница успешно загружена!")
    print(f"Получено символов: {len(text)}")

    found_paths = find_paths(text)

    print("\nНайденные Windows-пути:")
    for path in found_paths:
        print(path)

    print(f"\nВсего найдено: {len(found_paths)}")