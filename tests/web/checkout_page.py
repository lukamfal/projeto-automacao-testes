from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time


class CheckoutPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def ir_para_checkout(self):
        self.wait.until(EC.element_to_be_clickable((By.ID, "checkout"))).click()

    def _fechar_alerta_se_existir(self):
        try:
            botao_ok = self.driver.find_element(
                By.XPATH, "//button[contains(., 'OK') or contains(., 'Ok') or contains(., 'Dispensar') or contains(., 'Fechar')]"
            )
            botao_ok.click()
            time.sleep(0.5)
        except:
            pass

    def _digitar_no_campo(self, field_id, valor):
        self._fechar_alerta_se_existir()
        campo = self.wait.until(EC.visibility_of_element_located((By.ID, field_id)))
        campo.click()
        time.sleep(0.2)
        self._fechar_alerta_se_existir()
        campo.send_keys(Keys.CONTROL + "a")
        campo.send_keys(Keys.DELETE)
        for letra in valor:
            campo.send_keys(letra)
            time.sleep(0.05)

    def preencher_dados(self, nome, sobrenome, cep):
        self._digitar_no_campo("first-name", nome)
        self._digitar_no_campo("last-name", sobrenome)
        self._digitar_no_campo("postal-code", cep)
        time.sleep(0.5)
        self.wait.until(EC.element_to_be_clickable((By.ID, "continue"))).click()

    def finalizar_compra(self):
        finish = self.wait.until(EC.element_to_be_clickable((By.ID, "finish")))
        finish.click()

    def compra_concluida(self):
        mensagem = self.wait.until(
            EC.presence_of_element_located((By.CLASS_NAME, "complete-header"))
        ).text
        return "Thank you" in mensagem