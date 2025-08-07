from selenium.webdriver.common.by import By
from src.pages.BasePage import BasePage




class LoginPage(BasePage):

    username = (By.XPATH, "//input[@id='user-name']")
    password = (By.XPATH, "//input[@id='password']")
    login_button = (By.XPATH, "//input[@id='login-button']")
    backpage = (By.XPATH, "//div[normalize-space()='Sauce Labs Backpack']")

    def ingresar_usuario(self, usuario):
        self.input_text(self.username,usuario)

    def ingresar_password(self, password):
        self.input_text(self.password, password)

    def click_login_button(self):
        self.click_element(self.login_button)

