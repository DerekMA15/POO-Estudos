from random import randint
from Item import Item
class CD(Item): 
    def __init__(self,titulo:str,temp_reproducao:int,artista:str,comentarios:int):
        super().__init__(titulo,temp_reproducao,comentarios)
        self.__artista__ = artista
        self.__nmr_trilhas__ = 0 #nmr_trilhas
        self.gerador_Trilhas() # chamar o metodo para gerar as nmr de trilhas
    

    # Getter e Setter para temp_reprod
    def get_temp_reproducao(self):
        return self.__temp_reprod__
    def set_temp_reproducao(self, temp_reproducao):
        self.__temp_reprod__ = temp_reproducao

    # Getter e Setter para artista
    def get_artista(self):
        return self.__artista__
    def set_artista(self, artista):
        self.__artista__ = artista

    # Getter e Setter para nmr_trilhas
    def get_nmr_trilhas(self):
        return self.__nmr_trilhas__
    def set_nmr_trilhas(self, nmr_trilhas):
        self.__nmr_trilhas__ = nmr_trilhas

    # Getter e Setter para possuo
    def get_possuo(self):
        return self.__possuo__
    def set_possuo(self, possuo):
        self.__possuo__ = possuo

    # Getter e Setter para comentarios
    def get_comentarios(self):
        return self.__comentarios__
    def set_comentarios(self, comentarios):
        self.__comentarios__ = comentarios

    # Metodo Imprime
    def imprime(self):
        print("---------------------------CD----------------------------")
        print(self.get_titulo())#"Titulo: " +
        print(self.get_temp_reproducao()) #"Tempo de Reprodução: " +
        print(self.get_artista())#"Artista: " +
        print(self.get_nmr_trilhas())#"Número de Trilhas: "
        print(self.get_possuo())#"Possue :" + 
        print(self.get_comentarios())#"Comentarios :" + 
        print("--------------------------------------------------------\n")


    # Metodo gerador do nmr de trilhas
    def gerador_Trilhas(self):
       #self.set_nmr_trilhas(randint(1,10))
       self.__nmr_trilhas__= randint(1,10)