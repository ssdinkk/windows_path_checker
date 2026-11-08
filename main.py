from business.validator import validate_path
from business.search_service import find_paths
from data.file_reader import read_file
from data.web_reader import read_web_page


def main():
    while True:
        print("\n===== WINDOWS PATH CHECKER =====")
        print("1. Проверить Windows-путь")
        print("2. Найти пути в текстовом файле")
        print("3. Найти пути на веб-странице")
        print("4. Выйти")

        choice = input("\nВыберите действие: ")

        if choice == "1":
            path = input("Введите Windows-путь: ")

            if validate_path(path):
                print("Путь синтаксически корректен.")
            else:
                print("Путь синтаксически некорректен.")

        elif choice == "2":
            file_path = input("Введите путь к текстовому файлу: ")
            text = read_file(file_path)

            if text:
                found_paths = find_paths(text)
                print("\nНайденные пути:")

                for path in found_paths:
                    print(path)

                print(f"Всего найдено: {len(found_paths)}")

        elif choice == "3":
            url = input("Введите URL веб-страницы: ")
            text = read_web_page(url)

            if text:
                found_paths = find_paths(text)
                print("\nНайденные пути:")

                for path in found_paths:
                    print(path)

                print(f"Всего найдено: {len(found_paths)}")

        elif choice == "4":
            print("Завершение программы.")
            break

        else:
            print("Неверный выбор. Попробуйте ещё раз.")


if __name__ == "__main__":
    main()