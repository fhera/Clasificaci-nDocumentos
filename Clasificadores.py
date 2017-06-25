from sklearn.neighbors import KNeighborsClassifier
from newspaper import Article
from collections import Counter
from sklearn import naive_bayes
from ClasificacionKNN import ClasificacionKNN
from ClasificacionNB import ClasificacionNB
import Docs
import pandas
import numpy


class Clasificadores():
    doc = Docs.Docs()
    vocabulario = doc.vocabulario()

    ClasificacionNB()
    entrenamientoNB = pandas.read_csv('Datos/probabilidad.csv', header=0)
    clfKNN = ClasificacionKNN()
    entrenamientoKNN =clfKNN.conjunto_entrenamiento
    categoria = clfKNN.categorias
    tfid = clfKNN.tfid

    def NB(self, entrenamiento=entrenamientoNB, doc=None):
        clf = naive_bayes.MultinomialNB(alpha=1.0)
        datos_entrenamiento = entrenamiento.loc[:, 'arte':'isla']
        clases_entrenamiento = self.entrenamientoNB['Categoria']
        clf.fit(datos_entrenamiento, clases_entrenamiento)
        if doc != None:
            documento = self.doc_vocabulario(doc)
            documento = numpy.reshape(documento, (1, -1))
            print('La predicción de la categoría por Naive Bayes es:', clf.predict(documento))
        return clf

    def KNN(self, entrenamiento=entrenamientoKNN, doc=None):
        print("\n-----------ENTRENANDO ALGORITMO KNN-----------")
        docs_entrenamiento = entrenamiento
        cat_entrenamiento = self.categoria
        clf = KNeighborsClassifier(n_neighbors=14)

        clf.fit(docs_entrenamiento, cat_entrenamiento)
        if doc != None:
            test = self.tfid.transform([doc])
            print("La predicción de la categoría por KNN es:", clf.predict(test)[0])
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
        print("\n-----------PREDICCIONES CON KNN DE LOS ARTICULOS NUEVOS-----------")
        for url in urls:
            print('La predicción de la categoría es:', self.Predecir(url, classifier))

    # NB
    def cuenta_palabras(self, doc):
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
