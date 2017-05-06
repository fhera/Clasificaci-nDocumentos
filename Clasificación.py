from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.neighbors import KNeighborsClassifier
import pandas
import numpy
from sklearn import preprocessing
from sklearn import model_selection
from sklearn import naive_bayes
from sklearn import neighbors

# def read_all_documents(root):
#     labels = []
#     docs = []
#     print("Antes de los for", root)
#     for r, dirs, files in os.walk(root):
#         for file in files:
#             with open(os.path.join(r, file), "r") as f:
#                 docs.append(f.read())
#             labels.append(r.replace(root, ''))
#     print(labels)
#     return dict([('docs', docs), ('labels', labels)])
#
#
# doc = read_all_documents("Documentos")
# print("Leemos los documentos\n", doc)
#
# tfid = TfidfVectorizer()
# X_train = tfid.fit_transform(doc)
#
# clf = KNeighborsClassifier(n_neighbors=3)
# clf.fit(X_train)
class Clasificacion():
    def __init__(self,documento):
        self.documento = documento


    def __str__(self):
        return "La clasificación del documento con nombre {} es del tipo {}.".format(self.documento, self.tipo)

c = Clasificacion()