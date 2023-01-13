from pages.Main_page import MainPage
from config import TestData, valid_pass, valid_email, invalid_pass, invalid_email, name, surname, region, email, \
    password, false_email, false_mobile_mini, false_mobile_max, false_name_mini, name_two_letters, \
    thirty_letters, thirty_one_letters

# Строка для запуска кода
# python -m pytest -v --driver Chrome --driver-path /tests/chromedriver.exe tests/test_rostelekom.py

# ТК-РТ-001
# Логотип Ростелеком (переход на форму авторизации) виден на странице
def test_main_logo_on_page(driver):
    main_page = MainPage(driver)
    logo = main_page.is_visible(MainPage.MAIN_LOGO)
    assert logo == True

# ТК-РТ-002
# Кнопка "Почта" кликабельна и открывает форму авторизации с полем "Электронная почта"
def test_mail_clickable(driver):
    main_page = MainPage(driver)
    main_page.find_click(MainPage.MAIL)
    mail = main_page.is_visible(MainPage.USERNAME)
    assert mail == True

# ТК-РТ-003
# Авторизация по электронной почте и паролю
def test_auth_mail(driver):
    main_page = MainPage(driver)
    main_page.input_keys(MainPage.USERNAME, valid_email)
    main_page.input_keys(MainPage.PASS, valid_pass)
    main_page.find_click(MainPage.BUTTON_INPUT)
    logout = main_page.is_visible(MainPage.BUTTON_LOGOUT)
    assert logout == True

# ТК-РТ-004
# Авторизация по невалидной электронной почте и невалидному паролю
def test_invalid_auth_mail(driver):
    main_page = MainPage(driver)
    main_page.input_keys(MainPage.USERNAME, invalid_email)
    main_page.input_keys(MainPage.PASS, invalid_pass)
    main_page.find_click(MainPage.BUTTON_INPUT)
    error = main_page.is_visible(MainPage.ERROR_USERNAME_PASS)
    assert error == True

# ТК-РТ-005
# Авторизация по валидной электронной почте и невалидному паролю
def test_pass_invalid_auth_mail(driver):
    main_page = MainPage(driver)
    main_page.input_keys(MainPage.USERNAME, valid_email)
    main_page.input_keys(MainPage.PASS, invalid_pass)
    main_page.find_click(MainPage.BUTTON_INPUT)
    error_pass = main_page.is_visible(MainPage.ERROR_USERNAME_PASS)
    assert error_pass == True

# ТК-РТ-006
# Авторизация по невалидной электронной почте и валидному паролю
def test_elmail_invalid_auth_mail(driver):
    main_page = MainPage(driver)
    main_page.input_keys(MainPage.USERNAME, invalid_email)
    main_page.input_keys(MainPage.PASS, valid_pass)
    main_page.find_click(MainPage.BUTTON_INPUT)
    error_username = main_page.is_visible(MainPage.ERROR_USERNAME_PASS)
    assert error_username == True

# ТК-РТ-007
# Кнопка "Забыл пароль" кликабельна и открывает форму "Восстановление пароля"
def test_forgot_password(driver):
    main_page = MainPage(driver)
    main_page.find_click(MainPage.FORGOT)
    recovery = main_page.get_text_of_element(MainPage.PAGE_RIGHT)
    assert recovery == TestData.RECOVERY

# ТК-РТ-008
# Кнопка "Вернуться назад" в форме "Восстановление пароля" кликабельна и открывает форму "Авторизация"
def test_back_button(driver):
    main_page = MainPage(driver)
    main_page.find_click(MainPage.FORGOT)
    main_page.find_click(MainPage.BACK_BUTTON)
    auth_name = main_page.get_text_of_element(MainPage.PAGE_RIGHT)
    assert auth_name == TestData.AUTH

# ТК-РТ-009
# Кнопка "Зарегистрироваться" кликабельна и открывает форму "Регистрация"
def test_click_check_in(driver):
    main_page = MainPage(driver)
    main_page.find_click(MainPage.REGISTER)
    check_in = main_page.get_text_of_element(MainPage.PAGE_RIGHT)
    assert check_in == TestData.CHECK

