from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    #найти элемент и кликнуть по нему
    def find_click(self, by_locator):
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(by_locator)).click()

    # Проверить видимость элемента
    def is_visible(self, by_locator) -> bool:
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        return bool(element)

    #Ввод данных в строку ввода
    def input_keys(self, by_locator, text):
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(by_locator)).send_keys(text)

    #Получить заголовок окна
    def get_windows_title(self, text) -> bool:
        windows_title = WebDriverWait(self.driver, 5).until(EC. title_contains(text))
        return bool(windows_title)

    #Получить  атрибут текст элемента
    def get_text_of_element(self, by_locator):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        return element.text

    #Найти элемент
    def find_one_element(self, by_locator):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        return element