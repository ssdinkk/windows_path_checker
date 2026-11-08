import re

from business.validator import validate_path


PATH_CANDIDATE_PATTERN = re.compile(
    r'(?<![A-Za-z0-9_])'
    r'(?:[A-Za-z]:\\|\\\\)'
    r'[^\s<>:"/|?*]+'
)


def find_paths(text: str) -> list[str]:
    """
    Находит корректные Windows-пути в произвольном тексте.
    """
    if not isinstance(text, str):
        return []

    found_paths = []

    for match in PATH_CANDIDATE_PATTERN.finditer(text):
        candidate = match.group().rstrip(".,;!?)]}")

        if validate_path(candidate):
            found_paths.append(candidate)

    return found_paths