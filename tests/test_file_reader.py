from data.file_reader import read_file


def test_read_file(tmp_path):
    test_file = tmp_path / "example.txt"
    test_file.write_text("Hello, Windows!", encoding="utf-8")

    result = read_file(str(test_file))

    assert result == "Hello, Windows!"


def test_read_nonexistent_file():
    result = read_file("nonexistent_file.txt")

    assert result == ""