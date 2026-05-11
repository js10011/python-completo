popular_cat_names = {"Barcik", "Murka", "Vaska", "Neve", "Murzik"}

attempts = 0

while popular_cat_names:
    guess = input("Adivinhe o nome de um gato: ")
    attempts += 1
    if guess in popular_cat_names:
        popular_cat_names.remove(guess)
        print(f"Certo! Restam {len(popular_cat_names)} nomes para adivinhar.")
    else:
        print("Errado. Tente novamente.")

print(f"Você adivinhou todos os nomes em {attempts} tentativas!")