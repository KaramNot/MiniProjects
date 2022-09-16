# объявление функции
def is_palindrome(text):
    text = ''.join(i for i in text if i.isalpha()).lower()
    if text==text[::-1]:
        return True
    else:
        return False

# считываем данные
txt = input()

# вызываем функцию
print(is_palindrome(txt))
