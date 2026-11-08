from business.search_service import find_paths


def test_find_paths():
    text = """
    Проект: C:\\Users\\Diana\\Projects\\Python.
    Документ: D:\\Documents\\report.txt.
    Обычный текст без пути.
    """

    result = find_paths(text)

    assert result == [
        r"C:\Users\Diana\Projects\Python",
        r"D:\Documents\report.txt"
    ]


def test_find_no_paths():
    text = "Здесь нет Windows-путей."

    result = find_paths(text)

    assert result == []


def test_find_paths_with_empty_text():
    assert find_paths("") == []