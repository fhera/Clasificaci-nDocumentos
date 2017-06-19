from Docs import Docs
from collections import OrderedDict
import pandas
import csv
from sklearn import preprocessing
from sklearn import naive_bayes


class ClasificacionNB2():
    doc = Docs()
    categorias = doc.categorias
    vocabulario = doc.vocabulario()
    lista_vocabulario = [palabra for documentos in vocabulario.values() for palabra in documentos]

    # Capturamos el archivo csv y lo convertimos en un DataFrame
    voc = pandas.read_csv('Datos/probabilidad.csv', header=0)
    docu = pandas.read_csv('Datos/documentos.csv', header=0)

    def __init__(self):
        print("\n-----------PREPROCESADO-----------")
        # # Vamos a ir llamando los métodos necesarios para el preprocesado del texto situado en la clase Docs.py
        # self.doc.documentos_csv()
        # print("Un momento que estamos analizando los documentos...")
        # self.probabilidad_csv()

        ## PRUEBAS

        ohe = preprocessing.OneHotEncoder(sparse=False)
        datos_entrenamiento = self.docu.loc[:,'arte':'isla']
        datos_entrenamiento_nb = ohe.fit_transform(datos_entrenamiento)
        clases_entrenamiento = self.docu['Categoria']

        clasif_NB = naive_bayes.MultinomialNB(alpha=1.0)

        clasif_NB.fit(datos_entrenamiento_nb, clases_entrenamiento)



c = ClasificacionNB2()