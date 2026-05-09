height_cm = float(input("Digite a altura em centímetros: "))

# Constantes
cm_per_inch = 2.54
inch_per_foot = 12

# Conversão de centímetros para polegadas
height_inch = height_cm / cm_per_inch

# Cálculo do número de pés completos
feet = int(height_inch // inch_per_foot)

# Cálculo do restante em polegadas
inches = height_inch % inch_per_foot

# Exibição do resultado
print(feet, "pés", inches, "polegadas")


total_grains = 2**64 - 1
print(total_grains)