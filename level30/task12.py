"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Example Page</title>
    <style>
        /* Seletor de irmãos generalizados para alterar a cor dos parágrafos após o título <h1> */
        h1 + p {
            color: gray;
        }

        /* Seletor de irmãos generalizados para todos os parágrafos que seguem o título <h1> */
        h1 ~ p {
            color: gray;
        }

        /* Seletor filho para itálico dos itens de lista no <div> interno */
        #inner-div > ul > li {
            font-style: italic;
        }
    </style>
</head>
<body>
    <h1>Principal Título</h1>
    <p>O primeiro parágrafo após o h1 deve ser cinza.</p>
    <p>O segundo parágrafo também será cinza se seguir o h1.</p>
    <div id="outer-div">
        <div id="inner-div">
            <ul>
                <li>Primeiro item da lista</li>
                <li>Segundo item da lista</li>
                <li>Terceiro item da lista</li>
            </ul>
        </div>
    </div>
</body>
</html>"""