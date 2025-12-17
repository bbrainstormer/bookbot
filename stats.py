from typing import TypedDict

from typing_extensions import Dict, List


class CharInfo(TypedDict):
    char: str
    num: int


def word_count(text: str) -> int:
    return len(text.split())


def char_count(text: str) -> Dict[str, int]:
    counts: Dict[str, int] = {}
    for char in text.lower():
        counts[char] = counts.get(char, 0) + 1
    return counts


def process_char_count(counts: Dict[str, int]) -> List[CharInfo]:
    li: List[CharInfo] = []
    for char in counts:
        li.append({"char": char, "num": counts[char]})
    li.sort(reverse=True, key=(lambda char_info: char_info["num"]))
    return li
