from CD import CD
from Catalogo import CatalogoCDs 

album1 = CD("choraSertão",45,"xibinha","musicas para o coração chorar")
#album1.gerador_Trilhas()
#album1.imprime()
catalogo = CatalogoCDs()
catalogo.add_CD(album1)
print(catalogo.listar_cds())