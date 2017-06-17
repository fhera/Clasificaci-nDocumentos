from Docs import Docs
import numpy
import pandas
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.neighbors import KNeighborsClassifier
from sklearn import preprocessing
from sklearn.feature_extraction.text import CountVectorizer
from sklearn import model_selection
from sklearn import naive_bayes
from sklearn import neighbors
from newspaper import Article


class Clasificacion():
    doc = Docs()
    datos = doc.leer_doc()
    documentos = datos['docs']
    categorias = datos['categoria']

    docs_codificados = []
    tfid = []
    clf = []

    def __init__(self, doc=documentos):
        print("-----------PREPROCESADO-----------")
        # Vamos a dividir el conjunto de entrenamiento y el conjunto de test

        print("Un momento que estamos analizando los documentos...")
        vectorizer = CountVectorizer()
        vectorizer.fit_transform(self.documentos)
        print(vectorizer.get_feature_names())

        # Tratamos el vocabulario para añadirlo al vector tfidf
        vocabulario = self.doc.vocabulario()
        lista_vocabulario = [palabra for documentos in vocabulario.values() for palabra in documentos]

        tfid = TfidfVectorizer(stop_words=self.doc.palabras_comunes, vocabulary=lista_vocabulario)
        self.tfid = tfid
        documentos_codificado = tfid.fit_transform(self.documentos)
        self.docs_codificados = documentos_codificado
        print("Vocabulario:\n", tfid.get_feature_names())
        # print(documentos_codificado)

        print("-----------ENTRENANDO ALGORITMO KNN-----------")
        # docs_entrenamiento, docs_prueba = model_selection.train_test_split(
        #     self.docs_codificados, test_size=.33, random_state=12345,
        #     stratify=self.categorias)
        docs_entrenamiento = self.docs_codificados
        cat_entrenamiento = self.categorias
        clf = neighbors.KNeighborsClassifier(n_neighbors=15)

        clf.fit(docs_entrenamiento, cat_entrenamiento)

        test = self.doc.leer_doc("test")
        docs_prueba = self.tfid.fit_transform(test['docs'])
        cat_prueba = test['categoria']

        print('Porcentaje de acierto sobre 1: %0.3f' % clf.score(docs_prueba, cat_prueba))
        self.clf = clf

    def Predecir(self, url, classifier):
        articulo = Article(url)
        articulo.download()
        articulo.parse()
        # print(articulo.text)
        article = articulo.text
        X_test = self.tfid.transform([article])
        return classifier.predict(X_test)[0]

    def Mostrar_predicciones(self, urls, classifier):
        print("-----------PREDICCIONES DE LOS ARTICULOS NUEVOS-----------")
        for url in urls:
            print('La predicción de la categoría es: ' + self.Predecir(url, classifier))


c = Clasificacion()
clasificador = c.clf

c.Mostrar_predicciones([
    'http://www.abc.es/economia/abci-bufetes-intentan-accionistas-bankia-vayan-juicio-201602190746_noticia.html',
    'http://www.elconfidencial.com/deportes/futbol/2016-02-19/torres-atletico-cope_1154857/',
    'http://sevilla.abc.es/deportes/alfinaldelapalmera/noticias/fichajes-betis/betis-pide-tres-millones-petros-130734-1497644020.html',
    'http://sevilla.abc.es/deportes/alfinaldelapalmera/noticias/fichajes-betis/betis-no-mas-ofertas-villamarin-130737-1497644996.html',
    'http://www.abc.es/cultura/arte/abci-crece-familia-duques-osuna-coleccion-prado-201706170138_noticia.html'
], clasificador)




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
