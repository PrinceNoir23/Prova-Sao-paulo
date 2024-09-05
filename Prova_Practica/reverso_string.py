# Função para inverter os caracteres de uma string
def inverter_string(s):
    return s[::-1]

# Solicitar ao usuário a string a ser invertida
string_original = input("Digite a string a ser invertida: ")
string_invertida = inverter_string(string_original)

print("String invertida:", string_invertida)
