#desenvolver um programa main e testar os métodos 
from Professor import Professor

prof_01 = Professor()

#atribuindo valores aos atributos através dos setters 
prof_01.setNome("Paulo")
prof_01.setMatricula(1)
prof_01.setCarga_Horaria(8)
#(poderia ter feito um construct e colocar tudo isso dentro de um unico método para evitar tantas linhas)

#imprimir os get
print(prof_01.getNome())
print(prof_01.getMatricula())
print(prof_01.getCarga_Horaria())

#Mais Horas out = 16
prof_01.maisHoras(8)
print(prof_01.getCarga_Horaria())

#Menos Horas out = 12
prof_01.menosHoras(4)
print(prof_01.getCarga_Horaria())