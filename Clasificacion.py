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

    def __init__(self, documento):
        self.docs = documento

    def preprocesamiento(self):
        tfid = TfidfVectorizer(stop_words=self.palabras_comunes)
        documentos_codificado = tfid.fit_transform(self.docs)

    def knn(self):

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


# ##### Pruebas con KNN #####
# from sklearn import preprocessing
# from sklearn import model_selection
#
# documentos = pandas.read_csv('documentos.csv', header=0)
#
# codificadores = []
# docs_codificado = pandas.DataFrame()
#
# for variable, valores in documentos.iteritems():
#     le = preprocessing.LabelEncoder()
#     le.fit(valores)
#     # print('Codificación de valores para {}: {}'.format(variable, le.classes_))
#     codificadores.append(le)
#     docs_codificado[variable] = le.transform(valores)
#
# # _____ Separación en conjunto test y entrenamientos
# print('Codificación:', codificadores[-1].classes_)
# print("Cantidad total de ejemplos:", docs_codificado.shape[0])
# print(docs_codificado['Categoria'].value_counts(normalize=True,
#                                                 sort=False))  # Frecuencia total de cada clase de categoria
#
# docs_entrenamiento, docs_prueba = model_selection.train_test_split(
#     docs_codificado, test_size=.20, random_state=12345,
#     stratify=docs_codificado['Categoria'])
#
# print("\nConjunto de prueba(33%):")
# print(docs_prueba.shape[0], 200 * .2)
# print(docs_prueba['Categoria'].value_counts(
#     normalize=True, sort=False))
#
# print("\nConjunto de entrenamiento(67%) :")
# print(docs_entrenamiento.shape[0], 200 * (1 - .2))
# print(docs_entrenamiento['Categoria'].value_counts(
#     normalize=True, sort=False))
#
# datos_entrenamiento = docs_entrenamiento.loc[:, 'artista':'ser']
# clases_entrenamiento = docs_entrenamiento['Categoria']
#
# datos_prueba = docs_prueba.loc[:, 'artista':'ser']
# clases_prueba = docs_prueba['Categoria']
#
# from sklearn import neighbors
#
# clasif_kNN = neighbors.KNeighborsClassifier(n_neighbors=10, metric='hamming')
#
# clasif_kNN.fit(datos_entrenamiento, clases_entrenamiento)
#
# print("Score:", clasif_kNN.score(datos_prueba, clases_prueba))
#
# # nuevo_ejemplo = articulo.text
# #
# #
# # distancias, vecinos = clasif_kNN.kneighbors(nuevo_ejemplo_codif)
# # print(nuevo_ejemplo_codif)
# # print(datos_entrenamiento.iloc[vecinos[0]])
# # print(distancias[0])
