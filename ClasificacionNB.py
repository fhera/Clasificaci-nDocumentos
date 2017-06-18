from Docs import Docs
from collections import OrderedDict
import pandas
import csv


class ClasificacionNB():
    doc = Docs()
    categorias = doc.categorias
    vocabulario = doc.vocabulario()
    lista_vocabulario = [palabra for documentos in vocabulario.values() for palabra in documentos]

    # Capturamos el archivo csv y lo convertimos en un DataFrame
    voc = pandas.read_csv('Datos/documentos.csv', header=0)

    # voc = pandas.read_csv('pruebasNB/voc.csv', header=0)
    # vocabulario = ['Chino', 'Pekin', 'Shangai', 'Macao', 'Tokio', 'Japon', 'Categoria']
    # categorias = ['ch', 'j']

    def Probabilidades_categorias(self):
        res = []
        for categoria in self.categorias:
            res.append((categoria, len(self.voc[self.voc['Categoria'] == categoria]) / self.voc['Categoria'].count()))
        return res

    def Probabilidades_vocabulario(self):
        res = OrderedDict()
        vocabulario = self.lista_vocabulario
        for categoria in self.categorias:
            lista_palabras = []
            for palabra in vocabulario:
                ocurrencias = 0
                sumatorio = 0
                numerador = 0
                denominador = 0
                # cuenta el número de veces que 'palabra' esta en la categoria 'categoria'
                frame = self.voc[self.voc['Categoria'] == categoria]
                for i in frame[palabra]:
                    ocurrencias += i

                # cuenta el numero de palabras que hay en la categoria 'categoria'
                valores = self.voc[self.voc['Categoria'] == categoria].values
                nuevaLista = []
                for i in range(len(valores)):
                    lista = valores[i]
                    for frecuencia in range(len(lista) - 1):
                        nuevaLista.append(lista[frecuencia])
                for frecuencia in nuevaLista:
                    sumatorio += frecuencia

                numerador = ocurrencias + 1
                denominador = sumatorio + len(self.vocabulario) - 1

                lista_palabras.append((palabra, numerador / denominador))
            res[categoria] = lista_palabras
        return res

    def probabilidad_csv(self):
        pvoc = self.Probabilidades_vocabulario()
        pcat = self.Probabilidades_categorias()
        documentocsv = 'Datos/probabilidad.csv'
        csvsalida = open(documentocsv, 'w', newline='')
        lista_palabras = self.lista_vocabulario
        lista_palabras.append('pcategoria')
        salida = csv.DictWriter(csvsalida, fieldnames=lista_palabras)
        # Indica que hay cabecera, es obligatorio con DictWriter
        salida.writeheader()
        # Rellena el diccionario con todas las palabras, para el header del csv
        valores = OrderedDict()
        for palabra in lista_palabras:
            valores.update({palabra: 0})
        # Rellenamos con el vector peso en cada fila
        for categoria in self.categorias:
            valores = dict.fromkeys(valores, 0)
            lista_tupla = pvoc.get(categoria)
            for tupla in lista_tupla:
                valores[tupla[0]] = tupla[1]

            valor = [x[1] for x in pcat if x[0] == categoria]
            valores['pcategoria'] = valor[0]
            salida.writerow(valores)

        del salida
        csvsalida.close()
        print("Creado fichero '{}' que contiene las probabilidades de las categorias".format(documentocsv))


c = ClasificacionNB()
# print("Probabilidades de las categorias:\n", c.Probabilidades_categorias())
# print("Probabilidades del vocabulario:\n", c.Probabilidades_vocabulario())
c.probabilidad_csv()
