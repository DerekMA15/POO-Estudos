from random import randint

class Item : 
    def __init__(self,titulo:str,temp_reproducao:int,comentarios:int):
        self.__titulo__ = titulo
        self.__temp_reprod__ = temp_reproducao
        self.__comentarios__ = comentarios
        self.__possuo__ = True
        #self.__diretor__ = diretor
    
    # Getter e Setter para titulo
    def get_titulo(self):
        return self.__titulo__
    def set_titulo(self, titulo):
        self.__titulo__ = titulo

    # Getter e Setter para temp_reprod
    def get_temp_reproducao(self):
        return self.__temp_reprod__
    def set_temp_reproducao(self, temp_reproducao):
        self.__temp_reprod__ = temp_reproducao

    # Getter e Setter para artista
    #def get_diretor(self):
     #   return self.__artista__
    #def set_diretor(self, diretor:str):
     #   self.__artista__ = diretor

    # Getter e Setter para possuo
    def get_possuo(self):
        return self.__possuo__
    def set_possuo(self, possuo:bool):
        self.__possuo__ = possuo

    # Getter e Setter para comentarios
    def get_comentarios(self):
        return self.__comentarios__
    def set_comentarios(self, comentarios:str):
        self.__comentarios__ = comentarios

    # Metodo Imprime
    def imprime(self):
        print(self.get_titulo())#"Titulo: " +
        print(self.get_temp_reproducao()) #"Tempo de Reprodução: " +
        print(self.get_possuo())#"Possue :" + 
        print(self.get_comentarios())#"Comentarios :" + 