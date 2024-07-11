from generic.base_class import BaseClass
from selenium.webdriver.common.by import By
from selenium.webdriver import Chrome


class Login_Page:

    def __init__(self,driver):
        self.driver=driver
        self.__un = (By.NAME, "username")
        self.__pw = (By.NAME, "password")
        self.__go = (By.NAME, "login-button")
        self.__errmsg = (By.CSS_SELECTOR, ".error")

    def set_username(self,un):
        self.driver.find_element(*self.__un).send_keys(un)

    def set_password(self,pw):
        self.driver.find_element(*self.__pw).send_keys(pw)

    def click_go(self):
        self.driver.find_element(*self.__go).click()
