from CD import CD
class CatalogoCDs: 
    def __init__(self):
        self.__Cds__ = []

    # adicionar CDs
    def add_CD(self, CD:CD):
        self.__Cds__.append(CD)
    
    def rmvr_CD(self, titulo):
        self.cds = [ CD for CD in self.__Cds__ if CD.get_titulo() != titulo]

    def listar_cds(self):
        for CD in self.__Cds__:
            CD.imprime()

    def existeCds(self):
        if len(self.__Cds__) > 0 : 
            return True # Existe
        else :
            return False # Não existe 
        
    def pesquisarCD(self,titulo):
        for CD in self.__Cds__:
            if CD.get_titulo() == titulo:
                CD.imprime()
                break 
            else:
                return False # CD não existe na lista
    def listarCdsPossuo(self):
        sublista  = self.__Cds__
        sublista = [ CD for CD in sublista if CD.get_possuo() == True]