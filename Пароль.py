# объявление функции
def is_password_good(password):
    count1 = 0
    count2 = 0
    count3 = 0
    for i in password:
        if i in '0123456789':
            count1+=1
        if i.isupper()==True:
            count2+=1
        if i.islower()==True:
            count3+=1
    if count1>=1 and count2>=1 and count3>=1 and len(password)>=8:
        return True
    else:
        return False

# считываем данные
txt = input()

# вызываем функцию
print(is_password_good(txt))
