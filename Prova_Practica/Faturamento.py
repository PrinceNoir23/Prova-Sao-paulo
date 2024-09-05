import json

# Carregar os dados do arquivo .JSON
with open('dados.json') as archivo:
    datos = json.load(archivo)









# cálculo de valores máximos e mínimos
valor_maximo = max(registro['valor'] for registro in datos if registro['valor'] > 0)
valor_minimo = min(registro['valor'] for registro in datos if registro['valor'] > 0)

# acrescente que se não for um número, não some, para evitar erros
media = [registro['valor'] for registro in datos if registro['valor'] > 0.0 and isinstance(registro['valor'], float)]
media = sum(media)/len(media)
 
# Días com valor igual a 0
dias_con_zeros = [registro['dia'] for registro in datos if registro['valor'] == 0.0]

# Procurar valores maximos e minimos
dias_minimo = [registro['dia'] for registro in datos if registro['valor'] == valor_minimo]
dias_maximo = [registro['dia'] for registro in datos if registro['valor'] == valor_maximo]
maior_a_media = [registro['dia'] for registro in datos if registro['valor'] > media]

print(f"O valor maximo é: {valor_maximo} no dia: {', '.join(map(str, dias_maximo))}")
print(f"O valor minimo é: {valor_minimo} no dia: {', '.join(map(str, dias_minimo))}")
print(f"Os dias sem faturamento são: {', '.join(map(str, dias_con_zeros))}, oseja {len(dias_con_zeros)} dias")
print(f"Os dias com faturamento diário foi superior à média mensal são: {', '.join(map(str, maior_a_media))}, oseja {len(maior_a_media)} dias")