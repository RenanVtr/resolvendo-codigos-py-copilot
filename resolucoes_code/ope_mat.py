# Vamos solicitar como entrada dois números e depois vamos realizar uma operação simples entre eles.

num1 = float(input("Digite primeiro numero: "))
operacao = input("Digite o tipo de operacao desejada (+,-,/,*): ")
num2 = float(input("Digite segundo numero: "))

match operacao:

    case "+":
        print( num1 + num2)
    case "-":
        print(num1 - num2)
    case "/":
        print(num1 / num2)
    case "*":
        print(num1 * num2)
    case _:
        print("Operador invaido")