from selenium import webdriver
from selenium.webdriver.common.by import By

# Criamos uma instância do driver do navegador
driver = webdriver.Chrome()

# Abrimos a página web
driver.get("http://example.com/articles")

# Procuramos todos os elementos com a classe "article-title"
article_titles = driver.find_elements(By.CLASS_NAME, "article-title")

# Extraímos e exibimos o texto de cada título
for title in article_titles:
    print(title.text)

# Fechamos o driver independentemente do resultado
driver.quit()