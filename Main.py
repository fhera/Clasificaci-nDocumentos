import Genera_documentos
from io import open
import Docs
import csv
import pandas
import re

############# Generador de documentación ############
# 4.3 Obtener un conjunto de textos de entrenamiento (y de test)
# genera = Genera_documentos.Genera_documentos()


############# Clase Documentos #################

doc = Docs.Docs()

doc.documentos_csv()
# print("Listamos las palabras de los documentos:\n", doc.lista_palabras())
# print("Frecuencia de palabras en los docs:\n", doc.frecuencia())

# print(doc.vocabulario())
# print(doc.vocabulario_para_csv())

# print("Frecuencia docs:\n", doc.frecuencia_documental())
# print("Frecuencia docs inversa:\n", doc.frecuencia_documental_inversa())
# print("Peso:\n", doc.peso())


# Cuenta las palabras de la categoria indicada
# print(len(doc.lista_palabras()['Deportes']))



####### 4.7 Realización de experimentos  ########

#  url = "http://www.abc.es/internacional/20150508/abci-hitler-aniversario-201505022206.html"
# articulo = Article(url)
# articulo.download()
# articulo.parse()
# print(articulo.text)

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