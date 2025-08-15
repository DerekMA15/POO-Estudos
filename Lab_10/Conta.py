class Conta:
    def __init__(self,nome:str,nmr_conta:int):
        self.__nome__ = nome
        self.__nmr_conta__ = nmr_conta
        self.__saldo__ = 0 # mudar para string e trabalhar com conversão
        self.__conta_ativa__ = True

    # dois metodos publicos para um para depositos e outro para saques

    def deposito(self,valor:int): #usar o tratamento de exceções ara evitar o deposito de quantias negativas
    
        while True:
            try:
                valor = int(input("Digite um novo valor (positivo): "))

                if valor >= 0:
                    raise ValueError("O valor deve ser positivo.")
                
                if not isinstance(valor,(int)):
                    raise TypeError("valor deve ser inteiro.")
                
                self.setSaldo_DEPOSITO(valor)
                return "Valor depositado com sucesso."
            
            except ValueError:
                return "Depósito não realizado. Valor inserido não reconhecido."
            
            except:
                return "Tipo inválido, tente novamente."
            
    def saque(self,valor:int):  #usar o tratamento de exceções ara evitar o saque de quantias maiores que as disponiveis na conta bancaria
       while True:
                try :
                    #valor = int(input(" Digite novo valor: "))
                    # self.__saque__ -= valor primeira forma de aplicar, mas são métodos privados 
                    # return "valor Sacado" + " seu saldo é: "+ self.getSaldo()

                    if valor <= 0:  
                        raise ValueError ("Valor não aceito para saque.")
                    
                    if valor > self.getSaldo:
                        raise ValueError ("Não tem o atual valor em seu Saldo.")
                    
                    if not isinstance(valor(int)):
                        raise TypeError ("Tipo Invalido")

                    self.setSaldo_SAQUE(valor)

                    return "Valor sacado de sua carteira. "
                
                except  :
                    return "Deposito não realizado, valor inserido não reconhecido." 

    def getSaldo(self):
        return self.__saldo__
    
    def setSaldo(self,valor:int):
         self.__saldo__ += valor

    def setSaldo_SAQUE(self,valor:int):
         self.__saldo__ -= valor

    def setSaldo_DEPOSITO(self,valor:int):
         self.__saldo__ += valor

    def getNome(self):
        return self.__nome__
    
    def setNome(self,nome:str):
        self.__nome__ = nome