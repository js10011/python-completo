import requests

# URL da primeira requisição AJAX, copiada da aba Network do DevTools
url = 'https://openweathermap.org/themes/openweathermap/assets/js/smart_banner_android.js' 

# Realizando a solicitação HTTP
response = requests.get(url)

# Exibindo o código de status da resposta
print("Código de status da resposta:", response.status_code)


import requests

# URL da primeira requisição AJAX, copiada da aba Network do DevTools
url = 'https://openweathermap.org/themes/openweathermap/assets/js/smart_banner_android.js' 

# Realizando a solicitação HTTP
response = requests.get(url)

# Exibindo o código de status da resposta
print("Código de status da resposta:", response.status_code)