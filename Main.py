import Genera_documentos
from io import open
import Docs
from Clasificadores import Clasificadores
from newspaper import Article

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


####### 4.7 Realización de experimentos  ########

url = "http://www.abc.es/cultura/arte/abci-prado-y-thyssen-salen-armario-201706150132_noticia.html"
articulo = Article(url)
articulo.download()
articulo.parse()
nuevo_ejemplo = articulo.text

###### Llamada a los métodos finales ######

# clasificador = Clasificadores(2)
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



### Metemos las frecuencias de palabras en un archivo ########
# frec=doc.frecuencia()
# file = open('frecuencia.txt', 'w', encoding='utf8')
# file.write(str(frec))
# file.close()
import pandas
from sklearn import preprocessing
from sklearn import naive_bayes

docu = pandas.read_csv('Datos/documentos.csv', header=0)
########
le = preprocessing.LabelEncoder()  # Creamos un codificador de etiquetas
codificadores = []
docs_codificado = pandas.DataFrame()

for variable, valores in docu.iteritems():
    le = preprocessing.LabelEncoder()
    le.fit(valores)
    # print('Codificación de valores para {}: {}'.format(variable, le.classes_))
    codificadores.append(le)
    docs_codificado[variable] = le.transform(valores)



###############
ohe = preprocessing.OneHotEncoder(sparse=False)
datos_entrenamiento = docs_codificado.loc[:, 'arte':'isla']
datos_entrenamiento_nb = ohe.fit_transform(datos_entrenamiento)
clases_entrenamiento = docs_codificado['Categoria']

clasif_NB = naive_bayes.MultinomialNB(alpha=1.0)

clasif_NB.fit(datos_entrenamiento_nb, clases_entrenamiento)
###############

nuevo_ejemplo_codif = [le.transform([valor])
                       for valor, le in zip(nuevo_ejemplo, codificadores)]
nuevo_ejemplo_nb = ohe.transform(nuevo_ejemplo_codif)

print(clasif_NB.predict(nuevo_ejemplo_nb))