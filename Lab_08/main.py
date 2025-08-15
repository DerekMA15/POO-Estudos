from Carro import Carro
from Moto import Moto 
from Bicicleta import Bicicleta

carro1 = Carro("GOL","WolvsWagen",2,"carro",4)
carro1.setNumrRodas(4)
carro1.som_Carro()
carro1.infoCarro()

#subclasse Carro implementada com sucesso. 

moto1 = Moto("Factor","Yamaha",2,"moto boa",125)
moto1.som_Moto()
moto1.infoMoto()

#subclasse Moto implementada com sucesso. 

bicicleta1 = Bicicleta("aro20", "OGI", 2,"bike boa", 20)
bicicleta1.som_Bicicleta()
bicicleta1.infoBicicleta()
