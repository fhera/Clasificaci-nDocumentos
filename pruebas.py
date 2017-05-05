from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.neighbors import KNeighborsClassifier

import Documento
import os


def read_all_documents(root):
    labels = []
    docs = []
    print("Antes de los for", root)
    for r, dirs, files in os.walk(root):
        for file in files:
            with open(os.path.join(r, file), "r") as f:
                docs.append(f.read())
            labels.append(r.replace(root, ''))
    print(labels)
    return dict([('docs', docs), ('labels', labels)])


doc = read_all_documents("Documentos")
print("Leemos los documentos\n", doc)

tfid = TfidfVectorizer()
X_train = tfid.fit_transform(doc)

clf = KNeighborsClassifier(n_neighbors=3)
clf.fit(X_train)