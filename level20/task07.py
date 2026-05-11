# Importe o módulo math incorporado
import math as std_math

# Chamada da função sqrt do módulo math padrão
print(std_math.sqrt(9))

# Importe o módulo math personalizado
import importlib.util

# Caminho para o módulo personalizado
# custom_math_path = './math.py'
custom_math_path = 'core/level11/task17/math.py'

# Carregue o módulo math personalizado
spec = importlib.util.spec_from_file_location("custom_math", custom_math_path)
custom_math = importlib.util.module_from_spec(spec)
spec.loader.exec_module(custom_math)

# Chamada da função sqrt do módulo math personalizado
custom_math.sqrt(9)