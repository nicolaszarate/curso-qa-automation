from src.pages.BasePage import BasePage
from src.pages.EjercicioLoginPage import LoginPage
import pytest

class TestLogin_ejercicio:
    @classmethod
    def setup_class(cls):
        cls.driver = BasePage.initialize_ChromeDriver()
        cls.login_page = LoginPage(cls.driver)

    @classmethod
    def teardown_class(cls):
        BasePage(cls.driver).close_browser()

    def test_login(self):
        self.login_page.navigate_to("https://the-internet.herokuapp.com/login")
        self.login_page.max_window()
        self.login_page.ingresar_usuario("tomsmith")
        self.login_page.ingresar_password("SuperSecretPassword!")
        self.login_page.click_login_button()