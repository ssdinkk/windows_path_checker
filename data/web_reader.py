import requests


def read_web_page(url: str) -> str:
    """
    Загружает веб-страницу и возвращает её текст.
    """
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()

        response.encoding = response.apparent_encoding

        return response.text

    except requests.exceptions.RequestException as error:
        print(f"Ошибка загрузки страницы: {error}")
        return ""