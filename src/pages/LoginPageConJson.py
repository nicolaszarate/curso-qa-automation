from src.pages.BasePage import BasePage
from selenium.webdriver.common.by import By

class LoginPageConJson(BasePage):

    firstname_locator = (By.XPATH, "//input[@id='firstName']")
    lastname_locator = (By.XPATH, "//input[@id='lastName']")
    email_locator = (By.XPATH, "//input[@id='userEmail']")
    gender_locator = (By.XPATH, "//label[normalize-space()='Male']")
    mobile_locator = (By.XPATH, "//input[@id='userNumber']")
    date_locator = (By.XPATH, "//input[@id='dateOfBirthInput']")
    hobbies_locator = (By.XPATH, "//label[normalize-space()='Sports']")
    direccion_locator = (By.XPATH, "//textarea[@id='currentAddress']")
    submit_button_locator = (By.XPATH, "//button[@id='submit']")
    login_data = "loginJson.json"

    def open_url(self):
        obtener_url = self.get_data(self.login_data)
        url = obtener_url['url']
        self.navigate_to(url)

    def ingresar_firstname_json(self):
        obtener_name = self.get_data(self.login_data)
        name_value = obtener_name['firstname']
        self.input_text(self.firstname_locator, name_value)

    def ingresar_lastname_json(self):
        obtener_lastname = self.get_data(self.login_data)
        lastname_value = obtener_lastname['lastname']
        self.input_text(self.lastname_locator, lastname_value)

    def ingresar_email_json(self):
        obtener_email = self.get_data(self.login_data)
        email_value = obtener_email['email']
        self.input_text(self.email_locator, email_value)

    def click_gender_json(self):
        self.click_element(self.gender_locator)

    def ingresar_mobile_json(self):
        obtener_mobile = self.get_data(self.login_data)
        mobile_value = obtener_mobile['mobile']
        self.input_text(self.mobile_locator, mobile_value)


    def ingresar_date_json(self):
        obtener_date = self.get_data(self.login_data)
        date_value = obtener_date['date']
        self.input_text(self.date_locator, date_value)

    def ingresar_hobbies_json(self):
        element = self.wait_for_element(self.hobbies_locator)
        self.driver.execute_script("arguments[0].click();", element)


    def ingresar_direccion_json(self):
        obtener_direccion = self.get_data(self.login_data)
        direccion_value = obtener_direccion['direccion']
        self.input_text(self.direccion_locator, direccion_value)

    def click_submit_button_json(self):
        self.click_element(self.submit_button_locator)

    def login_json(self):
        self.open_url()
        self.max_window()
        self.ingresar_firstname_json()
        self.ingresar_lastname_json()
        self.ingresar_email_json()
        self.click_gender_json()
        self.ingresar_mobile_json()
        self.ingresar_date_json()
        self.ingresar_hobbies_json()
        self.ingresar_direccion_json()
        self.click_submit_button_json()
