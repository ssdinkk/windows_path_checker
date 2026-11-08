import re


INVALID_CHARS = r'<>:"/\\|?*\x00-\x1F'

COMPONENT = (
    rf'(?!\.{{1,2}}(?:\\|$))'
    rf'[^{INVALID_CHARS}]+'
    rf'(?<![ .])'
)

WINDOWS_PATH_PATTERN = re.compile(
    rf'(?:'
    rf'[A-Za-z]:\\(?:{COMPONENT}\\)*{COMPONENT}'
    rf'|'
    rf'\\\\{COMPONENT}\\{COMPONENT}(?:\\{COMPONENT})*'
    rf')'
)


def validate_path(path: str) -> bool:
    """
    Проверяет синтаксическую корректность полного Windows-пути.
    """
    if not isinstance(path, str):
        return False

    return WINDOWS_PATH_PATTERN.fullmatch(path) is not None