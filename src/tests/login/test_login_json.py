import pytest
from selenium.webdriver.common.by import By
from src.pages.BasePage import BasePage
from src.pages.LoginPageConJson import LoginPageConJson
import time

@pytest.mark.regresion()
@pytest.mark.pepemujica()
class TestLogin:

    @classmethod
    def setup_class(cls):
        cls.driver = BasePage.initialize_ChromeDriver()
        cls.login_page_con_json = LoginPageConJson(cls.driver)

    @classmethod
    def teardown_class(cls):
        BasePage(cls.driver).close_browser()

    def test_login(self):
        # Login con usuario estándar
        self.login_page_con_json.login_json()
        # Verificar que el login fue exitoso

        print("Esperando 10 segundos para ver el resultado después de submit...")
        time.sleep(10)

        print("Test completado!")


