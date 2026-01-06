import sys
from stats import get_num_words, get_chars_dict, sort_chars_dict


def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]

    text = get_book_text(book_path)

    num_words = get_num_words(text)
    print(f"Found {num_words} total words\n")

    chars_dict = get_chars_dict(text)
    sorted_chars = sort_chars_dict(chars_dict)

    print("Character counts:")
    for item in sorted_chars:
        char = item["char"]
        count = item["num"]

        if not char.isalpha():
            continue

        print(f"{char}: {count}")


main()
