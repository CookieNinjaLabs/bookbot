from stats import get_char_count, get_word_count, sort_dictionary


def get_book_text(filepath):
    with open(filepath) as f:
        content = f.read()
        return content


def print_report(path, word_count, chars):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"{word_count} words found in the document")
    print("----------- Character Count ----------")
    for item in chars:
        if item["char"].isalpha():
            print(f"{item['char']}: {item['count']}")


def main():
    path = "./books/frankenstein.txt"
    book_text = get_book_text(path)
    word_count = get_word_count(book_text)
    chars = get_char_count(book_text)
    sorted_chars = sort_dictionary(chars)
    print_report(path, word_count, sorted_chars)


if __name__ == "__main__":
    main()
