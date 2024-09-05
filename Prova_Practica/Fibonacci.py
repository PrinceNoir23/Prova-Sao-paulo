# Como os termos de Fibonacci podem ser expressos por raízes quadradas devido à fórmula de Binet, existe uma relação interessante entre os termos da sequência e certas formas quadráticas. A sequência de Fibonacci tem a propriedade de que, se um número x pertencer a ela, então um dos dois números a seguir:

# 5 * x**2 - 4 ou 5 * x**2 + 4

# será um quadrado perfeito
import math



def check_integers(y, y1):
    if y == int(y) or y1 == int(y1):
        return "Pertence"
    else:
        return "No Pertence"
x = int(input("Digite o número que deseja verificar se é da sequência de Fibonacci: "))
y = math.sqrt(5 * x**2 - 4)
y1 = math.sqrt(5 * x**2 + 4)
print(check_integers(y, y1))
