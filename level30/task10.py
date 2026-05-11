"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Child Selector Example</title>
    <style>
        /* Seletor de elemento filho para alteração de estilo de texto */
        div > p {
            font-weight: bold;
        }
    </style>
</head>
<body>
    <div>
        <p>Este parágrafo é um descendente direto do div externo e deve estar em negrito.</p>
        <div>
            <p>Este parágrafo está dentro do div aninhado e não deve ser afetado pelo estilo de negrito.</p>
        </div>
    </div>
</body>
</html>"""