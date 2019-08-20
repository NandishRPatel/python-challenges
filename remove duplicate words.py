def remove_duplicate_words(s):
    list_string = []
    for i in s.split():
        if not i in list_string:
            list_string.append(i)
    return " ".join(list_string)