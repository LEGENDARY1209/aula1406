# Calculadora Simples em Python

def dividir(a, b):
    if b == 0:
        return "Erro: Divisão por zero!"
    return a / b

def multiplicar(a, b):
    return a * b

def modulo(a, b):
    if b == 0:
        return "Erro: Divisão por zero!"
    return a % b

def subtrair(a, b):
    return a - b

def menu():
    print("Selecione a operação:")
    print("1. Divisão")
    print("2. Multiplicação")
    print("3. Resto Inteiro (Módulo)")
    print("4. Subtração")
    print("5. Sair")

while True:
    menu()
    escolha = input("Digite a escolha (1/2/3/4/5): ")

    if escolha == '5':
        print("Encerrando o programa.")
        break

    try:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
    except ValueError:
        print("Entrada inválida! Por favor, insira números válidos.")
        continue

    if escolha == '1':
        print(f"Resultado: {dividir(num1, num2)}")
    elif escolha == '2':
        print(f"Resultado: {multiplicar(num1, num2)}")
    elif escolha == '3':
        print(f"Resultado: {modulo(num1, num2)}")
    elif escolha == '4':
        print(f"Resultado: {subtrair(num1, num2)}")
    else:
        print("Opção inválida!")
