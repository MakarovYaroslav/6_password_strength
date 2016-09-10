import re


def get_password_strength(password):
    strength = 1
    if len(password) == 0:
        return 0
    if len(password) > 14:
        strength += 3
    elif 12 <= len(password) <= 14:
        strength += 2
    elif 8 <= len(password) < 12:
        strength += 1
    if password.isdigit() == False:
        strength += 1
        if re.search('\d', password):
            strength += 2
    if (password.isupper() or password.islower()) == False:
        strength += 1
    if re.search('[@#$]', password):
            strength += 2
    return strength


if __name__ == '__main__':
    print('Сложность пароля = %s' % get_password_strength('dddd3Ddd##dddddd'))
