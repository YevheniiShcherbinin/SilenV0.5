from lib2to3.pgen2 import driver
from pages.login import *
from pages.headernavigation import *
from selenium import webdriver
import pytest
import time


class Test:

    def test_koralgo_dev(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get("https://dev.koralgo.com/")

        login = Login(driver)
        login.login()
        login.enter_credentials()
        login.login_to_app()

        headmenu = HeaderMenu(driver)
        headmenu.search_page()
        headmenu.LogOut()

        time.sleep(5)
        driver.quit()


if __name__ == "__main__":
    Test.test_koralgo_dev(self=Test())
