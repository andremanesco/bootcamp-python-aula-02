import math
from datetime import datetime

# #### Inteiros (`int`)

def valida_input(prompt):
    while True:
        num = input(prompt)
        try:
            return int(num)
        except ValueError:
            print("⚠️ Você inseriu um valor inválido, tente novamente!")

# 1. Escreva um programa que soma dois números inteiros inseridos pelo usuário.
print("\n 🟢 Exercício 1: Soma de Números Inteiros")

n1 = valida_input("Digite o primeiro número: ")
n2 = valida_input("Digite o segundo número: ")

soma = n1 + n2

print(f"🔹 A soma dos valores é: {soma}")

# 2. Crie um programa que receba um número do usuário e calcule o resto da divisão desse número por 5.
print("\n 🟢 Exercício 2: Cálculo resto da divisão")

numero = valida_input("Digite um número: ")

resto = numero % 5

print(f"🔹 O resto da divisão desse número por 5 é: {resto}")


# 3. Desenvolva um programa que multiplique dois números fornecidos pelo usuário e mostre o resultado.
print("\n 🟢 Exercício 3 - Multiplicação de dois números")

n1 = valida_input("Digite o primeiro número: ")
n2 = valida_input("Digite o segundo número: ")

resultado = n1 * n2

print(f"🔹 O resultado da multiplicação de {n1}x{n2} é: {resultado}")

# 4. Faça um programa que peça dois números inteiros e imprima a divisão inteira do primeiro pelo segundo.
print("\n 🟢 Exercício 4 - Parte inteira da divisão entre dois números")

n1 = valida_input("Digite o primeiro número: ")
n2 = valida_input("Digite o segundo número: ")

resultado = n1 // n2

print(f"🔹 O resultado da inteiro da divisão de {n1} por {n2} é: {resultado}")


# 5. Escreva um programa que calcule o quadrado de um número fornecido pelo usuário.
print("\n 🟢 Exercício 5 - Quadrado de um número")

num = valida_input("Digite um número: ")

resultado = num**2

print(f"🔹 O resultado de {num}^2 é: {resultado}")


# #### Números de Ponto Flutuante (`float`)
def valida_float(prompt):
    while True:
        num = input(prompt)

        try:
            return float(num)
        except ValueError:
            print("⚠️ Você digitou um valor inválido, tente novamente!")

# 6. Escreva um programa que receba dois números flutuantes e realize sua adição.
print("\n 🟢 Exercício 6 - Adição de dois número float")

n1 = valida_float("Digite o primeiro número: ")
n2 = valida_float("Digite o segundo número: ")

soma = n1 + n2

print(f"🔹 A soma de {n1} + {n2} é: {soma}")


# 7. Crie um programa que calcule a média de dois números flutuantes fornecidos pelo usuário.
print("\n 🟢 Exercício 7 - Média entre dois números")

n1 = valida_float("Digite o primeiro número: ")
n2 = valida_float("Digite o segundo número: ")

media = (n1 + n2) / 2

print(f"🔹 A média entre {n1} e {n2} é: {media}")

# 8. Desenvolva um programa que calcule a potência de um número (base e expoente fornecidos pelo usuário).
print("\n 🟢 Exercício 8 - Cálculo de potência de dois números")

base = valida_float("Digite o primeiro número: ")
expoente = valida_float("Digite o segundo número: ")

potencia = base ** expoente

print(f"🔹 O resultado de {base} ^ {expoente} é: {potencia}")

# 9. Faça um programa que converta a temperatura de Celsius para Fahrenheit.
print("\n 🟢 Exercício 9 - Conversão de Temperatura")

celsius = valida_float("Digite a temperatura em graus celsius: ")

fahrenheit = (1.8 * celsius) + 32

print(f"🔹 {celsius}ºC --> {fahrenheit:.1f}ºF")

# 10. Escreva um programa que calcule a área de um círculo, recebendo o raio como entrada.
print("\n 🟢 Exercício 10 - Área do Círculo")

raio_do_circulo = valida_float("Digite o valor do raio: ")

