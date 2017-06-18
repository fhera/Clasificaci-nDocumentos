from io import open
from collections import Counter
from collections import OrderedDict
import numpy as np
import math
import os
import re  # Expresiones regulares
import csv


class Docs():
    docs = {}
    categorias = []
    num_docs = 0
    # Las palabras_comunes las empleamos para que el algoritmo sea más eficiente.
    palabras_comunes = ['a', 'ante', 'bajo', 'cabe', 'con', 'contra', 'de', 'desde', 'en', 'entre', 'hacia', 'hasta',
                        'para', 'por', 'según', 'sin', 'so', 'sobre', 'tras', 'durante', 'mediante', 'excepto', 'salvo',
                        'incluso', 'más', 'menos', 'no', 'si', 'sí', 'el', 'la', 'los', 'las', 'un', 'una', 'unos',
                        'unas', 'este', 'esta', 'estos', 'estas', 'aquel', 'aquella', 'aquellos', 'aquellas', 'he',
                        'esa', 'has', 'ha', 'hemos', 'habéis', 'han', 'había', 'habías', 'habíamos', 'habíais', 'cómo',
                        'habían', 'ese', 'además', 'ahora', 'alguna', 'al', 'algún', 'alguno', 'algunos', 'algunas',
                        'mi', 'mis', 'misma', 'mismo', 'muchas', 'muchos', 'y', 'algo', 'antes', 'del', 'ellas', 'eso',
                        'muy', 'que', 'su', 'sus', 'ya', 'él', 'éste', 'ésta', 'ahí', 'allí', 'como', 'cuando', 'era',
                        'es', 'le', 'me', 'lo', 'pero', 'qué', 'también', 'te', 'yo', 'tu', 'el', 'nosotros',
                        'vosotros', 'después', 'se', 'o', 'n', 's', 'son', 'dos', 'esto', 'está', 'están', 'nos', 'ni',
                        'tiene', 'uno', 'hay', 'todos', 'sido', 'usted', 'cada', 'todo', 'fue', 'ser', 'hace', 'mucho',
                        '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', 'entonces', 'solo']

    # Constructor que coge los documentos de la ruta indicada en scandir
    # y guarda los nombres en una lista de documentos.
    def __init__(self, path="Documentos"):
        res = {}
        n = 0
        # r= devuelve el directorio, dirs = categoria,
        # files= el contenido del directorio
        for r, dirs, files in os.walk(path):
            documentos = []
            for file in files:
                n += 1

                with open(os.path.join(r, file), "r") as f:
                    documentos.append(f.read())
                    f.close()
            categoria = r.replace(path + os.sep, '')
            # Quitamos la primera iteración porque la primera vez realiza un recorrido
            # por el directorio, por lo que no se carga ningún directorio. dirs se carga
            # en la lista de subdirectorios en la primera iteración, pero en las siguientes
            # ya se encuentra cargada en r.
            if len(dirs) == 0:
                res[categoria] = documentos
        self.docs = res
        self.categorias = list(res.keys())
        self.num_docs = n

    def leer_doc(self, path="Documentos"):
        categoria = []
        docs = []
        for r, dirs, files in os.walk(path):
            for file in files:
                with open(os.path.join(r, file), "r") as f:
                    docs.append(f.read())
                categoria.append(r.replace(path, ''))
        return dict([('docs', docs), ('categoria', categoria)])

    # Transforma el texto de cada documento en una lista de palabras
    def lista_palabras(self):
        documentos_por_categoria = self.docs
        res = {}
        for categoria in self.categorias:
            lista_palabras = []
            for documento in documentos_por_categoria[categoria]:
                # Con re podemos meter patrones, pero tiene ya patrones
                # predefinidos, con \w coge todas las palabras y quita los
                # símbolos
                palabras = re.findall(r"\w+", documento)
                # Esto es por si queremos ordenar las palabras
                # palabras = sorted([i.lower() for i in palabras])
                palabras = [i.lower() for i in palabras]
                lista_palabras.append([i for i in palabras if i not in self.palabras_comunes])
            res[categoria] = lista_palabras
        return res

    # Frecuencia con la que aparece una palabra en cada documento
    def frecuencia(self):
        docs = self.lista_palabras()
        res = OrderedDict()
        for categoria in self.categorias:
            lista_docs = []
            for documentos in docs[categoria]:
                c = Counter(documentos).items()
                lista_docs.append(sorted(c, key=lambda palabra: palabra[1], reverse=True))
            res[categoria] = lista_docs
        return res

    # 4.4 Definir el vocabulario, unas 20 palabras clave por cada categoría
    #  Devolverá un diccionario con clave:categoría y valor:lista de 20 palabras más repetidas en todos los docs.
    def vocabulario(self):
        docs = self.lista_palabras()
        res = OrderedDict()
        lista_vocabulario = []
        for categoria in self.categorias:
            lista_docs = []
            for documentos in docs[categoria]:
                for palabras in documentos:
                    if palabras not in lista_vocabulario:
                        lista_docs.append(palabras)
            c = Counter(lista_docs).most_common(20)
            res[categoria] = [c[i][0] for i in range(len(c))]
            # Va añadiendo palabras a la lista de vocabulario para comprobar en el if que no se
            # repiten
            lista_vocabulario = [palabra for documentos in res.values() for palabra in documentos]
        return res

    # Guarda el documento en la carpeta Datos
    def documentos_csv(self):
        frec = self.frecuencia()
        vocabulario = self.vocabulario()
        documentocsv = 'Datos/documentos.csv'
        csvsalida = open(documentocsv, 'w', newline='')
        lista_palabras = [palabra for documentos in vocabulario.values() for palabra in documentos]
        lista_palabras.append('Categoria')
        salida = csv.DictWriter(csvsalida, fieldnames=lista_palabras)
        # Indica que hay cabecera, es obligatorio con DictWriter
        salida.writeheader()
        # Rellena el diccionario con todas las palabras, para el header del csv
        valores = OrderedDict()
        for item in lista_palabras:
            valores.update({item: 0})

        for categoria in self.categorias:
            voc = vocabulario[categoria]
            for documentos in frec[categoria]:
                # Resetea a 0 los valores de las claves para cada doc
                valores = dict.fromkeys(valores, 0)
                for palabras in documentos:
                    if palabras[0] in voc:
                        valores[palabras[0]] = palabras[1]
                valores['Categoria'] = categoria
                salida.writerow(valores)
        del salida
        csvsalida.close()

        print("Documento creado en el fichero {}".format(documentocsv))


        # Nº de veces que aparece una palabra en documentos distintos

    def frecuencia_documental(self):
        docs = self.lista_palabras()
        res = OrderedDict()
        lista_docs = []
        for categoria in self.categorias:
            for documentos in docs[categoria]:
                for palabras in documentos:
                    lista_docs.append(palabras)
            c = Counter(lista_docs).items()
            # la iteración siguiente me ordena las palabras por el nº de repeticiones
            # res[categoria] = sorted(c, key=lambda palabra: palabra[1], reverse=True)
            res[categoria] = c
        return res

    # log(N/frec_documental) -> N=nº total de documentos
    def frecuencia_documental_inversa(self):
        frec_doc = self.frecuencia_documental()
        res = OrderedDict()
        vocabulario = self.vocabulario()
        lista_vocabulario = [palabra for documentos in vocabulario.values() for palabra in documentos]
        for categoria in self.categorias:
            for palabra in frec_doc[categoria]:
                pal = palabra[0]
                # print("{} = {}".format(palabra,self.num_docs/frec_doc[palabra]))
                if pal in lista_vocabulario:
                    n = palabra[1]
                    res[palabra[0]] = round(math.log10(self.num_docs / n), 4)
        return res

    # Para cada documento tenemos que calcular el peso:
    # Wi= frecuencia · frec_doc_inversa
    def peso(self):
        frec = self.frecuencia()
        frec_inversa = self.frecuencia_documental_inversa()
        pesos = []
        res = []
        n = 0
        for categoria in self.categorias:
            for documentos in frec[categoria]:
                peso = []
                dict_doc = dict(documentos)
                for tupla in list(frec_inversa.items()):
                    if tupla[0] in dict_doc.keys():
                        peso.append((tupla[0], tupla[1] * dict_doc.get(tupla[0])))
                    else:
                        peso.append((tupla[0], 0))
                pesos.append(peso)
            res = pesos
        return res

    def pesos_csv(self):
        pesos = self.peso()
        vocabulario = self.vocabulario()
        documentocsv = 'Datos/pesos.csv'
        csvsalida = open(documentocsv, 'w', newline='')
        lista_palabras = [palabra for documentos in vocabulario.values() for palabra in documentos]
        lista_palabras.append('Categoria')
        salida = csv.DictWriter(csvsalida, fieldnames=lista_palabras)
        # Indica que hay cabecera, es obligatorio con DictWriter
        salida.writeheader()
        # Rellena el diccionario con todas las palabras, para el header del csv
        valores = OrderedDict()
        for palabra in lista_palabras:
            valores.update({palabra: 0})
        # Rellenamos con el vector peso en cada fila
        for categoria in self.categorias:
            for documentos in pesos:
                # Resetea a 0 los valores de las claves para cada doc
                valores = dict.fromkeys(valores, 0)
                for palabras in documentos:
                    if palabras[0] in lista_palabras:
                        valores[palabras[0]] = palabras[1]
                valores['Categoria'] = categoria
                salida.writerow(valores)
        del salida
        csvsalida.close()

        print("Creado fichero {} que contiene los pesos de los documentos".format(documentocsv))

pruebas = Docs()
# print(pruebas.vocabulario())
# print("Frecuencia:\n", pruebas.frecuencia())
# print("Frec documental:\n", pruebas.frecuencia_documental())
# print("Frec inversa:\n", pruebas.frecuencia_documental_inversa())
# print("Peso:\n", pruebas.peso())
print("Peso a csv:\n", pruebas.pesos_csv())
# print("Proximidad:\n", pruebas.proximidad(pruebas.peso()))
