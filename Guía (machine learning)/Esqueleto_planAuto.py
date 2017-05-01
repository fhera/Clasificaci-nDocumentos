#El paquete de Python scikit-learn (sklearn en lo que sigue) proporciona un marco de trabajo para el aprendizaje automático.
#pandas y numpy son modulos para el análisis de datos y cáculo científico
import pandas
import numpy


##############  MODELADO DE LOS DATOS  ######################

# cars devuelve un DataFrame de un archivo csv con los atributos names
cars = pandas.read_csv('cars.csv', header=None,
                       names=['buying', 'maint', 'doors', 'persons',
                              'lug_boot', 'safety', 'acceptability'])
print(cars.shape)  # Número de filas y columnas
cars.head(10)  # Diez primeros ejemplos


# sklearn trabaja sobre variables discretas, por lo que tenemos que convertir los datos en nº enteros. Preprocesamos el contenido:

from sklearn import preprocessing
codificadores = []
cars_codificado = pandas.DataFrame()

for variable, valores in cars.iteritems():
    le = preprocessing.LabelEncoder()
    le.fit(valores)
    print('Codificación de valores para {}: {}'.format(variable, le.classes_))
    codificadores.append(le)
    cars_codificado[variable] = le.transform(valores)

cars_codificado.head(10)

# Si no es necesario conservar los codificadores, la siguiente es una manera más directa de codificar las variables
# le = preprocessing.LabelEncoder()
# cars_codificado = cars.apply(le.fit_transform, axis=0)

############ SEPARACIÓN DE CONJUNTOS ENTRENAMIENTO-PRUEBAS ####################
#Separamos el conjunto de entrenamiento del de pruebas, pero teniendo en cuenta que los datos pueden no ser uniformes. Realizamos la separación de ejemplos de manera estratificada, intentando mantener la proporción:

from sklearn import model_selection

print('Codificación:', codificadores[-1].classes_)
print("Cantidad total de ejemplos:",cars_codificado.shape[0])
print(cars_codificado['acceptability'].value_counts(
        normalize=True, sort=False))  # Frecuencia total de cada clase de aceptabilidad

#Para dividir un conjunto de datos en un subconjunto de entrenamiento y otro de prueba, sklearn proporciona la función train_test_split.
# Esto es lo relevante, divide el conjunto de entrenamiento y prueba
cars_entrenamiento, cars_prueba = model_selection.train_test_split(
    cars_codificado, test_size=.33, random_state=12345,
    stratify=cars_codificado['acceptability'])


#Un requisito, pues, para poder continuar es separar los conjuntos de datos cars_entrenamiento y cars_prueba en los valores de los atributos por un lado y la clasificación por otro.

datos_entrenamiento = cars_entrenamiento.loc[:, 'buying':'safety']
clases_entrenamiento = cars_entrenamiento['acceptability']

datos_prueba = cars_prueba.loc[:, 'buying':'safety']
clases_prueba = cars_prueba['acceptability']


############ ALGORITMO NAIVE BAYES ####################



# sklearn implementa naive Bayes para atributos discretos mediante instancias de la clase MultinomialNB:

from sklearn import naive_bayes

clasif_NB = naive_bayes.MultinomialNB(alpha=1.0)  # alpha es el tamaño muestral equivalente


#La utilización de la instancia construida requiere que los atributos que caracterizan los ejemplos sean binarios. Podemos transformar nuestros atributos multinomiales en atributos binarios mediante el preprocesador OneHotEncoder de sklearn.

ohe = preprocessing.OneHotEncoder(sparse = False)


# En las expresiones siguientes, el método values proporciona los datos como un vector de numpy y el método reshape lo transforma entonces a una matriz con una columna y tantas filas como sea necesario. Esto debe hacerse ya que el preprocesador OneHotEncoder solo trabaja con matrices.

print(cars_codificado['buying'].values)
print(cars_codificado['buying'].values.reshape(-1, 1))
ohe.fit(cars_codificado['buying'].values.reshape(-1, 1))
ohe.transform(cars_codificado['buying'].values.reshape(-1, 1))


ohe = preprocessing.OneHotEncoder(sparse = False)
# El método fit_transform realiza un ajuste a partir de una matriz de datos seguido de una transformación de esos mismos datos.

datos_entrenamiento_nb = ohe.fit_transform(datos_entrenamiento)
datos_prueba_nb = ohe.fit_transform(datos_prueba)


# Las siguientes expresiones muestran las cuentas realizadas y (los logaritmos de) las probabilidades aprendidas por el modelo:

print(clasif_NB.class_count_)
print(clasif_NB.class_log_prior_)
print(clasif_NB.feature_count_)
print(clasif_NB.feature_log_prob_)

# El método predict devuelve la clase predicha por el modelo para un nuevo ejemplo y el método score el rendimiento sobre un conjunto de datos de prueba:

nuevo_ejemplo = ['vhigh', 'vhigh', '3', 'more', 'big', 'high']
# Codificamos los valores de los atributos
nuevo_ejemplo_codif = [le.transform([valor])
                       for valor, le in zip(nuevo_ejemplo, codificadores)]
nuevo_ejemplo_codif = numpy.reshape(nuevo_ejemplo_codif, (1, -1))
print(nuevo_ejemplo_codif)
# Transformamos los atributos a codificación binaria
nuevo_ejemplo_nb = ohe.transform(nuevo_ejemplo_codif)
print(nuevo_ejemplo_nb)
# Predecimos la clase
clase_nuevo_ejemplo = clasif_NB.predict(nuevo_ejemplo_nb)
print(codificadores[-1].inverse_transform(clase_nuevo_ejemplo))


# Calculamos la fracción de clases correctamente predichas para el conjunto de datos de prueba:
clasif_NB.score(datos_prueba_nb, clases_prueba)



##################### ALGORITMO kNN ####################

# sklearn implementa kNN como instancias de la clase KNeighborsClassifier
from sklearn import neighbors

clasif_kNN = neighbors.KNeighborsClassifier(n_neighbors=5, metric='hamming')


#Entrenamos el modelo.

clasif_kNN.fit(datos_entrenamiento, clases_entrenamiento)


# El método kneighbors permite encontrar los (índices de los)  kk  vecinos más cercanos de los ejemplos proporcionados, así como las distancias a las que se encuentran:

distancias, vecinos = clasif_kNN.kneighbors(nuevo_ejemplo_codif)
print(nuevo_ejemplo_codif)
print(datos_entrenamiento.iloc[vecinos[0]])
print(distancias[0])


#El método predict devuelve la clase predicha por el modelo para un nuevo ejemplo y el método score el rendimiento sobre un conjunto de datos de prueba:

clase_nuevo_ejemplo = clasif_kNN.predict(nuevo_ejemplo_codif)
print(codificadores[-1].inverse_transform(clase_nuevo_ejemplo))


# Calculamos la fracción de clases correctamente predichas para el conjunto de datos de prueba:
clasif_kNN.score(datos_prueba, clases_prueba)






