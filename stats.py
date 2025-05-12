def get_num_words(text):
    parts = text.split()
    return len(parts)

def get_num_characters(text):
    frequencies = {}
    for c in text:

        frequencies[c.lower()] = frequencies.get(c.lower(), 0) + 1
    return frequencies

def sort_on(dict):
    return dict["num"]

def sort_character_frequencies(num_characters):
    dictionaries = []
    for key, value in num_characters.items():
        dictionaries.append({"char": key, "num": value})
    dictionaries.sort(reverse=True, key=sort_on)
    return dictionaries