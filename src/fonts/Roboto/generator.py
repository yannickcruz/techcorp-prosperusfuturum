import os

# Caminho para a pasta das fontes
caminho_pasta = "./"

# Mapeamento de pesos da fonte
pesos = {
    "Thin": 100,
    "ExtraLight": 200,
    "Light": 300,
    "Regular": 400,
    "Medium": 500,
    "SemiBold": 600,
    "Bold": 700,
    "ExtraBold": 800,
    "Black": 900
}

# Criação do CSS
css = ""
for arquivo in os.listdir(caminho_pasta):
    if arquivo.endswith(".ttf"):
        nome = arquivo.replace(".ttf", "")
        partes = nome.split("-")
        
        peso = 400  # Padrão Regular
        estilo = "normal"

        for key in pesos:
            if key in nome:
                peso = pesos[key]
        
        if "Italic" in nome:
            estilo = "italic"
        
        css += f"""
@font-face {{
    font-family: 'Roboto';
    src: url('{caminho_pasta}{arquivo}') format('ttf');
    font-weight: {peso};
    font-style: {estilo};
}}\n"""

# Salva no arquivo styles.css
with open("styles.css", "w", encoding="utf-8") as f:
    f.write(css)

print("Arquivo CSS gerado com sucesso!")
