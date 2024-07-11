from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class Home_Page:

    def __init__(self,driver):
        self.driver=driver
        self.__logout=(By.XPATH, "//a[text()='Logout']")

    def verify_homepage_isDisplayed(self,wait):
        try:
            wait.until(EC.visibility_of_element_located(self.__logout))
            print("Home page is displayed")
            return True
        except:
            print("Home page is not Displayed")
            return False
