# Windows Path Checker

## Описание проекта

Windows Path Checker — программа для проверки синтаксической корректности полных путей к файлам в операционной системе Windows, а также поиска таких путей в текстовых файлах и на веб-страницах.

## Возможности

- Проверка корректности Windows-путей.
- Поддержка абсолютных путей с диском (например, `C:\Users\Diana\file.txt`).
- Поддержка сетевых UNC-путей (например, `\\Server\Shared\file.txt`).
- Поиск путей в произвольном тексте.
- Чтение текстовых файлов.
- Загрузка содержимого веб-страниц.
- Консольный интерфейс с меню.
- Автоматическое тестирование с помощью pytest.

## Структура проекта

```text
windows_path_checker/
├── business/
│   ├── __init__.py
│   ├── validator.py
│   └── search_service.py
├── data/
│   ├── file_reader.py
│   ├── web_reader.py
│   └── example.txt
├── tests/
│   ├── test_validator.py
│   ├── test_search_service.py
│   ├── test_file_reader.py
│   └── test_web_reader.py
├── main.py
├── requirements.txt
└── README.md
```

## Установка и запуск

1. Клонировать репозиторий:

```bash
git clone https://github.com/ssdinkk/windows_path_checker.git
```

2. Перейти в папку проекта:

```bash
cd windows_path_checker
```

3. Установить зависимости:

```bash
pip install -r requirements.txt
```

4. Запустить программу:

```bash
python main.py
```

## Запуск тестов

Для запуска автоматических тестов выполните:

```bash
python -m pytest -v
```

## Используемые технологии

- Python 3.13
- Regular Expressions (re)
- pathlib
- requests
- pytest

## Автор Диана Самаева ИДБ-25-11

Учебный проект. Вариант 19.
