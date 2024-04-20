class Imovel(object):
    __inscricao = 0
    __area = 0.0
    valor_m2 = 0.0

    def __init__(self, inscricao, area, valorm2): 
        self.__inscricao = inscricao
        self.__area = area
        self.__valor_m2 = valorm2

    def calcularIPTU(self): 
        return self.__area * self.__valor_m2
    
    def exibir(self): 
        return f"IPTU: R${Imovel.calcularIPTU(self):.2f}"
    
class Casa(Imovel):
    __area_construida = 0.0
    __taxa_construcao = 0.0

    def __init__(self, inscricao, area, valorm2, construida, construcao):
        super().__init__(inscricao, area, valorm2)
        self.__area_construida = construida
        self.__taxa_construcao  = construcao

    def calcularIPTU(self):
        return super().calcularIPTU() + self.__area_construida * self.__taxa_construcao
    
    def exibir(self):
        return f"Com os acrescimos o seu IPTU fica em R${Casa.calcularIPTU(self):.2f}"


    
ins = int(input("Qual é a sua inscrição? "))
are = float(input("Qual é a area do seu imovel? "))
ins = float(input("Qual é o valor por metro quadrado da sua localidade? "))
pai = Imovel(ins, are, ins)
print(pai.exibir())

taxa = input("Gostaria de saber com o acrescimo das taxas de construção? \n -(RESPONDA COM SIM OU NÃO)- \n")

if taxa == "SIM" or taxa == "Sim" or taxa == "sim":
    constru = float(input("Qual foi a area construida? "))
    taxcons = float(input("Qual é o taxa de consrução da sua localidade? "))
    filho = Casa(ins, are, ins, constru, taxcons)
    print(filho.exibir())
elif taxa == "NÃO" or taxa == "NAO" or taxa == "Não" or taxa == "Nao" or taxa == "não" or taxa == "nao":  
    print("Fechando...")
else:
    print("ERRO!")


