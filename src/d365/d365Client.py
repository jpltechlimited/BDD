from selenium.webdriver.common.by import By
from src.commonClient import CommonClient


class D365Client(CommonClient):
    def __init__(self, with_login=False, default_wait_time=10):
        super().__init__("d365", default_wait_time)
        if with_login:
            self.__login__()

    def __login__(self):
        self.driver.get(self.mainUrl)
        self.__textbox_enter_text_by_name__("loginfmt", self.username)
        self.__click_submit_by_name__("Next")
        self.__textbox_enter_text_by_name__("passwd", self.password)
        self.__click_submit_by_name__("Sign in")
        self.__click_submit_by_name__("Yes")

    def form_fill_attribute_by_display_name(self, display_name, value):
        xpath = "//input[@aria-label='{}']".format(display_name)
        self.__textbox_enter_text_by_xpath__(xpath, value)

    def ribbon_click_on_button(self, display_name):
        ribbon = self.__get_available_element__(By.XPATH, "//ul[@aria-label='Commands']")
        buttons = ribbon.find_elements_by_xpath("//li")
        button = next(f for f in buttons if f.get_attribute('aria-label') == display_name)
        button.click()

    def navigate_switch_to_view(self, view):
        self.__click_by_xpath__("//span[contains(@id, 'ViewSelector')]")
        selector = self.__get_available_element__(By.XPATH, "//ul[contains(@id,'ViewSelector')]")
        options = selector.find_elements_by_xpath("//li[@role='option']")
        view_option = next(option for option in options if option.text == view)
        view_option.click()

    def navigate_to_subarea(self, area, subarea):
        area_button_xpath = "//button[@data-id='sitemap-areaSwitcher-expand-btn']"
        area_button = self.__get_available_element__(By.XPATH, area_button_xpath)
        area_button.click()
        options = area_button.find_elements_by_xpath("//ul[@aria-label='Change area']//li")
        area_option = next(option for option in options if option.text == area)
        area_option.click()
        xpath = "//li[@title='{}']".format(subarea)
        self.__click_by_xpath__(xpath)

    def dispose(self):
        self.driver.quit()
