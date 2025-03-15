def get_word_count(text):
    word_count = len(text.split())
    print(f"{word_count} words found in the document")


def get_char_count(text):
    chars = {}
    for i in range(len(text)):
        char = text[i].lower()
        if char in chars:
            chars[char] += 1
        else:
            chars[char] = 1
    return chars
