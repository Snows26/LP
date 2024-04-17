def msg():
    print("QUAL SERIA OS NUMEROS A CALCULAR?")

def soma(a, b):
    result = print(a + b)
    return result

def sub(a, b):
    result = print(a - b)
    return result

def mult(a, b):
    result = print(a * b)
    return result

def div(a, b):
    result = print(a / b)
    return result

def layout(value):

    while value != 5:

        value = int(input("BEM VINDO A CALCULADORA! \n 1- SOMA \n 2- SUBTRAÇÃO \n 3- MULTIPLICAÇÃO \n 4- DIVISÃO \n 5- FECHAR \n"))

        if(value == 1): 
            msg()
            val1 = int(input("Valor 1: "))
            val2 = int(input("Valor 2: "))
            soma(val1, val2)
            layout(0)

        elif(value == 2): 
            msg()
            val1 = int(input("Valor 1: "))
            val2 = int(input("Valor 2: "))
            sub(val1, val2)
            layout(0)

        elif(value == 3): 
            val1 = int(input("Valor 1: "))
            val2 = int(input("Valor 2: "))
            mult(val1, val2)
            layout(0)

        elif(value == 4): 
            val1 = int(input("Valor 1: "))
            val2 = int(input("Valor 2: "))
            div(val1, val2)
            layout(0)

        else:
            print("DESLIGANDO...")
        break

layout(0)