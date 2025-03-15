from stats import get_char_count, get_word_count


def get_book_text(filepath):
    with open(filepath) as f:
        content = f.read()
        # print(content)
        get_word_count(content)
        chars = get_char_count(content)
        print(chars)


def main():
    get_book_text("./books/frankenstein.txt")


if __name__ == "__main__":
    main()
