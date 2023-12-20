from re import match


def registration_err(data: str) -> list:
    errors = []
    try:
        if not match(r'^[a-zA-Z0-9@\+\.\-\_]{8,30}$', data['username']):
            errors.append('Имя пользователя должно быть длинной 8 или больше символов'
                          ', содержать буквы(латиница), цифры, символы(@.+-_)')

        if data['password1'] != data['password2']:
            errors.append("Пароли не совпадают")
    except Exception as e:
        errors.append('Попробуйте еще раз')

    return errors
