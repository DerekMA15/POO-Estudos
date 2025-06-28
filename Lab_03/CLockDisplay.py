from NumberDisplay import NumberDisplay

class ClockDisplay: 
    def __init__(self): 
        self.__hours = NumberDisplay(24) 
        self.__minutes = NumberDisplay(60) 
        self.__seconds = NumberDisplay(60)
        self.__updateDisplay() 

    def __updateDisplay(self): 
        #Atualiza a string interna que representa o mostrador.
        self.__displayString = self.__hours.getDisplayValue() + ':' + self.__minutes.getDisplayValue()  + ':' +  self.__seconds.getDisplayValue()
    
    def timeTick(self):
        #segundos
        self.__seconds.increment()
        if self.__seconds.getValue() == 0:  
           #minutos
            self.__minutes.increment()
            if self.__minutes.getValue() == 0:
                    #horas
                    self.__hours.increment() 
        self.__updateDisplay()
    
    def getDisplay(self):
        return self.__displayString


