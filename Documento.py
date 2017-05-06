from io import open
from collections import Counter
import numpy as np
import math
import os


class Documentos():
    documentos = ()
    num_docs = 0

    # Constructor que coge los documentos de la ruta indicada en scandir
    # y guarda los nombres en una lista de documentos.
    def __init__(self, root):
        docs = []
        tipos = []
        for r, dirs, files in os.walk(root):
            for file in files:
                with open(os.path.join(r, file), "r") as f:
                    docs.append(f.read())
                tipos.append(r.replace(root, ''))
        self.documentos = dict([('docs', docs), ('tipos', tipos)])
        self.num_docs = len(self.documentos) + 1

    # Lee del archivo de palabras que no son claves, las palabras.
    def leer_palabras_no_claves(self):
        palabras_no_claves = []
        fichero = open("PalabrasNoClaves/palabras.txt", "r")
        text = fichero.readlines()
        fichero.close()
        for palabra in text:
            palabras = palabra.replace("\n", "").split(' ')
            palabras_no_claves.extend(palabras)

        return palabras_no_claves

    # Transforma el texto de cada documento en una lista de palabras
    # TODO: quitar las palabras que no sean claves en el documento
    def lista_palabras(self):
        lista = self.documentos['docs']
        palabras_no_claves = self.leer_palabras_no_claves()
        lista_palabras = []
        lista_palabras_def = []
        for palabra in lista:
            palabras = palabra.replace("\n", "").split(' ')
            # Esto es por si queremos ordenar las palabras
            palabras = sorted(palabras)
            lista_palabras.append([i.lower() for i in palabras])
        # El siguiente bucle va a quitar las palabrasNoClave
        for peque_lista in lista_palabras:
            palabras_limpias = []
            for i in peque_lista:
                if i not in palabras_no_claves:
                    palabras_limpias.append(i)
            lista_palabras_def.append(palabras_limpias)
        return lista_palabras_def

    # Frecuencia con la que aparece una palabra en cada documento
    def frecuencia(self):
        docs = self.lista_palabras()
        frec = []
        # En res guardamos todas las palabras que aparecen en todos los docs
        res = [palabra for palabras in docs for palabra in palabras]
        c = Counter()
        for palabras in docs:
            for palabra in res:
                c[palabra] = 0
            c.update(palabras)
            frec.append(sorted(list(c.items())))  # Sorted ordena por orden natural
        return frec

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


# doc = Documentos("./Documentos")
# print("Listamos las palabras que no queremos: \n", doc.leer_palabras_no_claves())
# print("Listamos las palabras de los documentos:\n", doc.lista_palabras())
# print("Frecuencia de palabras en los docs:\n", doc.frecuencia())
# print("Frecuencia docs:\n", doc.frecuencia_documental())
# print("Frecuencia docs inversa:\n", doc.frecuencia_documental_inversa())
# print("Peso:\n", doc.peso())
# print("Proximidad:", doc.proximidad([0.1761, 0, 0, 0, 0, 0, 0, 0.1761, 0.4771]))
