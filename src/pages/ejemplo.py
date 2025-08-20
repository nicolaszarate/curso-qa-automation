from src.pages.BasePage import BasePage
from selenium.webdriver.common.by import By

class LoginPageConJson(BasePage):

    username_locator = (By.XPATH, "//input[@id='user-name']")
    password_locator = (By.XPATH, "//input[@id='password']")
    login_button_locator = (By.XPATH, "//input[@id='login-button']")
    locator_products = (By.XPATH, "//span[@class='title']")
    login_data = "loginJson.json"


    def open_url(self):
        obtener_url = self.get_data(self.login_data)
        url = obtener_url['url']
        self.navigate_to(url)

    def ingresar_usuario_json(self):
        obtener_user = self.get_data(self.login_data)
        usuario_value = obtener_user['username']
        self.input_text(self.username_locator, usuario_value)

    def ingresar_password_json(self):
        obtener_password = self.get_data(self.login_data)
        password_value = obtener_password['password']
        self.input_text(self.password_locator, password_value)

    def click_btn_ingresar_json(self):
        self.click_element(self.login_button_locator)

    def login_json(self):
        self.open_url()
        self.max_window()
        self.ingresar_usuario_json()
        self.ingresar_password_json()
        self.click_btn_ingresar_json()

