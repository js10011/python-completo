from PIL import Image, ImageDraw, ImageFont

# Carregar a imagem de fundo
background = Image.open("background.jpg")
draw = ImageDraw.Draw(background)

# Definir fontes
font_size_text = 60
font_size_watermark = 20
try:
    # Usar a fonte FreeType, se disponível
    font_text = ImageFont.truetype("arial.ttf", font_size_text)
    font_watermark = ImageFont.truetype("arial.ttf", font_size_watermark)
except IOError:
    # Caso não esteja disponível, usar a fonte padrão do PIL
    font_text = ImageFont.load_default()
    font_watermark = ImageFont.load_default()

# Tamanho da imagem
image_width, image_height = background.size

# Texto "Sale -50%"
text = "Sale -50%"
text_width, text_height = draw.textsize(text, font=font_text)
text_x = (image_width - text_width) / 2
text_y = 10  # Parte superior da imagem
draw.text((text_x, text_y), text, font=font_text, fill="black")

# Desenhar um oval amarelo ao redor do texto
oval_margin = 10
draw.ellipse(
    [(text_x - oval_margin, text_y - oval_margin),
     (text_x + text_width + oval_margin, text_y + text_height + oval_margin)],
    outline="yellow", width=5
)

# Desenhar uma seta vermelha apontando para o texto
arrow_start = (text_x + text_width / 2, text_y + text_height + oval_margin)
arrow_end = (text_x + text_width / 2, text_y + text_height + 100)  # Comprimento da seta
draw.line([arrow_start, arrow_end], fill="red", width=5)
draw.polygon([
    (arrow_end[0] - 10, arrow_end[1] - 20),
    arrow_end,
    (arrow_end[0] + 10, arrow_end[1] - 20)
], fill="red")

# Adicionar marca d'água "StoreName" no canto inferior esquerdo
watermark_text = "StoreName"
watermark_width, watermark_height = draw.textsize(watermark_text, font=font_watermark)
watermark_x = 10
watermark_y = image_height - watermark_height - 10
draw.text((watermark_x, watermark_y), watermark_text, font=font_watermark, fill="black")

# Salvar a imagem final
background.save("advertisement_banner.jpg")