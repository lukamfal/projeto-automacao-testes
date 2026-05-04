from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class InventoryPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def adicionar_primeiro_produto(self):
        botao = self.wait.until(
            EC.presence_of_element_located((By.XPATH, "//button[contains(text(),'Add to cart')]"))
        )
        nome = self.driver.find_element(By.CLASS_NAME, "inventory_item_name").text
        botao.click()
        return nome

    def ir_para_carrinho(self):
        self.driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()