from CD import CD
from DVD import DVD
from Item import Item 

class Catalogo:
    def __init__(self):
        self.__catalogo_Itens__ = []
    
    def add_iten(self,iten:Item):
        self.__catalogo_Itens__.append(iten)

    def show_list(self):
        for iten in self.__catalogo_Itens__:
            iten.imprime()
    
    def remove_list(self,titulo):
        self.__catalogo_Itens__ = [Item for Item in self.__catalogo_Itens__ if Item.get_titulo() != titulo]
    
    def existeItem(self):
        if len(self.__catalogo_Itens__) > 0:
            return True
        else:
            return False
    
    def pesquisaItem(self,titulo):
        for Item in self.__catalogo_Itens__:
            if Item.get_titulo == titulo:
                return True # Existe
        return False # Não Existe