import sys

from stats import char_count, process_char_count, word_count

# from stats import CharInfo


def get_book_text(filepath: str) -> str:
    with open(filepath) as f:
        return f.read()


def main():
    args: list[str] = sys.argv
    if len(args) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    filepath: str = args[1]
    frankenstein_text: str = get_book_text(filepath)
    # print(frankenstein_text)
    print(f"Found {word_count(frankenstein_text)} total words")
    frankenstein_char_count = char_count(frankenstein_text)
    clean_char_count = process_char_count(frankenstein_char_count)
    for char_info in clean_char_count:
        if not char_info["char"].isalpha():
            continue
        print(f"{char_info['char']}: {char_info['num']}")


if __name__ == "__main__":
    main()
