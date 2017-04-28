from io import open
import os

class Documentos():
    # def __init__(self, doc):
    #     self.documentos = doc

    def documentos(self):
        lista_documentos = []
        with os.scandir("./Documentos") as it:
            for entry in it:
                if not entry.name.startswith('.') and entry.is_file():
                    lista_documentos.append(entry.name)
        return lista_documentos

    def leer_documento(self):
        lista_documentos = self.documentos()

        for i in range(len(lista_documentos)):
            fichero = open("Documentos/{}".format(lista_documentos[i]), "r")
            texto = fichero.readlines()
            print (texto)
            fichero.close()


    def frecuencia(self):
        pass
    def frecuencia_documental(self):
        pass
    def frecuencia_documental_inversa(self):
        pass
    def peso(self):
        pass

doc = Documentos()
doc.leer_documento()
