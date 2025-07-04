
def keys_and_values(word):
    result = {}
    for char in word:
        if char in result:
            result[char] += 1
        result[char] = 1
    return result

print(keys_and_values('GOOGLE'))