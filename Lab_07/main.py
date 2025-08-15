from CD import CD 
from DVD import DVD
from Catalogo import Catalogo

cd1 = CD("Sertanejo Raiz", 50, "João Mineiro", "Ótimo para festas")
cd2 = CD("Rock Brasil", 40, "Legião Urbana", "Clássico dos anos 80")

dvd1 = DVD("Pop Hits", 60, "chucochuco", "Músicas animadas")
dvd2 = DVD("Jazz Night", 55, "Miles Davis", "Relaxante e sofisticado")

catalogo = Catalogo()

# Para testar:
#cd1.imprime()
#cd2.imprime()

#dvd1.imprime()
#dvd2.imprime()

catalogo.add_iten(cd1)
catalogo.add_iten(cd2)
catalogo.add_iten(dvd1)
catalogo.add_iten(dvd2)

catalogo.show_list()

catalogo.remove_list("Rock Brasil")

catalogo.show_list()
