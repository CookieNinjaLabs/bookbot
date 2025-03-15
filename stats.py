def get_word_count(text):
    word_count = len(text.split())
    return word_count


def get_char_count(text):
    chars = {}
    for i in range(len(text)):
        char = text[i].lower()
        if char in chars:
            chars[char] += 1
        else:
            chars[char] = 1
    return chars


def sort_on(item: dict):
    return item["count"]


def sort_dictionary(input_dict):
    list_of_dicts = []
    for key in input_dict:
        list_of_dicts.append({"char": key, "count": input_dict[key]})

    list_of_dicts.sort(reverse=True, key=sort_on)
    return list_of_dicts
