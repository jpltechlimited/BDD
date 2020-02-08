import os
import time
from selenium.webdriver import Chrome, Firefox
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By


class CommonClient:
    def __init__(self, client_type, default_wait_time):
        self.default_wait_time = default_wait_time
        self.client_type = client_type
        self.__config__()
        self.__get_browser__()

    def __get_browser__(self):
        if os.environ[self.client_type + ".browser"] == "chrome":
            self.driver = Chrome(ChromeDriverManager().install())
        elif os.environ[self.client_type + "browser"] == "firefox":
            self.driver = Firefox()
        else:
            raise Exception(f'browser is not a supported')
        self.driver.implicitly_wait(self.default_wait_time)
        self.driver.maximize_window()

    def __config__(self):
        self.username = os.environ[self.client_type + ".username"]
        self.password = os.environ[self.client_type + ".password"]
        self.mainUrl = os.environ[self.client_type + ".mainUrl"]

    def __get_available_element__(self, by_locator, locator):
        return WebDriverWait(self.driver, self.default_wait_time).until(
            ec.visibility_of_element_located((by_locator, locator)),
            ec.element_to_be_clickable((by_locator, locator))
        )

    def __textbox_enter_text_by_name__(self, name, text):
        textbox = self.__get_available_element__(By.NAME, name)
        textbox.send_keys(text)

    def __textbox_enter_text_by_xpath__(self, xpath, text):
        textbox = self.__get_available_element__(By.XPATH, xpath)
        textbox.click()
        textbox.clear()
        time.sleep(1)
        textbox.send_keys(text)

    def __click_by_xpath__(self, xpath):
        button = self.__get_available_element__(By.XPATH, xpath)
        button.click()

    def __click_submit_by_name__(self, name):
        xpath = "//input[@type='submit' and @value='{}']".format(name)
        self.__click_by_xpath__(xpath)
