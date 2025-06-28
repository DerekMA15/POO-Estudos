class NumberDisplay: 
    def __init__(self, rollOverLimit): 
        self.__limit = rollOverLimit 
        self.__value = 0 

    def increment(self): 
        self.__value = (self.__value + 1) % self.__limit 
    
    def getDisplayValue(self): 
        if(self.__value < 10): 
            return "0" + str(self.__value) 
        else: 
            return str(self.__value)
            
    def getValue(self):
        return self.__value
    
    def setValue(self, replacementValue):        
        if (replacementValue >= 0 and replacementValue < self.__limit):
            self.__value = replacementValue
            return True
        else:
            return False
