class Professor: 
    def __init__(self):
        
        self.__nome = ""
        self.__matricula = 0
        self.__carga_horaria = 0
        

    #definir metodos get e set dos atributos do professor

    #getters
    def getNome(self):
        return self.__nome
    
    def getMatricula(self):
        return self.__matricula
    
    def getCarga_Horaria(self):
        return self.__carga_horaria
    
    #setters
    def setNome(self,name):
        self.__nome = name

    def setMatricula(self,numero):
        self.__matricula = numero
    
    def setCarga_Horaria(self,horas):
        self.__carga_horaria = horas
    
    #desenvolver dois métodos maisHoras e menosHoras

    def maisHoras(self,horas):
        self.__carga_horaria += horas
        
    
    def menosHoras(self,horas):
        self.__carga_horaria -= horas