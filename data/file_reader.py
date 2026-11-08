from pathlib import Path


def read_file(file_path: str) -> str:
    """
    Читает текстовый файл и возвращает его содержимое.
    """
    path = Path(file_path)

    try:
        return path.read_text(encoding="utf-8")
    except FileNotFoundError:
        print(f"Ошибка: файл не найден — {file_path}")
    except PermissionError:
        print(f"Ошибка: нет доступа к файлу — {file_path}")
    except UnicodeDecodeError:
        print(f"Ошибка: не удалось прочитать файл в кодировке UTF-8 — {file_path}")
    except OSError as error:
        print(f"Ошибка чтения файла: {error}")

    return ""