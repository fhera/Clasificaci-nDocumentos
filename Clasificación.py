from Docs import Docs
import numpy
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
    categoria =[]
    preposiciones =['a', 'ante', 'bajo', 'cabe', 'con', 'contra', 'de', 'desde', 'en', 'entre', 'hacia', 'hasta',
                    'para', 'por', 'según', 'sin', 'so', 'sobre', 'tras','durante','mediante','excepto','salvo',
                    'incluso','más','menos']
    adverbios = ['no','si','sí']
    articulos = ['el','la','los','las','un','una','unos','unas','este','esta','estos','estas','aquel','aquella','aquellos','aquellas']
    verbos_auxiliares = ['he','has','ha','hemos','habéis','han','había','habías','habíamos','habíais','habían']

    def __init__(self, documento=Docs.leer_documentos()):
        self.docs = documento['docs']
        self.categoria = documento['categoria']

    def knn(self):
        tfid = TfidfVectorizer(stop_words=self.preposiciones+ self.adverbios +self.articulos +self.verbos_auxiliares )
        X_train = tfid.fit_transform(self.docs)
        Y_train = tfid.fit_transform(self.categoria)



    def __str__(self):
        return "La clasificación del documento con nombre {} es del tipo {}.".format(self.documento, self.tipo)


c = Clasificacion()
