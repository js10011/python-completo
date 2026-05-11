from PIL import Image, ImageFilter

# Abertura da imagem
input_image = Image.open("input.jpg")

# Aplicação do filtro de desfoque (BLUR)
blur_image = input_image.filter(ImageFilter.BLUR)
blur_image.save("output_blur.jpg")

# Aplicação do filtro de contorno (CONTOUR)
contour_image = input_image.filter(ImageFilter.CONTOUR)
contour_image.save("output_contour.jpg")

# Aplicação do filtro de aumento de nitidez (SHARPEN)
sharpen_image = input_image.filter(ImageFilter.SHARPEN)
sharpen_image.save("output_sharpen.jpg")