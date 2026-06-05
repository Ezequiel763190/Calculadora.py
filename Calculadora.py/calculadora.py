import os
import math

def calculadora():

    print("\n--------- CALCULADORA ---------")

    while True:
        print("\nDivisão = /")
        print("Multiplicação = *")
        print("Soma = +")
        print("Subtração = -")
        print("Potência = **")
        print("Resto da divisão = %")
        print("Raiz quadrada = raiz")
        print("Limpar tela = limpar")

        operador = input("Escolha uma operação: ").lower()

        if operador == "limpar":
            os.system("cls" if os.name == "nt" else "clear")
            continue

        if operador == "raiz":
            try:
                n1 = float(input("Digite um número: "))

                if n1 < 0:
                    print("Não existe raiz quadrada real de número negativo!")
                    continue

                resultado = math.sqrt(n1)
                print("Resultado:", resultado)

            except ValueError:
                print("Digite apenas números!")
                continue

        else:
            try:
                n1 = float(input("Escolha o primeiro número: "))
                n2 = float(input("Escolha o segundo número: "))

            except ValueError:
                print("Digite apenas números!")
                continue

            if operador == "/":
                if n2 == 0:
                    print("Não é possível dividir por zero!")
                    continue
                resultado = n1 / n2

            elif operador == "*":
                resultado = n1 * n2
            elif operador == "-":
                resultado = n1 - n2
            elif operador == "+":
                resultado = n1 + n2
            elif operador == "**":
                resultado = n1 ** n2
            elif operador == "%":
                if n2 == 0:
                    print("Não é possível dividir por zero!")
                    continue
                resultado = n1 % n2

            else:
                print("Operação inválida!")
                continue

            print("Resultado:", resultado)

        while True:
            resposta = input("Deseja realizar outra operação? (Sim/Não): ")

            if resposta.lower() == "sim":
                break

            elif resposta.lower() == "não" or resposta.lower() == "nao":
                print("Calculadora encerrada!")
                return

            else:
                print("Não entendi, digite apenas Sim ou Não.")

calculadora()