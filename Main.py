import Genera_documentos
import Docs
import pandas
import re

############# Generador de documentación ############
# 4.3 Obtener un conjunto de textos de entrenamiento (y de test)
# genera = Genera_documentos.Genera_documentos()


############# Clase Documentos #################

doc = Docs.Docs()
# print("Listamos las palabras que no queremos: \n", doc.leer_palabras_no_claves())
# print("Listamos las palabras de los documentos:\n", doc.lista_palabras())
print("Frecuencia de palabras en los docs:\n", doc.frecuencia())
# print("Frecuencia docs:\n", doc.frecuencia_documental())
# print("Frecuencia docs inversa:\n", doc.frecuencia_documental_inversa())
# print("Peso:\n", doc.peso())

# print(doc.vocabulario())

# Cuenta las palabras de la categoria indicada
# print(len(doc.lista_palabras()['Deportes']))



####### 4.7 Realización de experimentos  ########

#  url = "http://www.abc.es/internacional/20150508/abci-hitler-aniversario-201505022206.html"
# articulo = Article(url)
# articulo.download()
# articulo.parse()
# print(articulo.text)