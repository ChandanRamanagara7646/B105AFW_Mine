import time

import pytest
import os
from pyjavaproperties import Properties
from selenium.webdriver import Chrome
from selenium.webdriver.support.ui import WebDriverWait


class BaseClass:

    @pytest.fixture(autouse=True)
    def pre_condition(self):
        generic = os.path.dirname(__file__)
        print('\n',generic)

        self.EXCEL_PATH=generic+"/../data/input.xlsx"

        ppt_obj=Properties()
        ppt_obj.load(open(generic+'/../config.properties'))
        browser=ppt_obj['BROWSER']
        app_url=ppt_obj['APP_URL']
        ito=ppt_obj['IMPLICIT_WAIT']
        eto=ppt_obj['EXPLICIT_WAIT']

        self.driver=Chrome()
        self.driver.get(app_url)
        self.driver.implicitly_wait(ito)
        self.wait=WebDriverWait(self.driver,eto)
        self.driver.maximize_window()
        time.sleep(2)

    @pytest.fixture(autouse=True)
    def post_condition(self):
        yield
        self.driver.quit()



