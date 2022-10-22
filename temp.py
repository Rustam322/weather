import random
import string

login = 'admin'
password = 'qwerty'

j = 0
while True:
    j += 1
    pas = ''
    for i in range(6):
        pas += random.choice(list(
                                  string.ascii_lowercase

                                ))

    print(f'Попытка №{j} - пароль: {pas}')
    if pas == password:
        print('Взлом удался')
        break
