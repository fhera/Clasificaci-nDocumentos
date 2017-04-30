from io import open
from collections import Counter
from tabulate import tabulate
import math
import os


class Documentos():
    documentos = []
    num_docs = 0

    # Constructor que coge los documentos de la ruta indicada en scandir
    # y guarda los nombres en una lista de documentos.
    def __init__(self):
        lista_documentos = []
        with os.scandir("./Documentos") as it:
            for entry in it:
                if not entry.name.startswith('.') and entry.is_file():
                    lista_documentos.append(entry.name)
        self.documentos = lista_documentos
        self.num_docs = len(lista_documentos)

    # Lee los documentos y guarda en una lista el texto de cada documento
    def leer_documentos(self):
        lista_documentos = self.documentos
        docs = []
        for i in range(len(lista_documentos)):
            fichero = open("Documentos/{}".format(lista_documentos[i]), "r")
            texto = fichero.readlines()
            fichero.close()
            docs.append(texto)
        return docs

    # Transforma el texto de cada documento en una lista de palabras
    def lista_palabras(self):
        lista = self.leer_documentos()
        lista_palabras = []
        for i in range(len(lista)):
            for documento in lista[i]:
                palabras = documento.replace("\n", "").split(' ')
                lista_palabras.append([i.lower() for i in palabras])
        return lista_palabras

    # Frecuencia con la que aparece una palabra en cada documento
    def frecuencia(self):
        docs = self.lista_palabras()
        frec = []
        for palabras in docs:
            frec.append(Counter(palabras))
        for i in frec:
            print("i:", dict(i))
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

        # print(tabulate(frec))
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
        print(frec)
        pass


doc = Documentos()
# print("Leemos los documentos\n", doc.leer_documentos())
# print("Listamos las palabras de los documentos\n", doc.lista_palabras())
# print("Frecuencia de palabras en los docs\n", doc.frecuencia())
# print("Frecuencia docs\n", doc.frecuencia_documental())
# print("Frecuencia docs inversa\n", doc.frecuencia_documental_inversa())
doc.peso()