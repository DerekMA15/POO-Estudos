from veiculo import Veiculo 
class Carro(Veiculo):
    ''' Desenvolver a classe Carro 
        modo que ela seja subclasse de Veiculo. 
        Adicionar os campos privados 
        exclusivos dessa subclasse, por 
        exemplo(número de portas para Carro)'''
    
    def __init__(self, modelo:str,fabricante:str,nmr_rodas:int,descricao:str, nmr_portas:int): 
        super().__init__(modelo,fabricante,nmr_rodas,descricao)#Chama a Classe Pai
        self.__nmr_portas__ = nmr_portas 


    def getNumrPortas(self):
        return self.__nmr_portas__
    
    def setNumrPortas(self, numr_portas:int):
        self.__nmr_portas__ = numr_portas
    
    def infoCarro(self):
        super().infoGeral()
        print(self.getNumrPortas())
        print()
    
    def som_Carro(self):
        print(super().__emite_som__(True))