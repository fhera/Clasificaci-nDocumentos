from Docs import Docs
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import CountVectorizer
import pandas
import numpy as np
from sklearn import preprocessing
from sklearn import model_selection
from sklearn.neighbors import KNeighborsClassifier


class ClasificacionKNN():
    doc = Docs()
    datos = doc.leer_doc()
    documentos = datos['docs']
    categorias = datos['categoria']

    palabras_comunes = doc.palabras_comunes
    vocabulario = doc.vocabulario()

    tfid = []

    def __init__(self, doc=documentos):

        print("-----------PREPROCESADO-----------")
        # Vamos a ir llamando los métodos necesarios para el preprocesado del texto situado en la clase Docs.py
        self.doc.documentos_csv()
        print("-----------CONJUNTO DE ENTRENAMIENTO/TEST-----------")
        # Vamos a dividir el conjunto de entrenamiento y el conjunto de test

        print("Un momento que estamos analizando los documentos...")
        vectorizer = CountVectorizer()
        vectorizer.fit_transform(self.documentos)
        print(vectorizer.get_feature_names())

        # Tratamos el vocabulario para añadirlo al vector tfidf
        lista_vocabulario = [palabra for documentos in self.vocabulario.values() for palabra in documentos]

        tfid = TfidfVectorizer(stop_words=self.palabras_comunes, vocabulary=lista_vocabulario)
        self.tfid = tfid
        documentos_codificado = tfid.fit_transform(self.documentos)
        self.conjunto_entrenamiento = documentos_codificado
        # print("Vectores del documento sin codificar:\n", tfid.get_feature_names())

        ### Metemos el conjunto de entrenamiento en un archivo ########
        file = open('Datos/conjunto_entrenamientoKNN.txt', 'w', encoding='utf8')
        file.write(str(documentos_codificado.todense()))
        file.close()
        print("Conjunto de entrenamiento listo")

    # def __init__(self):
    #     docs = pandas.read_csv('Datos/pesos.csv', header=0)
    #
    #     codificadores = []
    #     docs_codificado = pandas.DataFrame()
    #     lista_valores = []
    #     for variable, valores in docs.iteritems():
    #         le = preprocessing.LabelEncoder()
    #         le.fit(valores)
    #         # print('Codificación de valores para {}: {}'.format(variable, le.classes_))
    #         codificadores.append(le)
    #         docs_codificado[variable] = le.transform(valores)
    #
    #     print(docs_codificado.tail(10))
    #
    #     print('Codificación:', codificadores[-1].classes_)
    #     print("Cantidad total de ejemplos:", docs_codificado.shape[0])  # Cantidad total de ejemplos
    #     print(docs_codificado['Categoria'].value_counts(normalize=True, sort=False))
    #
    #     docs_entrenamiento, docs_prueba = model_selection.train_test_split(
    #         docs_codificado, test_size=.33, random_state=12345,
    #         stratify=docs_codificado['Categoria'])
    #
    #
    #     datos_entrenamiento = docs_entrenamiento.loc[:,:'isla']
    #     clases_entrenamiento = docs_entrenamiento['Categoria']
    #
    #     datos_prueba = docs_prueba.loc[:,:'isla']
    #     clases_prueba = docs_prueba['Categoria']
    #
    #     # print(datos_entrenamiento)
    #     # print("Categoria:\n",clases_entrenamiento)
    #
    #     clasif_kNN = KNeighborsClassifier(n_neighbors=5, metric='hamming')
    #     clasif_kNN.fit(datos_entrenamiento, clases_entrenamiento)
    #     # distancias, vecinos = clasif_kNN.kneighbors(nuevo_ejemplo_codif)
    #
    #     print(clasif_kNN.score(datos_prueba, clases_prueba))


c = ClasificacionKNN()