area_do_circulo = math.pi * raio_do_circulo ** 2

area_do_circulo_formatada = "{:.2f}".format(area_do_circulo)

print(f"{area_do_circulo:.2f}")

# #### Strings (`str`)

# 11. Escreva um programa que receba uma string do usuário e a converta para maiúsculas.
print("\n 🟢 Exercício 11 - Upper case")

texto = input("Digite um texto: ")

texto_formatado = texto.upper()

print(f"🔹 Texto formatado: {texto_formatado}")

# 12. Crie um programa que receba o nome completo do usuário e imprima o nome com todas as letras minúsculas.
print("\n 🟢 Exercício 12 - Lower case")

texto = input("Digite um texto: ")

texto_formatado = texto.lower()

print(f"🔹 Texto formatado: {texto_formatado}")


# 13. Desenvolva um programa que peça ao usuário para inserir uma frase e, em seguida, imprima esta frase sem espaços em branco no início e no final.
print("\n 🟢 Exercício 13 - Remoção de espaços")

texto = input("Digite um texto: ")

texto_formatado = texto.strip()

print(f"🔹 Texto formatado: {texto_formatado}")


# 14. Faça um programa que peça ao usuário para digitar uma data no formato "dd/mm/aaaa" e, em seguida, imprima o dia, o mês e o ano separadamente.
print("\n 🟢 Exercício 14 - Separando ano, mês e dia de uma data")

while True:
    data = input("Digite uma data no formato yyyy/mm/dd: ")
    try:
        formatted_date = datetime.strptime(data, "%Y/%m/%d").date()
        break
    except ValueError:
        print("A data digitada não está no formato correto, tente novamente.")

dia = formatted_date.day
mes = formatted_date.month
ano = formatted_date.year

print(f"🔹 Data: {formatted_date}")
print(f"🔹 Dia: {dia}")
print(f"🔹 Mês: {mes}")
print(f"🔹 Ano: {ano}")


# 15. Escreva um programa que concatene duas strings fornecidas pelo usuário.


# #### Booleanos (`bool`)

# 16. Escreva um programa que avalie duas expressões booleanas inseridas pelo usuário e retorne o resultado da operação AND entre elas.
print("\n 🟢 Exercício 16 - Operação AND entre booleanos")

bol1 = input("Digite o primeiro Boolean: ")
bol2 = input("Digite o segundo Boolean: ")

resultado = bol1 and bol2

print("Resultado do AND lógico:", resultado)

# 17. Crie um programa que receba dois valores booleanos do usuário e retorne o resultado da operação OR.
print("\n 🟢 Exercício 17 - Operação OR entre booleanos")

bol1 = input("Digite o primeiro Boolean: ")
bol2 = input("Digite o segundo Boolean: ")

resultado = bol1 or bol2

print("Resultado do OR lógico:", resultado)


# 18. Desenvolva um programa que peça ao usuário para inserir um valor booleano e, em seguida, inverta esse valor.
print("\n 🟢 Exercício 18 - Inversão de boolean")

bol = input("Digite o Boolean: ")

inv_bool = not bol

resultado = inv_bool

print("Resultado do AND lógico:", resultado)

# 19. Faça um programa que compare se dois números fornecidos pelo usuário são iguais.
print("\n 🟢 Exercício 19 - Verifica números iguais")

n1 = valida_input("Digite o primeiro número: ")
n2 = valida_input("Digite o segundo número: ")

result = n1 == n2

print(f"Resultado da igualdade: {result}")

# 20. Escreva um programa que verifique se dois números fornecidos pelo usuário são diferentes.
print("\n 🟢 Exercício 20 - Verifica números diferentes")

n1 = valida_input("Digite o primeiro número: ")
n2 = valida_input("Digite o segundo número: ")

result = n1 != n2

print(f"Resultado da diferença: {result}")

# #### try-except e if

# 21: Conversor de Temperatura
# 22: Verificador de Palíndromo
# 23: Calculadora Simples
# 24: Classificador de Números
# 25: Conversão de Tipo com Validação