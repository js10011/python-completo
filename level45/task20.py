from PIL import Image, ImageEnhance, ImageFilter

def process_image(input_path, output_path):
    # Carregamento da imagem
    image = Image.open(input_path)
    
    # Conversão para preto e branco
    bw_image = image.convert("L")
    
    # Aplicação do filtro de nitidez
    sharp_image = bw_image.filter(ImageFilter.SHARPEN)
    
    # Aumento de brilho
    enhancer_brightness = ImageEnhance.Brightness(sharp_image)
    bright_image = enhancer_brightness.enhance(1.3)  # Aumento de brilho em 30%
    
    # Aumento de contraste
    enhancer_contrast = ImageEnhance.Contrast(bright_image)
    contrast_image = enhancer_contrast.enhance(1.5)  # Aumento de contraste em 50%
    
    # Salvamento da imagem final
    contrast_image.save(output_path)

# Definindo o caminho dos arquivos de entrada e saída
input_path = "input.jpg"
output_path = "output_final.jpg"

# Processamento da imagem
process_image(input_path, output_path)