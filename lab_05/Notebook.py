
import random

class Notebook:

    def __init__(self):
        self.__notes = list()

    def storeNote(self,note):
        self.__notes.append(note)
    
    def numberOfNotes(self):
        return len(self.__notes) 

    def showNote(self,noteNumber):
        if noteNumber < 0:
            print("Este não é um número de nota válido")

        elif noteNumber < self.numberOfNotes():
            return(self.__notes[noteNumber])

        else :
            print("Este não é um número de nota válido")
    
    def removeNote(self, note):
        if note in self.__notes:
            self.__notes.remove(note)

        else:
            print("Esta não é uma nota válida") 

    def listNotes(self):
        index = 0
        while index < self.numberOfNotes():
            print(self.__notes[index])
            index += 1

    def listNotesfor(self):
        for nota in self.__notes:
            print(nota)
    
    def hasNotes(self):
        if self.numberOfNotes() == 0:
            return False
        else:
            return True
        
    def CompareNote(self,nota):
        if nota in self.__notes: 
            return True
        else:
            return False
        
    def showNoteRandom(self):
       return random.randint(0,len(self.__notes))

    def showMultNoteRandom(self,x):
        while(x != 0):
            print(self.showMultNoteRandom())
            x -= 1
     