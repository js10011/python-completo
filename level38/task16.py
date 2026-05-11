import unittest

# Função que estamos testando
def string_length(s):
    """Retorna o comprimento da string fornecida."""
    return len(s)


# Classe para testar métodos de string
class TestStringMethods(unittest.TestCase):
    # Teste para a função string_length
    def test_string_length(self):
        # Verifica se o comprimento da string "Hello, World!" é 13
        self.assertEqual(string_length("Hello, World!"), 13)

# Execução dos testes
unittest.main()