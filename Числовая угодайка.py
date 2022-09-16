import random

print("Добро пожаловать в числовую угадайку!!!")

def y_net(y):
    if y=='да' or y=='нет':
        return True
    else:
        return False
def is_valid(num, z):
    if num>=1 and num<=z:
        return True
    else:
        return False
y = input('сыграем? да или нет   :')
while y_net(y)==False:
    y = input('да или нет не понятно? :')
while y !="нет":
    z = int(input('Выбири до какого числа я загадываю от 1 до:'))
    num_kompytera = random.randint(1, z)
    count = 1
    x = False
    while x!=True:
        num_polzovately = int(input('какое число я загадал?  '))
        if is_valid(num_polzovately, z)==False:
            print('А может быть все-таки введем целое число?  ')
            continue
        if is_valid(num_polzovately, z)==True:
            if num_polzovately>num_kompytera:
                print('Ваше число больше загаданного, попробуйте еще разок')
                count+=1
                continue
            elif num_polzovately<num_kompytera:
                print('Ваше число меньше загаданного, попробуйте еще разок')
                count+=1
                continue
            else:
                print('Вы угадали, поздравляем!')
                print('число попыток =', count)
                x = True
                break
    y = input('сыграем? да или нет:').lower()
    while y_net(y)==False:
        y = input('да или нет не понятно? :')
input()
