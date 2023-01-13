from selenium.webdriver.common.by import By
from pages.Base_page import BasePage
from config import TestData

class MainPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.BASE_URL)


    MAIN_LOGO = (By.CSS_SELECTOR, "#app-header > div > div > svg")
    MAIL = (By.XPATH, "//*[@id='t-btn-tab-mail']")
    USERNAME = (By.XPATH, '// *[ @ id = "username"]')
    PASS = (By.XPATH, '//*[@id="password"]')
    BUTTON_INPUT = (By.XPATH, '//*[@id="kc-login"]')
    BUTTON_LOGOUT = (By.CSS_SELECTOR, "#logout-btn")
    ERROR_USERNAME_PASS = (By.XPATH, '// *[ @ id = "form-error-message"]')
    FORGOT = (By.CSS_SELECTOR, "#forgot_password")
    PAGE_RIGHT = (By.XPATH, '//*[@id="page-right"]/div/div/h1')
    BACK_BUTTON = (By.XPATH, '//*[@id="reset-back"]')
    REGISTER = (By.XPATH, '// *[ @ id = "kc-register"]')
    NAME = (By.XPATH, '//*[@id="page-right"]/div/div/div/form/div[1]/div[1]/div/input')
    SURNAME = (By.XPATH, '//*[@id="page-right"]/div/div/div/form/div[1]/div[2]/div/input')
    REGION = (By.XPATH, '//*[@id="page-right"]/div/div/div/form/div[2]/div/div/input')
    EMAIL = (By.XPATH, '//*[@id="address"]')
    PASSWORD = (By.XPATH, '//*[@id="password"]')
    PASSWORD_REPEAT = (By.XPATH, '//*[@id="password-confirm"]')
    BUTTON_REGISTER = (By.XPATH, '//*[@id="page-right"]/div/div/div/form/button')
    ERROR_HINT_EMAIL = (By.XPATH, '//*[@id="page-right"]/div/div/div/form/div[3]/span')
    ERROR_HINT_NAME = (By.XPATH, '//*[@id="page-right"]/div/div/div/form/div[1]/div[1]/span')
    VK = (By.CSS_SELECTOR, '#oidc_vk>svg')
    BUTTON_ENTRY_VK = (By.CSS_SELECTOR, '#install_allow')
    OK = (By.CSS_SELECTOR, '#oidc_ok>svg')
    LABLE_OK = (By.CSS_SELECTOR, '#widget-el>div.ext-widget_h>div')
    G = (By.XPATH, '//*[@id="oidc_google"]')
    ACCOUNT_G = (By.XPATH, '//*[@id="headingText"]/span[1]')
    MY_WORLD = (By.XPATH, '//*[@id="oidc_mail"]')
    BUTTON_ENTRY_MM = (By.XPATH, '//*[@id="login-form"]/div[2]/button')
    YA = (By.XPATH, '//*[@id="oidc_ya"]')
    LABLE_YA = (By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div/div/div[2]/div[1]/div/a')
