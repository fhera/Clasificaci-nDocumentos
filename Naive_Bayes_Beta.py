from sklearn import naive_bayes
from sklearn import preprocessing
from sklearn import model_selection
import csv, operator
import pandas
import numpy
import time

#Etiquetas:
names=['artista','arte','obra','años','museo','año','kentridge','mundo','obras',
                             'exposición','premio','está','bienal','gran','fue','público','proyecto',
                             'artistas','artes','director','whatsapp','usuarios','todo','internet',
                             'google','zombies','amazon','millones','facebook','mensaje','of',
                             'compañía','semana','call','duty','tiene','tiempo','mayo','está',
                             'android','teatro','obra','danza','años','compañía','madrid','director',
                             'ser','mundo','espectáculo','hay','público','hace','está','sido','todos',
                             'esa','dice','tiene','usted','madrid','españa','euros','empresas','marcas',
                             'productos','año','millones','2016','sector','1','está','2015','parte',
                             'audiencia','distribución','nuevo','ciento','3','serna','moda','todo',
                             'años','reina','marca','vestido','negro','colección','fue','gran','equipo',
                             'vez','trabajo','prendas','tiempo','tiene','primera','campaña','casa','ser',
                             'partido','equipo','madrid','todo','ser','bien','fue','final','barcelona',
                             'puntos','mutua','open','5','mucho','gran','2','selección','spurs','18',
                             'suárez','thoreau','vida','todo','nos','libro','ser','mundo','uno','naturaleza',
                             'nada','sino','emerson','puede','cómo','hay','siempre','está','forma','porque',
                             'años','años','tierra','vida','universidad','cuántica','científicos','millones',
                             'investigadores','hace','tiempo','ser','gran','esto','fue','otros','está',
                             'superficie','donde','hay','puede','años','especies','españa','especie','río',
                             'aves','seo','amazonía','puede','organización','protección','red','año',
                             'países','país','pueden','ue','otros','están','hay','fue','años','san',
                             'historia','casa','rey','maría','hoy','donde','así','todo','don','siglo',
                             'españa','ni','gran','uno','villadiego','ser','entonces','Categoria']

#Capturamos el archivo csv y lo convertimos en un DataFrame
vocAux = pandas.read_csv('documentos.csv', header=None, names = names)

print('\n------------- Número de filas y columnas -------------')
print(vocAux.shape)
vocAux.head(5)

#Convertimos los números en etiquetas, según unos rangos elegidos meditadamente.
csvarchivo = open('documentos.csv')  # Abrir archivo csv
entrada = csv.reader(csvarchivo)  # Leer todos los registros
lista = []
for i in range(200): #Este 200 es por el número de filas
    palabras = next(entrada)
    for index in range(200): #Este otro por el número de columnas, son 201 pero de esta forma no convierte la última que es la correspondiente a la categoria
        if palabras[index] == '0' or palabras[index] == '1' or palabras[index] == '2' or palabras[index] == '3' or palabras[index] == '4':
            palabras[index] = 'vlow'
        elif palabras[index] == '5' or palabras[index] == '6' or palabras[index] == '7' or palabras[index] == '8' or palabras[index] == '9':
            palabras[index] = 'low'
        elif palabras[index] == '10' or palabras[index] == '11' or palabras[index] == '12' or palabras[index] == '13' or palabras[index] == '14':
            palabras[index] = 'med'
        elif palabras[index] == '15' or palabras[index] == '16' or palabras[index] == '17' or palabras[index] == '18' or palabras[index] == '19':
            palabras[index] = 'high'
        elif palabras[index] == '20' or palabras[index] == '21' or palabras[index] == '22' or palabras[index] == '23' or palabras[index] == '24':
            palabras[index] = 'vhigh'
        else:
            palabras[index] = 'vhigh'
    lista.append(palabras)
#print(lista)

#Creamos el CSV de salida con los datos convertidos en palabras
csvsalida = open('salida.csv', 'w')
salida = csv.writer(csvsalida)
salida.writerows(lista)

#Lo cargamos
voc = pandas.read_csv('salida.csv', header=None, names = names)
voc.head(10)

#Comienza Naive Bayes
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

#print('\n------------- Codificacion de los valores de la categoria -------------')
#print('Codificacion:', codificadores[-1].classes_)
#print('Cantidad de ejemplos: ')
#print(voc_codificado.shape[0])

datos_entrenamiento = voc_codificado.loc[:,'artista':'entonces']
clase_entrenamiento = voc_codificado['Categoria']

#NAIVE-BAYES
clasif_NB = naive_bayes.MultinomialNB(alpha=1.0)
ohe = preprocessing.OneHotEncoder(sparse=False)

ohe.fit(voc_codificado['artista'].values.reshape(-1,1))
ohe.transform(voc_codificado['artista'].values.reshape(-1,1))

ohe = preprocessing.OneHotEncoder(sparse=False)
datos_entrenamiento_nb = ohe.fit_transform(datos_entrenamiento)

clasif_NB.fit(datos_entrenamiento_nb, clase_entrenamiento)

nuevo_ejemplo = [vlow,vlow,vlow,vlow,vlow,vlow,vlow,vlow,vlow,vlow,vlow,vlow,vlow,vlow,
                 vlow,vlow,vlow,vlow,vlow,vlow,vlow,vlow,vlow,vlow,vlow,vlow,vlow,vlow,
                 vlow,vlow,vlow,vlow,vlow,vlow,vlow,vlow,vlow,vlow,vlow,vlow,vlow,vlow,
                 vlow,vlow,vlow,vlow,vlow,vlow,vlow,vlow,vlow,vlow,vlow,vlow,vlow,vlow,
                 vlow,vlow,vlow,vlow,vlow,vlow,vlow,vlow,vlow,vlow,vlow,vlow,vlow,vlow,
                 vlow,vlow,vlow,vlow,vlow,vlow,vlow,vlow,vlow,vlow,vlow,vlow,vlow,vlow,
                 vlow,vlow,vlow,vlow,vlow,vlow,vlow,vlow,vlow,vlow,vlow,vlow,vlow,vlow,
                 vlow,vlow,vlow,vlow,vlow,vlow,vlow,vlow,vlow,vlow,vlow,vlow,vlow,vlow,
                 vlow,vlow,vlow,vlow,vlow,vlow,vlow,vlow,vlow,vlow,vlow,vlow,vlow,vlow,
                 vlow,vlow,vlow,vlow,vlow,vlow,vlow,vlow,vlow,vlow,vlow,vlow,vlow,vlow,
                 vlow,vlow,vlow,vlow,vlow,vlow,vlow,vlow,vlow,vlow,vlow,vlow,vlow,vlow,
                 vlow,vlow,vlow,vlow,vlow,vlow,vlow,vlow,vlow,vlow,vlow,vlow,vlow,vlow,
                 vlow,vlow,vlow,vlow,vlow,vlow,vlow,vlow,vlow,vlow,vlow,vlow,vlow,vlow,
                 vlow,vlow,vlow,vlow,vlow,vlow,vlow,vlow,vlow,vlow,vlow,vlow,vlow,vlow,
                 vlow,vlow,vlow,vlow]
          #Tiene que ser Arte

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