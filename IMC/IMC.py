def validar_numero(entrada):
    while not entrada.isdigit():
        entrada = input("Por favor, digite um valor numérico válido: ")
    return float(entrada)

def validar_texto(entrada):
    while not entrada.isalpha():
        entrada = input("Por favor, digite um valor de texto válido: ")
    return entrada

def calcular_contracheque():
    nome = validar_texto (input("Digite seu nome: "))
    idade = validar_numero (input("digite sua idade: "))
    peso = validar_numero (input("Digite seu peso: "))
    altura = validar_numero (input("Digite sua altura: "))