# ТК-РТ-010
# Заполнение формы "Регистрация" валидными данными и кликабельность кнопки "Зарегистрироваться"
def test_check_in(driver):
    main_page = MainPage(driver)
    main_page.find_click(MainPage.REGISTER)
    main_page.input_keys(MainPage.NAME, name)
    main_page.input_keys(MainPage.SURNAME, surname)
    main_page.input_keys(MainPage.REGION, region)
    main_page.input_keys(MainPage.EMAIL, email)
    main_page.input_keys(MainPage.PASSWORD, password)
    main_page.input_keys(MainPage.PASSWORD_REPEAT, password)
    main_page.find_click(MainPage.BUTTON_REGISTER)
    valid_reg = main_page.get_text_of_element(MainPage.PAGE_RIGHT)
    assert valid_reg == TestData.VERIFICATION_EMAIL

# ТК-РТ-011
# Заполнение формы "Регистрация" c невалидным email
def test_check_in_false_email(driver):
    main_page = MainPage(driver)
    main_page.find_click(MainPage.REGISTER)
    main_page.input_keys(MainPage.NAME, name)
    main_page.input_keys(MainPage.SURNAME, surname)
    main_page.input_keys(MainPage.REGION, region)
    main_page.input_keys(MainPage.EMAIL, false_email)
    main_page.input_keys(MainPage.PASSWORD, password)
    main_page.input_keys(MainPage.PASSWORD_REPEAT, password)
    main_page.find_click(MainPage.BUTTON_REGISTER)
    invalid_reg = main_page.get_text_of_element(MainPage.ERROR_HINT_EMAIL)
    assert invalid_reg == TestData.VERIFICATION_INVALID_EMAIL

# ТК-РТ-012
# Заполнение формы "Регистрация" c невалидным mobile (на 1 цифру больше)
def test_check_in_false_mobile_max(driver):
    main_page = MainPage(driver)
    main_page.find_click(MainPage.REGISTER)
    main_page.input_keys(MainPage.NAME, name)
    main_page.input_keys(MainPage.SURNAME, surname)
    main_page.input_keys(MainPage.REGION, region)
    main_page.input_keys(MainPage.EMAIL, false_mobile_max)
    main_page.input_keys(MainPage.PASSWORD, password)
    main_page.input_keys(MainPage.PASSWORD_REPEAT, password)
    main_page.find_click(MainPage.BUTTON_REGISTER)
    invalid_reg = main_page.get_text_of_element(MainPage.ERROR_HINT_EMAIL)
    assert invalid_reg == TestData.VERIFICATION_INVALID_EMAIL

# ТК-РТ-013
# Заполнение формы "Регистрация" c невалидным mobile (на 1 цифру меньше)
def test_check_in_false_mobile_mini(driver):
    main_page = MainPage(driver)
    main_page.find_click(MainPage.REGISTER)
    main_page.input_keys(MainPage.NAME, name)
    main_page.input_keys(MainPage.SURNAME, surname)
    main_page.input_keys(MainPage.REGION, region)
    main_page.input_keys(MainPage.EMAIL, false_mobile_mini)
    main_page.input_keys(MainPage.PASSWORD, password)
    main_page.input_keys(MainPage.PASSWORD_REPEAT, password)
    main_page.find_click(MainPage.BUTTON_REGISTER)
    invalid_reg = main_page.get_text_of_element(MainPage.ERROR_HINT_EMAIL)
    assert invalid_reg == TestData.VERIFICATION_INVALID_EMAIL

# ТК-РТ-014
# Заполнение формы "Регистрация" с невалидным именем (менее 2 символов)
def test_check_in_false_name_mini(driver):
    main_page = MainPage(driver)
    main_page.find_click(MainPage.REGISTER)
    main_page.input_keys(MainPage.NAME, false_name_mini)
    main_page.input_keys(MainPage.SURNAME, surname)
    main_page.input_keys(MainPage.REGION, region)
    main_page.input_keys(MainPage.EMAIL, email)
    main_page.input_keys(MainPage.PASSWORD, password)
    main_page.input_keys(MainPage.PASSWORD_REPEAT, password)
    main_page.find_click(MainPage.BUTTON_REGISTER)
    invalid_reg = main_page.get_text_of_element(MainPage.ERROR_HINT_NAME)
    assert invalid_reg == TestData.VERIFICATION_INVALID_NAME

