"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Exemplo de Seletor de Irmão Adjacente</title>
    <style>
        /* CSS seletor para mudar a cor do texto do parágrafo,
         que segue imediatamente após o cabeçalho */
        h1 + p {
            color: green;
        }
    </style>
</head>
<body>

    <h1>Cabeçalho 1</h1>
    <p>Parágrafo 1, seguindo o Cabeçalho 1.</p>
    
    <h1>Cabeçalho 2</h1>
    <p>Parágrafo 2, seguindo o Cabeçalho 2.</p>
    
    <h1>Cabeçalho 3</h1>
    <p>Parágrafo 3, seguindo o Cabeçalho 3.</p>
    
    <h1>Cabeçalho 4</h1>
    <p>Parágrafo 4, seguindo o Cabeçalho 4.</p>

</body>
</html>"""