import unittest
from selenium import webdriver

class TestExampleDomain(unittest.TestCase):
    def setUp(self):
        # Criamos uma instância do driver do navegador
        self.driver = webdriver.Chrome()
        self.driver.get("https://example.com")

    def test_open_page(self):
        # Verificação do título da página
        self.assertEqual(self.driver.title, "Example Domain")

    def tearDown(self):
        # Fechamento do navegador após a execução do teste
        self.driver.quit()

unittest.main()