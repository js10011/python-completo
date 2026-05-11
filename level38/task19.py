import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

class TestWebElements(unittest.TestCase):

    # Parâmetros para teste: navegadores, URL e elementos para verificação
    test_cases = [
        ("https://example.com", "login_button"),
        ("https://example.com", "registration_form"),
        ("https://example.com/registration", "submit_button"),
        ("https://example.com/registration", "name_field")
    ]

    def setUp(self):
        """Inicialização dos navegadores para cada teste"""
        self.browsers = {
            "chrome": webdriver.Chrome(service=ChromeService(ChromeDriverManager().install())),
            "firefox": webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
        }

    def tearDown(self):
        """Fechamento dos navegadores após cada teste"""
        for browser in self.browsers.values():
            browser.quit()

    def wait_for_element(self, browser, locator, timeout=10):
        """Aguarda a presença de um elemento pelo ID na página, considerando a instabilidade."""
        try:
            element_present = EC.visibility_of_element_located((By.ID, locator))
            WebDriverWait(browser, timeout).until(element_present)
            return True
        except Exception as e:
            print(f"Aviso: elemento com ID '{locator}' não encontrado no navegador {browser.name}. Erro: {e}")
            return False

    def test_elements_on_different_pages(self):
        """Teste principal com parametrização para verificar elementos nas páginas em diferentes navegadores."""
        for browser_name, browser in self.browsers.items():
            for url, element_id in self.test_cases:
                with self.subTest(browser=browser_name, url=url, element=element_id):
                    browser.get(url)  # Abre a página
                    element_exists = self.wait_for_element(browser, element_id)
                    # Verifica se o elemento foi encontrado
                    self.assertTrue(
                        element_exists,
                        f"Elemento com ID '{element_id}' não encontrado na página {url} no navegador {browser_name}"
                    )

# Execução dos testes
unittest.main()