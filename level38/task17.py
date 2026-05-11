import unittest

def add_item(lst, item):
    """Adiciona um elemento à lista."""
    lst.append(item)

def remove_item(lst, item):
    """Remove um elemento da lista."""
    lst.remove(item)

class TestListOperations(unittest.TestCase):
    def test_add_and_remove_item(self):
        # Criar lista vazia
        test_list = []
        
        # Adicionar elemento
        add_item(test_list, 'test_item')
        
        # Verificar se o elemento foi adicionado
        self.assertIn('test_item', test_list)
        
        # Remover elemento
        remove_item(test_list, 'test_item')
        
        # Verificar se a lista está vazia novamente
        self.assertEqual(test_list, [])

unittest.main()