# ТК-РТ-015
# Заполнение формы "Регистрация" с валидным именем (2 кириллических символа)
def test_check_in_name_two_letters(driver):
    main_page = MainPage(driver)
    main_page.find_click(MainPage.REGISTER)
    main_page.input_keys(MainPage.NAME, name_two_letters)
    main_page.input_keys(MainPage.SURNAME, surname)
    main_page.input_keys(MainPage.REGION, region)
    main_page.input_keys(MainPage.EMAIL, email)
    main_page.input_keys(MainPage.PASSWORD, password)
    main_page.input_keys(MainPage.PASSWORD_REPEAT, password)
    main_page.find_click(MainPage.BUTTON_REGISTER)
    valid_reg = main_page.get_text_of_element(MainPage.PAGE_RIGHT)
    assert valid_reg == TestData.VERIFICATION_EMAIL

# ТК-РТ-016
# Заполнение формы "Регистрация" с валидным именем (30 кириллических символов)
def test_check_in_name_thirty_letters(driver):
    main_page = MainPage(driver)
    main_page.find_click(MainPage.REGISTER)
    main_page.input_keys(MainPage.NAME, thirty_letters)
    main_page.input_keys(MainPage.SURNAME, surname)
    main_page.input_keys(MainPage.REGION, region)
    main_page.input_keys(MainPage.EMAIL, email)
    main_page.input_keys(MainPage.PASSWORD, password)
    main_page.input_keys(MainPage.PASSWORD_REPEAT, password)
    main_page.find_click(MainPage.BUTTON_REGISTER)
    valid_reg = main_page.get_text_of_element(MainPage.PAGE_RIGHT)
    assert valid_reg == TestData.VERIFICATION_EMAIL

# ТК-РТ-017
# Заполнение формы "Регистрация" с невалидным именем (31 кириллический символ)
def test_check_in_name_thirty_one_letters(driver):
    main_page = MainPage(driver)
    main_page.find_click(MainPage.REGISTER)
    main_page.input_keys(MainPage.NAME, thirty_one_letters)
    main_page.input_keys(MainPage.SURNAME, surname)
    main_page.input_keys(MainPage.REGION, region)
    main_page.input_keys(MainPage.EMAIL, email)
    main_page.input_keys(MainPage.PASSWORD, password)
    main_page.input_keys(MainPage.PASSWORD_REPEAT, password)
    main_page.find_click(MainPage.BUTTON_REGISTER)
    invalid_reg = main_page.get_text_of_element(MainPage.ERROR_HINT_NAME)
    assert invalid_reg == TestData.VERIFICATION_INVALID_NAME

# ТК-РТ-018
# Кнопка "VK" кликабельна и открывает форму для регистрации через аккаунт VK
def test_click_vk(driver):
    main_page = MainPage(driver)
    main_page.find_click(MainPage.VK)
    check_in = main_page.get_text_of_element(MainPage.BUTTON_ENTRY_VK)
    assert check_in == TestData.ENTRY_VK

# ТК-РТ-019
# Кнопка "OK" кликабельна и открывает форму для регистрации через аккаунт OK
def test_click_ok(driver):
    main_page = MainPage(driver)
    main_page.find_click(MainPage.OK)
    check_in = main_page.get_text_of_element(MainPage.LABLE_OK)
    assert check_in == TestData.OK

# ТК-РТ-020
# Кнопка "@" ("Мой мир") кликабельна и открывает форму для регистрации через аккаунт Электронную почту
def test_click_mail(driver):
    main_page = MainPage(driver)
    main_page.find_click(MainPage.MY_WORLD)
    check_in = main_page.get_text_of_element(MainPage.BUTTON_ENTRY_MM)
    assert check_in == TestData.MM

# ТК-РТ-021
# Кнопка "G" ("Google") кликабельна и открывает форму для регистрации через аккаунт Google
def test_click_g(driver):
    main_page = MainPage(driver)
    main_page.find_click(MainPage.G)
    check_in = main_page.get_text_of_element(MainPage.ACCOUNT_G)
    assert check_in == TestData.CHOICE_ACCOUNT

# ТК-РТ-022
# Кнопка "Я" кликабельна и открывает форму для регистрации через аккаунт Яндекс
def test_click_ya(driver):
    main_page = MainPage(driver)
    main_page.find_click(MainPage.YA)
    check_in = main_page.is_visible(MainPage.LABLE_YA)
    assert check_in == True



