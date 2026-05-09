# Rebelde no máximo

# Corrija os recuos no seguinte código para que ele exiba corretamente o status dependendo da quantidade de pontos obtidos.

score = int(input("Digite a quantidade de pontos obtidos: "))
if score >= 90:
  print("Excelente")

if score >= 75 and score < 90:
    print("Bom")

if score >= 50 and score < 75:
    print("Satisfatório")

if score < 50:
    print("Insatisfatório")