from veiculo import Veiculo 
class Bicicleta(Veiculo):
    ''' Desenvolver a classe Bicicleta 
        modo que ela seja subclasse de Veiculo. 
        Adicionar os campos privados 
        exclusivos dessa subclasse, por 
        exemplo(número  de marchas para Bicicleta)'''
    
    def __init__(self, modelo:str,fabricante:str,nmr_rodas:int,descricao:str, nmr_marchas:int): 
        super().__init__(modelo,fabricante,nmr_rodas,descricao)#Chama a Classe Pai
        self.__nmr_marchas__ = nmr_marchas

    def getNumrMarchas(self):
        return self.__nmr_marchas__
    
    def setNumrCilindradas(self, numr_marchas:int):
        self.__nmr_marchas__ = numr_marchas
    
    def infoBicicleta(self):
        super().infoGeral()
        print(self.getNumrMarchas())
        print()
    
    def som_Bicicleta(self):
        print(super().__emite_som__(False))
