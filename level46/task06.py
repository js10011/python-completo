from PIL import Image

def apply_mask(foreground_path, mask_path, output_path):
    # Carregar a imagem e a máscara
    foreground = Image.open(foreground_path).convert("RGBA")
    mask = Image.open(mask_path).convert("L")  # Escala de cinza

    # Redimensionar a máscara para que corresponda à imagem
    mask = mask.resize(foreground.size, Image.ANTIALIAS)

    # Aplicar a máscara ao canal alfa da imagem
    r, g, b, alpha = foreground.split()
    # Combinar RGB e máscara como canal alfa
    masked_image = Image.merge("RGBA", (r, g, b, mask))

    # Salvar a imagem resultante
    masked_image.save(output_path)

apply_mask("foreground.png", "mask.png", "masked_result.png")