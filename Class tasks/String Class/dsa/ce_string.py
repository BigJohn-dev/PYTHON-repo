
def new_word(word, add='ce'):
    if len(word) % 2 == 0:
        mid = len(word) // 2
        return word[:mid] + add + word[mid:]
    return word + add