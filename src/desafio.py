
# Escreva um programa em Python que solicita ao usuário para digitar seu nome, o valor do seu salário mensal e o valor do bônus que recebeu. O programa deve, então, imprimir uma mensagem saudando o usuário pelo nome e informando o valor do salário em comparação com o bônus recebido.

constante_bonus = 1000

print("🎉 Bem-vindo ao programa que irá te ajudar a calcular o valor do seu bônus!")

while True:
    nome = input("Digite o seu nome: ")
    if any(char.isdigit() for char in nome):
        print("❌ Erro: O nome não pode conter um caractere numérico.")
    elif len(nome.strip()) == 0:
        print("❌ Erro: O nome não pode ficar em branco.")
    else:
        break

print(f"✋🏼 Olá {nome}! Preciso de algumas informações para calcular o seu bônus.")

while True:
    salario = input("Digite o valor do seu salário: ")
    
    try:
        int_salario = int(salario)
        break
    except ValueError:
        print("Você digitou valor não válido, tente novamente!")

while True:
    per_bonus = input("Digite o Valor percentual do bônus: ")

    try:
        float_per_bonus = float(per_bonus)
        break
    except ValueError:
        print("Você digitou valor não válido, tente novamente!")

vlr_bonus = constante_bonus + (int_salario * float_per_bonus)

print(f"{nome}, o valor do seu bônus foi de {vlr_bonus}")