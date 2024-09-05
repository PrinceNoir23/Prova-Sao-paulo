SP = 67836.43
RJ = 36678.66
MG = 29229.88
ES = 27165.48
OUTROS = 19849.53

# Crear un diccionario con los nombres y valores
estados = {
    'SP': SP,
    'RJ': RJ,
    'MG': MG,
    'ES': ES,
    'OUTROS': OUTROS
}

total = sum(estados.values())

for nombre, valor in estados.items():
    porcentual = valor * 100 / total
    print(f"{nombre}: {porcentual:.2f}%")


