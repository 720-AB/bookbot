import sys
from stats import get_character_count, get_num_words, get_sorted_char_list




def get_book_text(path):
    with open(path) as f:
        return f.read()


def main():

    if len(sys.argv) != 2:
        print("Usage: python3 bootbot.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]

    text = get_book_text(book_path)

    num_words = get_num_words(text)
    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document")
    print()

    char_count = get_character_count(text)

    sorted_chars = get_sorted_char_list(char_count)

    for char_info in sorted_chars:
        char = char_info["char"]
        count = char_info["num"]

        if char.isalpha():
            print(f"The '{char}' character was found {count} times")

    print("--- End report ---")

main()
