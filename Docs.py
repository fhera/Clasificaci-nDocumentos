from io import open
from collections import Counter
import numpy as np
import math
import os
import re  # Expresiones regulares


class Docs():
    docs = {}
    categorias = []
    num_docs = 0
    root = "Documentos"
    palabras_comunes = ['a','ante','bajo','cabe','con','contra','de','desde','en','entre','hacia','hasta','para','por',
                        'según','sin','so','sobre','tras','durante','mediante','excepto','salvo','incluso','más','menos',
                        'no','si','sí','el','la','los','las','un','una','unos','unas','este','esta','estos','estas',
                        'aquel','aquella','aquellos','aquellas','he','has','ha','hemos','habéis','han','había','habías',
                        'habíamos','habíais','habían','además','ahora','alguna','al','algún','alguno','algunos','algunas',
                        'mi','mis','misma','mismo','muchas','muchos','y','algo','antes','del','ellas','eso','muy','que',
                        'su','sus','ya','él','éste','ésta','ahí','allí','como','cuando','era','es','le','me','lo','pero',
                        'qué','también','te','yo','tu','el''nosotros','vosotros','después','se','siempre']

    # Constructor que coge los documentos de la ruta indicada en scandir
    # y guarda los nombres en una lista de documentos.
    def __init__(self, root=root):
        documentos = []
        res = {}
        # r= devuelve el directorio, dirs = categoria,
        # files= el contenido del directorio
        for r, dirs, files in os.walk(root):
            for file in files:
                with open(os.path.join(r, file), "r") as f:
                    documentos.append(f.read())
                    f.close()

            res[''] = documentos
        self.docs = res
        self.categorias = list(res.keys())
        self.num_docs = len(self.docs) + 1

    # Transforma el texto de cada documento en una lista de palabras
    def lista_palabras(self):
        documentos_por_categoria = self.docs
        res = {}
        lista_palabras = []
        for categoria in self.categorias:
            for documento in documentos_por_categoria[categoria]:
                # palabras = documento.replace("\n", "").split(' ')
                palabras = re.findall(r"[\w]+", documento)
                # Esto es por si queremos ordenar las palabras
                palabras = sorted([i.lower() for i in palabras])
                lista_palabras.append([i for i in palabras if i not in self.palabras_comunes])
            res[categoria] = lista_palabras
        return res

    # Frecuencia con la que aparece una palabra en cada documento
    def frecuencia(self):
        docs = self.lista_palabras()
        frec = {}
        # En palabras_por_categoria guardamos todas las palabras que aparecen en todos los docs
        for categoria in self.categorias:
            for documentos in docs[categoria]:
                c = Counter(documentos)
            frec[categoria] = list(c.items())
        return frec

    # 4.4 definir el vocabulario, unas 20 palabras clave por cada categoría
    def vocabulario(self):
        for categoria in self.docs['categoria']:
            palabras_frecuentes = self.frecuencia()

        print(palabras_frecuentes)

    # Nº de veces que aparece una palabra en documentos distintos
    def frecuencia_documental(self):
        docs = self.lista_palabras()
        frec = {}
        for i in range(len(docs)):
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
