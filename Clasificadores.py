from sklearn.neighbors import KNeighborsClassifier
from newspaper import Article
from ClasificacionKNN import ClasificacionKNN
from ClasificacionNB import ClasificacionNB
from sklearn import naive_bayes
import Docs


class Clasificadores():
    doc = Docs.Docs()
    entrenamientoKNN = []
    entrenamientoNB = []

    def __init__(self, opcion):
        if  opcion== 1:
            print("Has elegido KNN.")
            conKNN = ClasificacionKNN()
            self.entrenamientoKNN = conKNN.conjunto_entrenamiento
            categoria = conKNN.categorias
            tfid = conKNN.tfid
        elif opcion==2:
            print("Has elegido Naive Bayes, este método es más lento.")
            conNB = ClasificacionNB()
            self.entrenamientoNB = conNB.conjunto_entrenamiento
            categoria = conNB.categorias
            tfid = conNB.tfid



    def NB(self, entrenamiento=entrenamientoNB, doc=None):
        clasif_NB = naive_bayes.MultinomialNB(alpha=1.0)

    def KNN(self, entrenamiento=entrenamientoKNN, doc=None):

        print("\n-----------ENTRENANDO ALGORITMO KNN-----------")
        docs_entrenamiento = entrenamiento
        cat_entrenamiento = self.categoria
        clf = KNeighborsClassifier(n_neighbors=14)

        clf.fit(docs_entrenamiento, cat_entrenamiento)
        if doc != None:
            test = self.tfid.transform([doc])
            print("La predicción de la categoría es:",clf.predict(test)[0])
        else:
            test = self.doc.leer_doc("test")
            docs_prueba = self.tfid.fit_transform(test['docs'])
            cat_prueba = test['categoria']
            print('Porcentaje de acierto sobre : {}%'.format(round(clf.score(docs_prueba, cat_prueba),3) * 100))
        return clf

    def Predecir(self, url, classifier):
        articulo = Article(url)
        articulo.download()
        articulo.parse()
        # print(articulo.text)
        article = articulo.text
        X_test = self.tfid.transform([article])
        return classifier.predict(X_test)[0]

    def Mostrar_predicciones(self,classifier, urls):
        print("\n-----------PREDICCIONES DE LOS ARTICULOS NUEVOS-----------")
        for url in urls:
            print('La predicción de la categoría es:', self.Predecir(url, classifier))