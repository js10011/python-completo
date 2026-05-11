"""
<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Contêineres Estilizados</title>
    <style>
        /* Seletor de descendentes para alterar a cor do texto dos parágrafos no primeiro contêiner */
        .container1 p {
            color: red;
        }
    </style>
</head>
<body>
    <!-- Primeiro contêiner com vários parágrafos -->
    <div class="container1">
        <p>Parágrafo 1 no primeiro contêiner.</p>
        <div>
            <p>Parágrafo aninhado no primeiro contêiner.</p>
        </div>
        <p>Parágrafo 2 no primeiro contêiner.</p>
    </div>

    <!-- Segundo contêiner com vários parágrafos -->
    <div class="container2">
        <p>Parágrafo 1 no segundo contêiner.</p>
        <div>
            <p>Parágrafo aninhado no segundo contêiner.</p>
        </div>
        <p>Parágrafo 2 no segundo contêiner.</p>
    </div>
</body>
</html>
"""