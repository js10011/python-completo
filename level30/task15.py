"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Demostração de Seletor de Imagens</title>
    <style>
        /* Seletor CSS para imagens, cujo src começa com "image" e termina com ".jpg" */
        img[src^="image"][src$=".jpg"] {
            border: 3px solid red;
        }
    </style>
</head>
<body>
<h1>Demostração de Seletor de Imagens</h1>
<div>
    <img src="image1.jpg" alt="Imagem 1">
    <img src="image2.png" alt="Imagem 2">
    <img src="photo3.jpg" alt="Foto 3">
    <img src="image4.jpeg" alt="Imagem 4">
    <img src="image5.jpg" alt="Imagem 5">
    <img src="icon6.gif" alt="Ícone 6">
    <img src="drawing7.svg" alt="Desenho 7">
</div>
</body>
</html>"""