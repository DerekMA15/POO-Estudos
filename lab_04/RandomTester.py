import random as rd
class RandomTester:
    def __init__(self):
        None


    #print um valor aleatorio
    def printOnRandom(self):   
        return rd.randrange(10)

    def multiRandom(self,x):
        array =[]
        for _ in range(x):
             array.append(self.printOnRandom())
        return array  
   
    def throwDice(self):
       return rd.randint(1,6)
    
    def max(self,x):
       return rd.randint(1,x)
    
    def minMax(self,min,max):
        return rd.randint(min,max)

    def toMax(self,max):
        return self.minMax(1,max)
            