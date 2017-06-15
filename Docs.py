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
    root = "Documentos"
    # Las palabras_comunes las empleamos para que el algoritmo sea más eficiente.
    palabras_comunes = ['a', 'ante', 'bajo', 'cabe', 'con', 'contra', 'de', 'desde', 'en', 'entre', 'hacia', 'hasta',
                        'para', 'por', 'según', 'sin', 'so', 'sobre', 'tras', 'durante', 'mediante', 'excepto', 'salvo',
                        'incluso', 'más', 'menos', 'no', 'si', 'sí', 'el', 'la', 'los', 'las', 'un', 'una', 'unos',
                        'unas', 'este', 'esta', 'estos', 'estas', 'aquel', 'aquella', 'aquellos', 'aquellas', 'he',
                        'has', 'ha', 'hemos', 'habéis', 'han', 'había', 'habías', 'habíamos', 'habíais', 'habían',
                        'además', 'ahora', 'alguna', 'al', 'algún', 'alguno', 'algunos', 'algunas', 'mi', 'mis',
                        'misma', 'mismo', 'muchas', 'muchos', 'y', 'algo', 'antes', 'del', 'ellas', 'eso', 'muy', 'que',
                        'su', 'sus', 'ya', 'él', 'éste', 'ésta', 'ahí', 'allí', 'como', 'cuando', 'era', 'es', 'le',
                        'me', 'lo', 'pero', 'qué', 'también', 'te', 'yo', 'tu', 'el', 'nosotros', 'vosotros', 'después',
                        'se', 'o', 'n', 's']

    # Constructor que coge los documentos de la ruta indicada en scandir
    # y guarda los nombres en una lista de documentos.
    def __init__(self, root=root):
        res = {}
        # r= devuelve el directorio, dirs = categoria,
        # files= el contenido del directorio
        for r, dirs, files in os.walk(root):
            documentos = []
            for file in files:
                with open(os.path.join(r, file), "r") as f:
                    documentos.append(f.read())
                    f.close()
            categoria = r.replace(root + os.sep, '')
            # Quitamos la primera iteración porque la primera vez realiza un recorrido
            # por el directorio, por lo que no se carga ningún directorio. dirs se carga
            # en la lista de subdirectorios en la primera iteración, pero en las siguientes
            # ya se encuentra cargada en r.
            if len(dirs) == 0:
                res[categoria] = documentos
        self.docs = res
        self.categorias = list(res.keys())
        self.num_docs = len(self.docs) + 1

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
                palabras = re.findall(r"[\w]+", documento)
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
        for categoria in self.categorias:
            lista_docs = []
            for documentos in docs[categoria]:
                for palabras in documentos:
                    lista_docs.append(palabras)
            c = Counter(lista_docs).most_common(20)
            res[categoria] = [c[i][0] for i in range(len(c))]
        return res

    def documentos_csv(self):
        frec = self.frecuencia()
        vocabulario = self.vocabulario()
        documentocsv= 'documentos.csv'
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
        frec = {}
        for i in range(0, len(docs)):
            for palabra in docs[i]:
                # print("Documento {}".format(i), palabra)
                if palabra in frec.keys() and frec[palabra][0] != i:
                    frec[palabra][1] += 1
                else:
                    frec[palabra] = [i, 1]
        for palabra in frec.keys():
            frec[palabra] = frec.get(palabra)[1]
        return frec

    # log(N/frec_documental) -> N=nº total de documentos
    def frecuencia_documental_inversa(self):
        frec_doc = self.frecuencia_documental()
        res = {}
        for palabra in frec_doc:
            # print("{} = {}".format(palabra,self.num_docs/frec_doc[palabra]))
            res[palabra] = math.log10(self.num_docs / frec_doc[palabra])
        return res

    # Para cada documento tenemos que calcular el peso:
    # Wi= frecuencia · frec_doc_inversa
    def peso(self):
        frec = self.frecuencia()
        frec_inversa = self.frecuencia_documental_inversa()
        pesos = []
        for documentos in range(len(frec)):
            peso = []
            for tuplas in range(len(frec[documentos])):
                # print("inv",frec_inversa.get(frec[i][0]))
                peso.append((frec[documentos][tuplas][0],
                             frec_inversa.get(frec[documentos][tuplas][0]) *
                             frec[documentos][tuplas][1]))
            pesos.append(peso)
        return pesos

    # 2.2 Proximidad entre documentos y consultas
    # numpy.dot(lista_w[1], v) -> Multiplicación escalar
    def proximidad(self, v):
        pesos = self.peso()
        lista_w = []
        [lista_w.append([i[1] for i in w]) for w in pesos]
        res = []
        for i in range(len(lista_w)):
            # print("divisor{}:".format(i), np.dot(lista_w[i], v))
            # print("dividendo{}:".format(i), (math.sqrt(np.dot(lista_w[i], lista_w[i])) *
            #                                  math.sqrt(np.dot(v, v))))
            res.append(np.dot(lista_w[i], v) /
                       (math.sqrt(np.dot(lista_w[i], lista_w[i])) *
                        math.sqrt(np.dot(v, v))))
        return res
