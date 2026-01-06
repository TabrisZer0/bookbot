def get_num_words(text):
    return len(text.split())


def get_chars_dict(text):
    chars = {}
    for c in text:
        c = c.lower()
        if c in chars:
            chars[c] += 1
        else:
            chars[c] = 1
    return chars


def sort_chars_dict(chars_dict):
    chars_list = []

    for char, count in chars_dict.items():
        chars_list.append({"char": char, "num": count})

    def sort_on(d):
        return d["num"]

    chars_list.sort(reverse=True, key=sort_on)
    return chars_list
