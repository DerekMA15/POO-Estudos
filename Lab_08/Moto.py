from veiculo import Veiculo 
class Moto(Veiculo):
    ''' Desenvolver a classe Moto 
        modo que ela seja subclasse de Veiculo. 
        Adicionar os campos privados 
        exclusivos dessa subclasse, por 
        exemplo(número  de cilindradas para Moto)'''
    
    def __init__(self, modelo:str,fabricante:str,nmr_rodas:int,descricao:str, nmr_cilindradas:int): 
        super().__init__(modelo,fabricante,nmr_rodas,descricao)#Chama a Classe Pai
        self.__nmr_cilindradas__ = nmr_cilindradas

    def getNumrCilindradas(self):
        return self.__nmr_cilindradas__
    
    def setNumrCilindradas(self, numr_cilindradas:int):
        self.__nmr_portas__ = numr_cilindradas
    
    def infoMoto(self):
        super().infoGeral()
        print(self.getNumrCilindradas())
        print()

    def som_Moto(self):
        print(super().__emite_som__(True))