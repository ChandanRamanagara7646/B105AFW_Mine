from generic.base_class import BaseClass
from generic.utility import Excel
from page.login_page import Login_Page
from page.home_page import Home_Page

class Test_Valid_Login(BaseClass):
    def test_valid_login(self):

        excel = Excel()
        un=excel.get_data(self.EXCEL_PATH,'ValidLogin',2,1)
        pw=excel.get_data(self.EXCEL_PATH,'ValidLogin',2,2)

        login_page=Login_Page(self.driver)
        login_page.set_username(un)
        login_page.set_password(pw)
        login_page.click_go()

        home_page=Home_Page(self.driver)
        result=home_page.verify_homepage_isDisplayed(self.wait)
        assert result
