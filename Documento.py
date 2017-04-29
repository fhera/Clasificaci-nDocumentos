from io import open
import os


class Documentos():
    documentos = []
    # Constructor que coge los documentos de la ruta indicada en scandir
    # y guarda los nombres en una lista de documentos.
    def __init__(self):
        lista_documentos = []
        with os.scandir("./Documentos") as it:
            for entry in it:
                if not entry.name.startswith('.') and entry.is_file():
                    lista_documentos.append(entry.name)
        self.documentos = lista_documentos

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
                lista_palabras.append(palabras)
        return lista_palabras

    # Frecuencia con la que aparece una palabra en cada documento
    def frecuencia(self):
        docs = self.lista_palabras()
        for palabras in docs:
            for palabra in palabras:
                print("Con la palabra '{}' hay {} coincidencias en el documento {}."
                      .format(palabra, palabras.count(palabra), docs.index(palabras)))


    def frecuencia_documental(self):
        pass

    def frecuencia_documental_inversa(self):
        pass

    def peso(self):
        pass


doc = Documentos()
# doc.leer_documentos()
# doc.lista_palabras()
doc.frecuencia()
