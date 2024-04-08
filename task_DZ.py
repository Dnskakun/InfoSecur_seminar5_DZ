"""
Напишите программу на Python, которая будет проверять
вводимый пользователем пароль на сложность
(Authentication and password management):
● не менее 8 символов
● наличие прописных и строчных букв
● наличие цифр
● и переводит его в хэш-значение
"""
import bcrypt

def user_pass_with_check():
    user_password = input('Введите пароль (не менее 8 символов, с прописными и строчными буквами, цифрами: ')
    flag: bool = True
    flag_digit: bool = False
    flag_upper: bool = False
    flag_lower: bool = False
    while(flag):
        if (len(user_password) > 7):
            for i in range (len(user_password)):
                if (user_password[i].isdigit()): flag_digit = True
                if (user_password[i].isupper()): flag_upper = True
                if (user_password[i].islower()): flag_lower = True
            if (flag_digit and flag_upper and flag_lower):
                flag = False
            else:
                user_password = input('Попробуйте ещё раз: ')
        else:
            user_password = input('Попробуйте ещё раз: ')
    return user_password

def crypt_user_pass(user_password):
    crypt_user_password = bcrypt.hashpw(user_password.encode(), bcrypt.gensalt())
    print
    return crypt_user_password

hash_password = crypt_user_pass(user_pass_with_check())
print(hash_password)

valid = bcrypt.checkpw('234sfsdSDF3'.encode(), hash_password)
print(valid)




