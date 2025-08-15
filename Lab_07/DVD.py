from Item import Item
class DVD(Item): 
    def __init__(self,titulo:str,temp_reproducao:int,diretor:str,comentarios:int):
        super().__init__(titulo,temp_reproducao,comentarios)
        self.__diretor__ = diretor

    # Getter e Setter para temp_reprod
    def get_temp_reproducao(self):
        return self.__temp_reprod__
    def set_temp_reproducao(self, temp_reproducao):
        self.__temp_reprod__ = temp_reproducao

    # Getter e Setter para artista
    def get_diretor(self):
        return self.__diretor__
    def set_artista(self, diretor):
        self.__diretor__ = diretor


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
        print("---------------------------DVD---------------------------")
        print(self.get_titulo())#"Titulo: " +
        print(self.get_temp_reproducao()) #"Tempo de Reprodução: " +
        print(self.get_diretor())#"Artista: " +
        print(self.get_possuo())#"Possue :" + 
        print(self.get_comentarios())#"Comentarios :" + 
        print("---------------------------------------------------------\n")
