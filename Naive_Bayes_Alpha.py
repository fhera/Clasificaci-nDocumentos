from sklearn import naive_bayes
from sklearn import preprocessing
from sklearn import model_selection
import pandas
import numpy

voc = pandas.read_csv('voc.csv', header=None,
                      names=['chino', 'pekin', 'shanghai',
                             'makao', 'tokio', 'japon','categoria'])

print('\n------------- Número de filas y columnas -------------')
print(voc.shape)
voc.head(4)

le = preprocessing.LabelEncoder()

print('\n------------- Codificación de valores -------------')
codificadores = []
voc_codificado = pandas.DataFrame()
for variable, valores in voc.iteritems():
    le = preprocessing.LabelEncoder()
    le.fit(valores)
    print('Codificacion de valores para {}: {}'.format(variable, le.classes_))
    codificadores.append(le)
    voc_codificado[variable] = le.transform(valores)

voc_codificado.head(4)

print('\n------------- Codificacion de los valores de la categoria -------------')
print('Codificacion:', codificadores[-1].classes_)
print('Cantidad de ejemplos: ')
print(voc_codificado.shape[0])
print('Ejemplos de cada tipo: ')

datos_entrenamiento = voc_codificado.loc[:,'chino':'japon']
clase_entrenamiento = voc_codificado['categoria']

#NAIVE-BAYES
clasif_NB = naive_bayes.MultinomialNB(alpha=1.0)
ohe = preprocessing.OneHotEncoder(sparse=False)

ohe.fit(voc_codificado['chino'].values.reshape(-1,1))
ohe.transform(voc_codificado['chino'].values.reshape(-1,1))

ohe = preprocessing.OneHotEncoder(sparse=False)
datos_entrenamiento_nb = ohe.fit_transform(datos_entrenamiento)

clasif_NB.fit(datos_entrenamiento_nb, clase_entrenamiento)

nuevo_ejemplo = ['2','none','none','none','1','1']          #El fallo está en que el 3 nunca ha aparecido en el entrenamiento y no sabe lo que es

# Codificamos los valores de los atributos
nuevo_ejemplo_codif = [le.transform([valor])
                       for valor, le in zip(nuevo_ejemplo, codificadores)]
nuevo_ejemplo_codif = numpy.reshape(nuevo_ejemplo_codif, (1, -1))

print('\n------------- Nuevo Ejemplo -------------')
print(nuevo_ejemplo_codif)
# Transformamos los atributos a codificación binaria
nuevo_ejemplo_nb = ohe.transform(nuevo_ejemplo_codif)
print(nuevo_ejemplo_nb)
# Predecimos la clase
clase_nuevo_ejemplo = clasif_NB.predict(nuevo_ejemplo_nb)
print(codificadores[-1].inverse_transform(clase_nuevo_ejemplo))

clasif_NB.score(datos_entrenamiento_nb, clase_entrenamiento)