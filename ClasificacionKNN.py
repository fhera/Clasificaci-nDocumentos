from Docs import Docs
from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np
np.set_printoptions(threshold=np.nan)
from sklearn.feature_extraction import DictVectorizer


class ClasificacionKNN():
    doc = Docs()
    datos = doc.leer_doc()
    documentos = datos['docs']
    categorias = datos['categoria']

    palabras_comunes = doc.palabras_comunes
    vocabulario = doc.vocabulario()
    lista_vocabulario = [palabra for documentos in vocabulario.values() for palabra in documentos]


    tfid = []
    conjunto_entrenamiento = []

    def __init__(self):
        print("-----------PREPROCESADO-----------")
        # Vamos a ir llamando los métodos necesarios para el preprocesado del texto situado en la clase Docs.py
        self.doc.documentos_csv()

        print("Un momento que estamos analizando los documentos...")
        vectorizer = DictVectorizer()
        # Le paso al vector para que entrene las frecuencias de cada documento,
        matriz = list(self.doc.frec_palabras(d) for d in self.documentos)
        vectorizer.fit_transform(self.doc.frec_palabras(d) for d in self.documentos)
        # print("Matriz:", vectorizer.get_feature_names())

        # Tratamos el vocabulario para añadirlo al vector tfidf

        tfid = TfidfVectorizer(stop_words=self.palabras_comunes, vocabulary=self.lista_vocabulario)
        self.tfid = tfid
        documentos_codificado = tfid.fit_transform(self.documentos)
        self.conjunto_entrenamiento = documentos_codificado
        # print("Vectores del documento sin codificar:\n", tfid.get_feature_names())

        print("\n-----------CREAMOS EL CONJUNTO DE ENTRENAMIENTO KNN-----------")
        # Vamos a dividir el conjunto de entrenamiento y el conjunto de test
        ### Metemos el conjunto de entrenamiento en un archivo ########
        documento_salida = 'Datos/pesos.txt'
        file = open(documento_salida, 'w', newline='')
        file.write(str(documentos_codificado.todense()))
        file.close()
        print("Creando fichero '{}' que contiene los pesos de los documentos".format(
            documento_salida))
