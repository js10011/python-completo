module_name = input("Digite o nome do módulo: ")
function_name = input("Digite o nome da função: ")

module = __import__(module_name)
function = getattr(module, function_name)

function(1)