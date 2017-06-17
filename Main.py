import Genera_documentos
from io import open
import Docs
import numpy as np
import csv
import pandas
import re
from newspaper import Article

############# Generador de documentación ############
# 4.3 Obtener un conjunto de textos de entrenamiento (y de test)
# genera = Genera_documentos.Genera_documentos()


############# Clase Documentos #################

doc = Docs.Docs()

# doc.documentos_csv()
# print("Listamos la¿s palabras de los documentos:\n", doc.lista_palabras())
# print("Frecuencia de palabras en los docs:\n", doc.frecuencia())

# print(doc.vocabulario())
# print(doc.vocabulario_para_csv())
## TODO Revisar método frecuencia_Documental hacia adelante
# print("Frecuencia docs:\n", doc.frecuencia_documental())
# print("Frecuencia docs inversa:\n", doc.frecuencia_documental_inversa())
# print("Peso:\n", doc.peso())


# Cuenta las palabras de la categoria indicada
# print(len(doc.lista_palabras()['Deportes']))



####### 4.7 Realización de experimentos  ########

# url = "http://www.abc.es/cultura/arte/abci-prado-y-thyssen-salen-armario-201706150132_noticia.html"
# articulo = Article(url)
# articulo.download()
# articulo.parse()
# nuevo_ejemplo = articulo.text

### Metemos las frecuencias de palabras en un archivo ########
# frec=doc.frecuencia()
# file = open('frecuencia.txt', 'w', encoding='utf8')
# file.write(str(frec))
# file.close()


### Escribir en un csv ###

# datos = [('aaa', 111), ('bbb', 222), ('ccc', 333)]
# csvsalida = open('salidat.csv', 'w', newline='')
# salida = csv.writer(csvsalida)
# salida.writerow(['campo1', 'campo2'])
# salida.writerows(datos)
# del salida
# csvsalida.close()

##### Vectorizar un texto ###
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.neighbors import KNeighborsClassifier

vectorizer = CountVectorizer(min_df=1)

documents = []
tipos = []


X = vectorizer.fit_transform(documents)

# Con esto tenemos el documento vectorizado
# print(X.toarray())
np.set_printoptions(threshold=np.nan) # Imprime la matriz entera

tfid = TfidfVectorizer(stop_words=doc.palabras_comunes)

X_train = tfid.fit_transform(documents)
Y_train = tipos
clf = KNeighborsClassifier(n_neighbors=10)
clf.fit(X_train, Y_train)
