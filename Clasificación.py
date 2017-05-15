from Docs import Docs
import numpy
import pandas
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.neighbors import KNeighborsClassifier
from sklearn import preprocessing
from sklearn import model_selection
from sklearn import naive_bayes
from sklearn import neighbors


# doc = read_all_documents("Documentos")
# print("Leemos los documentos\n", doc)
#
# tfid = TfidfVectorizer()
# X_train = tfid.fit_transform(doc)
#
# clf = KNeighborsClassifier(n_neighbors=3)
# clf.fit(X_train)

class Clasificacion():
    docs = []
    categoria = []
        documento = Docs()

    def __init__(self, documento=documento.leer_documentos()):
        self.docs = documento['docs']
        self.categoria = documento['categoria']

    # def preprocesamiento(self):


    def knn(self):
        tfid = TfidfVectorizer(stop_words=self.preposiciones +
                                          self.adverbios + self.articulos + self.verbos_auxiliares)
        documentos_codificado = tfid.fit_transform(self.docs)
        categorias_codificado = tfid.fit_transform(self.categoria)
        # clf = KNeighborsClassifier(n_neighbors=10)

        docs_entrenamiento, docs_prueba = model_selection.train_test_split(
            documentos_codificado, test_size=.33, random_state=12345)
        print(docs_entrenamiento.shape[0])

        cat_entrenamiento, cat_prueba = model_selection.train_test_split(
            categorias_codificado, test_size=.33, random_state=123454)
        clasif_kNN = neighbors.KNeighborsClassifier(n_neighbors=5)
        clasif_kNN.fit(docs_entrenamiento, cat_entrenamiento)

        # return clasif_kNN.score(docs_prueba, cat_prueba)

        # return clf.fit(documentos_codificado, categorias_codificado)

    def __str__(self):
        return "La clasificación del documento con nombre {} es del tipo {}.".format(self.documento, self.tipo)

c = Clasificacion()
print(c.knn())
