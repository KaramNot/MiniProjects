import random
digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_'
chars = ''
cal = int(input('Количество паролей для генерации?'))
a = int(input('Длину одного пароля?'))
b = input('Включать ли цифры 0123456789?(y/n)')
c = input('Включать ли прописные буквы ABCDEFGHIJKLMNOPQRSTUVWXYZ?(y/n)')
d = input('Включать ли строчные буквы abcdefghijklmnopqrstuvwxyz?(y/n)')
e = input('Включать ли символы !#$%&*+-=?@^_?(y/n)')
f = input('Исключить символы il1Lo0O?(y/n)')
if b=='y':
    chars+=digits
if c=='y':
    chars+=uppercase_letters
if d=='y':
    chars+=lowercase_letters
if e=='y':
    chars+=punctuation
if f=='y':
    for c in 'il1Lo0O':
        chars = chars.replace(c, '')
    
def generate_password(a, chars):
    password = ''
    for j in range(a):
        password += random.choice(chars)
    return password
for _ in range(cal):
    print(generate_password(a, chars))

input()
