list = (23,43,67,19,55)

pos = int(input("DIGITE UMA POSIÇÃO: "))

try:
    print(f"Possui o valor {list[pos]} na posição {pos}")
except:
    print("Digite um numero de 0 a 4")