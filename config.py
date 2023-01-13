valid_email = "likoffka@mail.ru"
valid_pass = "Asd77777"

invalid_email = 'likoffka12@gmail.com'
invalid_pass = 'Asd99999'

name = 'Анна'
surname = 'Иванова'
region = 'Москва г'
email = 'likoffka13@gmail.com'
password = 'Zxc12345'

false_email = '123456'
false_mobile_max = '891178945236'
false_mobile_mini = '8911789452'
false_name_mini = 'А'
name_two_letters = "Он"
thirty_letters = 'Череззабороногузадерищенкоконь'
thirty_one_letters = 'Череззабороногузадерищенко-конь'

class TestData:
    BASE_URL = 'https://b2c.passport.rt.ru/'

    #Заголовки названий элементов
    FORM_AUTH_MAIL = 'Почта'
    AUTH = 'Авторизация'
    RECOVERY = 'Восстановление пароля'
    CHECK = 'Регистрация'
    VERIFICATION_EMAIL = 'Подтверждение email'
    VERIFICATION_INVALID_EMAIL = 'Введите телефон в формате +7ХХХХХХХХХХ или +375XXXXXXXXX, или email в формате example@email.ru'
    VERIFICATION_INVALID_NAME = 'Необходимо заполнить поле кириллицей. От 2 до 30 символов.'
    ENTRY_VK = 'Войти'
    OK = 'Одноклассники'
    CHOICE_ACCOUNT = 'Вход'
    MM = 'Войти и разрешить'
