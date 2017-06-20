from Clasificadores import Clasificadores
from newspaper import Article

####### Realización de experimentos con documentos nuevos  ########

# print("Inserta la url de una noticia:", )
url = "http://www.abc.es/cultura/arte/abci-prado-y-thyssen-salen-armario-201706150132_noticia.html"
articulo = Article(url)
articulo.download()
articulo.parse()
#Obtenemos el texto del nuevo ejemplo de la siguiente forma:
nuevo_ejemplo = articulo.text


#Creamos un clasificador, que va a realizar el conjunto de entrenamiento de NB y KNN
clasificador = Clasificadores()


clfKNN = clasificador.KNN(doc=nuevo_ejemplo)
clfNB = clasificador.NB(doc=nuevo_ejemplo)

#Hemos creado en el caso de KNN un metodo iterativo para pasar una lista de urls
clasificador.Mostrar_predicciones(clfKNN,
                                  [
                                      'http://www.abc.es/economia/abci-bufetes-intentan-accionistas-bankia-vayan-juicio-201602190746_noticia.html',
                                      'http://www.elconfidencial.com/deportes/futbol/2016-02-19/torres-atletico-cope_1154857/',
                                      'http://sevilla.abc.es/deportes/alfinaldelapalmera/noticias/fichajes-betis/betis-pide-tres-millones-petros-130734-1497644020.html',
                                      'http://sevilla.abc.es/deportes/alfinaldelapalmera/noticias/fichajes-betis/betis-no-mas-ofertas-villamarin-130737-1497644996.html',
                                      'http://www.abc.es/cultura/arte/abci-crece-familia-duques-osuna-coleccion-prado-201706170138_noticia.html'
                                  ])
