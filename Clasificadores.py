from sklearn.neighbors import KNeighborsClassifier
from newspaper import Article
import ClasificacionKNN

class Clasificadores():
    conKNN = ClasificacionKNN.ClasificacionKNN()
    entrenamiento= conKNN.conjunto_entrenamiento

    def __init__(self):
        pass

    def KNN(self, entrenamiento = entrenamiento, doc=None):
        print("-----------ENTRENANDO ALGORITMO KNN-----------")
        # docs_entrenamiento, docs_prueba = model_selection.train_test_split(
        #     self.docs_codificados, test_size=.33, random_state=12345,
        #     stratify=self.categorias)
        docs_entrenamiento = entrenamiento
        cat_entrenamiento =
        clf = KNeighborsClassifier(n_neighbors=14)

        clf.fit(docs_entrenamiento, cat_entrenamiento)

        test = self.doc.leer_doc("test")
        docs_prueba = self.tfid.fit_transform(test['docs'])
        cat_prueba = test['categoria']

        print('Porcentaje de acierto sobre 1: %0.3f' % clf.score(docs_prueba, cat_prueba))
        return clf

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

clasificador = Clasificadores()
clfKNN = clasificador.KNN()

# c.Mostrar_predicciones([
#     'http://www.abc.es/economia/abci-bufetes-intentan-accionistas-bankia-vayan-juicio-201602190746_noticia.html',
#     'http://www.elconfidencial.com/deportes/futbol/2016-02-19/torres-atletico-cope_1154857/',
#     'http://sevilla.abc.es/deportes/alfinaldelapalmera/noticias/fichajes-betis/betis-pide-tres-millones-petros-130734-1497644020.html',
#     'http://sevilla.abc.es/deportes/alfinaldelapalmera/noticias/fichajes-betis/betis-no-mas-ofertas-villamarin-130737-1497644996.html',
#     'http://www.abc.es/cultura/arte/abci-crece-familia-duques-osuna-coleccion-prado-201706170138_noticia.html'
# ], clasificador)
