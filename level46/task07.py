from PIL import Image, ImageDraw

# Abra a imagem de fundo
background = Image.open("background.jpg").convert("RGBA")

# Crie uma nova imagem com fundo transparente
overlay = Image.new("RGBA", (100, 100), (255, 255, 255, 0))

# Desenhe um quadrado vermelho semitransparente
draw = ImageDraw.Draw(overlay)
red_square_color = (255, 0, 0, 128)  # Vermelho semitransparente
draw.rectangle((10, 10, 90, 90), fill=red_square_color)

# Sobreposição da imagem no fundo
background.paste(overlay, (150, 150), overlay)

# Salve a imagem final
background.save("combined_image.png", "PNG")