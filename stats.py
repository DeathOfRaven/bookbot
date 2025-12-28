def get_num_words(text):
    words = text.split()
    return len(words)

def get_num_characters(text):
    text = text.lower()
    result = {
        'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0, 'h': 0, 'i': 0, 'j': 0, 'k': 0, 'l': 0, 'm': 0, 
        'n': 0, 'o': 0, 'p': 0, 'q': 0, 'r': 0, 's': 0, 't': 0, 'u': 0, 'v': 0, 'w': 0, 'x': 0, 'y': 0, 'z': 0,
        'æ': 0, 'â': 0, 'ê': 0, 'ë': 0, 'ô': 0
    }
    characters = [*text]
    for char in characters:
        if char  in result:
            result[char] += 1
    return result

def sort_on(items):
    return items["num"]

def sorting(num_char):
    sorted = []
    for characters in num_char:
        dic = {"char": characters, "num": num_char[characters]}
        sorted.append(dic)
    sorted.sort(reverse = True, key=sort_on)
    return sorted