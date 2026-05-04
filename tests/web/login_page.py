from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
    URL = "https://www.saucedemo.com/"

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def abrir(self):
        self.driver.get(self.URL)

    def fazer_login(self, usuario, senha):
        self.wait.until(EC.presence_of_element_located((By.ID, "user-name"))).send_keys(usuario)
        self.driver.find_element(By.ID, "password").send_keys(senha)
        self.driver.find_element(By.ID, "login-button").click()

    def esta_na_pagina_de_produtos(self):
        return self.wait.until(
            EC.presence_of_element_located((By.CLASS_NAME, "inventory_list"))
        ).is_displayed()