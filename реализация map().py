def map(function, items):
    result = []
    for item in items:
        result.append(function(item))
    return result
words = ['abba', 'qwerty', 'python', 'a', 'deed', 'nun', 'level', 'deified', 'bbbbb', 'mother', 'surface', 'sister']

words_len = map(len, words)
print(max(words_len))
