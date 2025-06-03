def count_words(text):
    words_in_book = text.split()
    return len(words_in_book)

def count_chars(text):
    chars = {}
    for i in range(0, len(text)):
        char = text[i].lower()
        if char not in chars:
            chars[char] = 1
        else:
            chars[char] += 1
    return chars

def sort_on(dict):
    return dict["num"]

def sorted_list_of_dictionaries(dictionary):
    list = []
    for key in dictionary:
        list.append({"char": key, "num" : dictionary[key]})
    list.sort(reverse=True, key=sort_on)
    return list