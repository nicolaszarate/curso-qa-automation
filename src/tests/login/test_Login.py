from src.pages.BasePage import BasePage
from src.pages.LoginPage import LoginPage
import pytest

class TestLogin:
    @classmethod
    def setup_class(cls):
        cls.driver = BasePage.initialize_ChromeDriver()
        cls.login_page = LoginPage(cls.driver)

    @classmethod
    def teardown_class(cls):
        BasePage(cls.driver).close_browser()


    def test_login(self):
       self.login_page.navigate_to("https://www.saucedemo.com/")
       self.login_page.max_window()
       self.login_page.ingresar_usuario("standard_user")
       self.login_page.ingresar_password("secret_sauce")
       self.login_page.click_login_button()

       products_text = self.login_page.get_text(self.login_page.backpage)
       assert "Sauce Labs Backpack" == products_text, f"Se esperaba 'Products' en el texto, pero se obtuvo: {products_text}"

