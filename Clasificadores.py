from docutils.nodes import document
from sklearn.neighbors import KNeighborsClassifier
from newspaper import Article
from collections import Counter
from sklearn import naive_bayes
import Docs
import pandas
import numpy


class Clasificadores():
    entrenamientoNB = pandas.read_csv('Datos/probabilidad.csv', header=0)
    doc = Docs.Docs()
    entrenamientoKNN = []
    vocabulario = doc.vocabulario()

    # def __init__(self, opcion, entrenamiento=None, doc=None):
    #     if opcion == 1:
    #         print("Has elegido KNN.")
    #         if entrenamiento != None:
    #             conKNN = ClasificacionKNN(entrenamiento=entrenamiento, doc=doc)
    #         else:
    #             conKNN = ClasificacionKNN(doc=doc)
    #         self.entrenamientoKNN = conKNN.conjunto_entrenamiento
    #         categoria = conKNN.categorias
    #         tfid = conKNN.tfid
    #     elif opcion == 2:
    #         print("Has elegido Naive Bayes, este método es más lento.")
    #         if entrenamiento != None:
    #             conNB = ClasificacionNB(entrenamiento=entrenamiento, doc=doc)
    #         else:
    #             conNB = ClasificacionNB(doc=doc)
    #         self.entrenamientoNB = conNB.conjunto_entrenamiento
    #         categoria = conNB.categorias
    #         tfid = conNB.tfid

    def NB(self, entrenamiento=entrenamientoNB, doc=None):
        clf = naive_bayes.MultinomialNB(alpha=1.0)
        datos_entrenamiento = entrenamiento.loc[:, 'arte':'isla']
        clases_entrenamiento = self.entrenamientoNB['Categoria']
        clf.fit(datos_entrenamiento, clases_entrenamiento)
        if doc != None:
            documento = self.doc_vocabulario(doc)
            documento = numpy.reshape(documento, (1, -1))
            print('La predicción de la categoría es:',clf.predict(documento))

        return clf

    def KNN(self, entrenamiento=entrenamientoKNN, doc=None):

        print("\n-----------ENTRENANDO ALGORITMO KNN-----------")
        docs_entrenamiento = entrenamiento
        cat_entrenamiento = self.categoria
        clf = KNeighborsClassifier(n_neighbors=14)

        clf.fit(docs_entrenamiento, cat_entrenamiento)
        if doc != None:
            test = self.tfid.transform([doc])
            print("La predicción de la categoría es:", clf.predict(test)[0])
        else:
            test = self.doc.leer_doc("test")
            docs_prueba = self.tfid.fit_transform(test['docs'])
            cat_prueba = test['categoria']
            print('Porcentaje de acierto sobre : {}%'.format(round(clf.score(docs_prueba, cat_prueba), 3) * 100))
        return clf

    def Predecir(self, url, classifier):
        articulo = Article(url)
        articulo.download()
        articulo.parse()
        # print(articulo.text)
        article = articulo.text
        X_test = self.tfid.transform([article])
        return classifier.predict(X_test)[0]

    def Mostrar_predicciones(self, classifier, urls):
        print("\n-----------PREDICCIONES DE LOS ARTICULOS NUEVOS-----------")
        for url in urls:
            print('La predicción de la categoría es:', self.Predecir(url, classifier))

    # NB
    def cuenta_palabras(self,doc):
        lista = []
        wordcount = Counter(doc.split())
        for item in wordcount.items():
            lista.append(item)
        return dict(lista)

    def doc_vocabulario(self, doc):
        documento = self.cuenta_palabras(doc)
        lista_vocabulario = [palabra for documentos in self.vocabulario.values() for palabra in documentos]
        res = {}
        for palabra in lista_vocabulario:
            res[palabra] = 0
        for palabra, valor in documento.items():
            if palabra in lista_vocabulario:
                res[palabra] = valor
        return list(res.values())
