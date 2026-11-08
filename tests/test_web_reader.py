import requests
from unittest.mock import patch, Mock

from data.web_reader import read_web_page


def test_read_web_page():
    mock_response = Mock()
    mock_response.text = "<html>Hello!</html>"
    mock_response.apparent_encoding = "utf-8"
    mock_response.raise_for_status.return_value = None

    with patch("data.web_reader.requests.get", return_value=mock_response):
        result = read_web_page("https://example.com")

    assert result == "<html>Hello!</html>"


def test_read_web_page_error():
    with patch(
        "data.web_reader.requests.get",
            side_effect=requests.exceptions.ConnectionError("Connection error")
    ):
        result = read_web_page("https://example.com")

    assert result == ""