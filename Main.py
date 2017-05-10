import Genera_documentos
import Docs

############# Generador de documentación ############

# genera = Genera_documentos.Genera_documentos()



####### NEWSPAPER ######## Con este método es más lento
# url = "http://www.abc.es/internacional/20150508/abci-hitler-aniversario-201505022206.html"
# articulo = Article(url)
# articulo.download()
# articulo.parse()
# print(articulo.text)


############# Clase Documentos #################

# doc = Docs.Docs()
# print("Listamos las palabras que no queremos: \n", doc.leer_palabras_no_claves())
# print("Listamos las palabras de los documentos:\n", doc.lista_palabras())
# print("Frecuencia de palabras en los docs:\n", doc.frecuencia())
# print("Frecuencia docs:\n", doc.frecuencia_documental())
# print("Frecuencia docs inversa:\n", doc.frecuencia_documental_inversa())
# print("Peso:\n", doc.peso())
# print("Proximidad:", doc.proximidad([0.1761, 0, 0, 0, 0, 0, 0, 0.1761, 0.4771]))
