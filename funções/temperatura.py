def celsius_para_fahrenheit(celsius):
    return (celsius * 9/5) + 32


def fahrenheit_para_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9


def menu():
    print("Escolha uma opção:")
    print("1. Celsius para Fahrenheit")
    print("2. Fahrenheit para Celsius")
    opcao = int(input("Opção: "))
    return opcao


opcao = menu()


if opcao == 1:
    celsius = float(input("Digite a temperatura em Celsius: "))
    print("Temperatura em Fahrenheit:", celsius_para_fahrenheit(celsius))
elif opcao == 2:
    fahrenheit = float(input("Digite a temperatura em Fahrenheit: "))
    print("Temperatura em Celsius:", fahrenheit_para_celsius(fahrenheit))
else:
    print("Opção inválida")
