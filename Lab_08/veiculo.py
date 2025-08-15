class Veiculo:
    def __init__ (self, modelo:str,fabricante:str,nmr_rodas:int,descricao:str):

        """ modelo do veículo, fabricante 
            do veículo, número de rodas do 
            veículo e descrição do veículo""" 
        
        self.__modelo__ = modelo
        self.__fabricante__ = fabricante
        self.__nmr_rodas__ = nmr_rodas
        self.__descricption__ = descricao

        """ Essa classe deve ser bem 
            projetada (com construtor, métodos acessadores, 
            métodos modificadores e método de impressão de 
            atributos (imprime(self))"""
        
    def getModelo(self):
        return self.__modelo__
    
    def getFabricante(self):
        return self.__fabricante__
    
    def getNumrRodas(self):
        return self.__nmr_rodas__
    
    def getDescricao(self):
        return self.__descricption__
    

    def setModelo(self,modelo):
        self.__modelo__ = modelo
    
    def setFabricante(self,fabricante):
       self.__fabricante__ = fabricante
    
    def setNumrRodas(self,nmr_rodas):
        self.__nmr_rodas__ = nmr_rodas
    
    def setDescricao(self,descricao):
        self.__descricption__ = descricao
    
    def infoGeral(self):
        #print(vars(Veiculo))
        print(self.getModelo())
        print(self.getFabricante())
        print(self.getNumrRodas())
        print(self.getDescricao())

    def __emite_som__(self,som:bool):
        print(som)

        """•Acrescente um método emite_som(self) que não 
            faz nada mas que deve ser implementado pelas 
            subclasses.
            """