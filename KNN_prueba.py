import os
from Docs import Docs

doc = Docs()
datos = doc.leer_doc()
documentos = datos['docs']
categorias = datos['categoria']
vocabulario = doc.vocabulario()
lista_vocabulario = [palabra for documentos in vocabulario.values() for palabra in documentos]


def read_all_documents(root):
    labels = []
    docs = []
    for r, dirs, files in os.walk(root):
        for file in files:
            with open(os.path.join(r, file), "r") as f:
                docs.append(f.read())
            labels.append(r.replace(root, ''))
    return dict([('docs', docs), ('labels', labels)])


data = read_all_documents('Documentos')
print(data)
documents = data['docs']
labels = data['labels']
# frec = data
# file = open('frecuencia.txt', 'w', encoding='utf8')
# file.write(str(frec))
# file.close()

import re
from collections import defaultdict


def palabras(doc):
    return (palabras.lower() for palabras in re.findall(r"\w+", doc))


def frecuencia(palabras):
    f = defaultdict(int)
    for token in palabras:
        f[token] += 1
    return f


def frec_palabras(doc):
    return frecuencia(palabras(doc))


from sklearn.feature_extraction import DictVectorizer

vectorizer = DictVectorizer()
vectorizer.fit_transform(frec_palabras(d) for d in documents)
print("Matriz:\n", vectorizer.get_feature_names())

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.neighbors import KNeighborsClassifier

palabras_comunes = ['a', 'ante', 'bajo', 'cabe', 'con', 'contra', 'de', 'desde', 'en', 'entre', 'hacia', 'hasta',
                    'para', 'por', 'según', 'sin', 'so', 'sobre', 'tras', 'durante', 'mediante', 'excepto', 'salvo',
                    'incluso', 'más', 'menos', 'no', 'si', 'sí', 'el', 'la', 'los', 'las', 'un', 'una', 'unos',
                    'unas', 'este', 'esta', 'estos', 'estas', 'aquel', 'aquella', 'aquellos', 'aquellas', 'he',
                    'has', 'ha', 'hemos', 'habéis', 'han', 'había', 'habías', 'habíamos', 'habíais', 'habían',
                    'además', 'ahora', 'alguna', 'al', 'algún', 'alguno', 'algunos', 'algunas', 'mi', 'mis',
                    'misma', 'mismo', 'muchas', 'muchos', 'y', 'algo', 'antes', 'del', 'ellas', 'eso', 'muy', 'que',
                    'su', 'sus', 'ya', 'él', 'éste', 'ésta', 'ahí', 'allí', 'como', 'cuando', 'era', 'es', 'le',
                    'me', 'lo', 'pero', 'qué', 'también', 'te', 'yo', 'tu', 'el', 'nosotros', 'vosotros', 'después',
                    'se', 'o', 'n', 's', 'son', 'dos']

tfid = TfidfVectorizer(stop_words=palabras_comunes)

X_train = tfid.fit_transform(documents)
y_train = labels
clf = KNeighborsClassifier(n_neighbors=10)
clf.fit(X_train, y_train)

test = read_all_documents('test')
X_test = tfid.transform(test['docs'])
y_test = test['labels']
pred = clf.predict(X_test)

print('accuracy score %0.3f' % clf.score(X_test, y_test))

from newspaper import Article


def predict_category(url, classifier):
    articulo = Article(url)
    articulo.download()
    articulo.parse()
    # print(articulo.text)
    article = articulo.text
    X_test = tfid.transform([article])
    return clf.predict(X_test)[0]


def show_predicted_categories(urls, classifier):
    for url in urls:
        print('La predicción de la categoría es: ' + predict_category(url, clf))


show_predicted_categories(
    [
        'http://www.abc.es/economia/abci-bufetes-intentan-accionistas-bankia-vayan-juicio-201602190746_noticia.html',
        'http://www.elconfidencial.com/deportes/futbol/2016-02-19/torres-atletico-cope_1154857/',
        'http://sevilla.abc.es/deportes/alfinaldelapalmera/noticias/fichajes-betis/betis-pide-tres-millones-petros-130734-1497644020.html',
        'http://sevilla.abc.es/deportes/alfinaldelapalmera/noticias/fichajes-betis/betis-no-mas-ofertas-villamarin-130737-1497644996.html',
        'http://www.abc.es/cultura/arte/abci-crece-familia-duques-osuna-coleccion-prado-201706170138_noticia.html'
    ],clf)