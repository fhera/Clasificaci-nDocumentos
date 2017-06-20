import Genera_documentos
from io import open
import Docs
from Clasificadores import Clasificadores
from newspaper import Article
from collections import Counter

############# Generador de documentación ############
# 4.3 Obtener un conjunto de textos de entrenamiento (y de test)
# Genera_documentos.Genera_documentos()


############# Clase Documentos #################
# doc = Docs.Docs()

# doc.documentos_csv()
# print("Listamos las palabras de los documentos:\n", doc.lista_palabras())
# print("Frecuencia de palabras en los docs:\n", doc.frecuencia())

# print(doc.vocabulario())
# print(doc.vocabulario_para_csv())
# print("Peso:\n", doc.peso())

### Metemos las frecuencias de palabras en un archivo ########
# frec=doc.frecuencia()
# file = open('frecuencia.txt', 'w', encoding='utf8')
# file.write(str(frec))
# file.close()


####### 4.7 Realización de experimentos  ########

url = "http://www.abc.es/cultura/arte/abci-prado-y-thyssen-salen-armario-201706150132_noticia.html"
articulo = Article(url)
articulo.download()
articulo.parse()
nuevo_ejemplo = articulo.text


###### Llamada a los métodos finales ######

clasificador = Clasificadores()
# clfKNN = clasificador.KNN(doc=nuevo_ejemplo)
# clfKNN = clasificador.KNN()
# clasificador.Mostrar_predicciones(clfKNN,
#                                   [
#                                       'http://www.abc.es/economia/abci-bufetes-intentan-accionistas-bankia-vayan-juicio-201602190746_noticia.html',
#                                       'http://www.elconfidencial.com/deportes/futbol/2016-02-19/torres-atletico-cope_1154857/',
#                                       'http://sevilla.abc.es/deportes/alfinaldelapalmera/noticias/fichajes-betis/betis-pide-tres-millones-petros-130734-1497644020.html',
#                                       'http://sevilla.abc.es/deportes/alfinaldelapalmera/noticias/fichajes-betis/betis-no-mas-ofertas-villamarin-130737-1497644996.html',
#                                       'http://www.abc.es/cultura/arte/abci-crece-familia-duques-osuna-coleccion-prado-201706170138_noticia.html'
#                                   ])

clasificador.NB(doc=nuevo_ejemplo)