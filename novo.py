def validar_numero(entrada):
    while not entrada.isdigit():
        entrada = input("Por favor, digite um valor numérico válido: ")
    return float(entrada)

def validar_texto(entrada):
    while not entrada.isalpha():
        entrada = input("Por favor, digite um valor de texto válido: ")
    return entrada

def calcular_contracheque():
    nome = validar_texto(input("Digite seu nome: "))
    salario = validar_numero(input("Digite seu salário: "))
    hora_extra = validar_numero(input("Digite as horas extras trabalhadas: "))
    setor = validar_texto(input("Digite seu setor (adm ou operacional): "))

    if hora_extra > 4:
        saldo_banco_hora = hora_extra - 4
        hora_extra = 4
    else:
        saldo_banco_hora = 0

    valor_hora_extra = 4.50 if setor.lower() == "adm" else 3.50
    salario_atualizado = salario + (hora_extra * valor_hora_extra)

    print("\nResumo:")
    print(f"Nome: {nome}")
    print(f"Salário Atualizado: R${salario_atualizado:.2f}")
    print(f"Banco de Horas: {saldo_banco_hora} horas")

calcular_contracheque()