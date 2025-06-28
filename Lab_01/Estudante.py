class Estudante:
    #Atributos:
    #nome do estudante
    #a matricula
    #o número de créditos 
    def __init__(self,nome, matricula):
        self.__nome = nome
        self.__matricula = matricula
        self.__credito = 0
    #getters
    def getNome(self):
        return self.__nome
    def getMatricula(self):
        return self.__matricula
    def getCreditos(self):
        return self.__credito
    
    #definir método para adicionar mais créditos
    def addCredito(self,credito):
        self.__credito += credito

    #definir método para alterar o nome do estudante 
    def mudarNome(self,novo_nome):
        self.__nome = novo_nome
