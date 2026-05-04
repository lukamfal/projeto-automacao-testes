import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "."))

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from login_page import LoginPage
from inventory_page import InventoryPage
from checkout_page import CheckoutPage


@pytest.fixture
def driver():
    options = Options()
    options.add_argument("--start-maximized")
    options.add_argument("--disable-save-password-bubble")
    options.add_argument("--disable-features=PasswordManager,PasswordLeakDetection")
    options.add_argument("--disable-notifications")
    options.add_experimental_option("prefs", {
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False,
        "profile.password_manager_leak_detection": False,
        "safebrowsing.enabled": False
    })
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()


class TestE2ECompra:
    """Fluxo completo: login → carrinho → finalizar compra."""

    def test_fluxo_completo_compra(self, driver):
        # 1. Login
        login = LoginPage(driver)
        login.abrir()
        login.fazer_login("standard_user", "secret_sauce")
        assert login.esta_na_pagina_de_produtos()

        # 2. Adicionar produto ao carrinho
        inventario = InventoryPage(driver)
        inventario.adicionar_primeiro_produto()
        inventario.ir_para_carrinho()

        # 3. Finalizar compra
        checkout = CheckoutPage(driver)
        checkout.ir_para_checkout()
        checkout.preencher_dados("Lucca", "Teste", "12345")
        checkout.finalizar_compra()

        assert checkout.compra_concluida()