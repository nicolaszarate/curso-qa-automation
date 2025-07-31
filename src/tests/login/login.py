from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest


@pytest.mark.regresion
class TestLoginHardCodeado:


   @classmethod
   def setup_class(cls):
       cls.driver = webdriver.Chrome()
       cls.driver.implicitly_wait(10)


   @classmethod
   def teardown_class(cls):
       cls.driver.quit()


   def test_login(self):
       driver = self.driver


       # Navegar a la página
       driver.get("https://www.saucedemo.com/")
       driver.maximize_window()


       # Realizar login con datos hardcodeados
       driver.find_element(By.ID, "user-name").send_keys("standard_user")
       driver.find_element(By.ID, "password").send_keys("secret_sauce")
       driver.find_element(By.ID, "login-button").click()

       # Verificar que el login fue exitoso
       products_text = driver.find_element(By.CLASS_NAME, "title").text
       assert "Products" == products_text, f"Se esperaba 'Products' en el texto, pero se obtuvo: {products_text}"