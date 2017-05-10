from io import open
import os
import feedparser
from newspaper import Article


class Genera_documentos():
    # urls: es una variable que va a contener los feeds de las distintas
    # categorias y sitios webs
    urls = {"Economía": "http://www.abc.es/rss/feeds/abc_Economia.xml",
            "Deportes": "http://www.abc.es/rss/feeds/abc_Deportes.xml",
            "Ciencia": "http://www.abc.es/rss/feeds/abc_Ciencia.xml",
            "Tecnología": "http://www.abc.es/rss/feeds/abc_Tecnologia.xml",
            "Naturaleza": "http://www.abc.es/rss/feeds/abc_Natural.xml",
            "Moda": "http://www.abc.es/rss/feeds/abc_Moda.xml",
            "Historia": "http://www.abc.es/rss/feeds/abc_Historicas.xml",
            "Arte": "http://www.abc.es/rss/feeds/abc_Arte.xml",
            "Cultura": "http://www.abc.es/rss/feeds/abc_ABCCultural.xml",
            "Teatro": "http://www.abc.es/rss/feeds/abc_Teatro.xml"}
    # Directorio por defecto para guardar los documentos
    root = "Documentos"
    root_test = "Test"

    def __init__(self, directorio=root):
        for categoria in self.urls:
            n = 1
            url_doc = feedparser.parse(self.urls[categoria])
            subdir = '/'.join([directorio, categoria])
            # Comprobamos si se encuentra la carpeta con la
            # categoría del documento
            print("Categoria:", categoria)
            if not os.path.exists(subdir):
                os.makedirs(subdir)
            for feed in url_doc.entries:
                name = str(n).zfill(3) + '.dat'
                doc = open(subdir + '/' + name, 'w+')
                try:
                    url = feed.link
                    articulo = Article(url)
                    articulo.download()
                    articulo.parse()
                    titulo = articulo.title + "\n\n"
                    texto = articulo.text
                    print(n, url)
                    # titulo = feed['title'] + "\n\n"
                    # texto = feed['summary'].split('">')[1]
                    # texto = feed['summary']
                    doc.write(titulo)
                    doc.write(texto)
                    doc.close()
                    n = n + 1
                except IndexError:
                    print("La noticia {} no tiene texto.".format(url))



####### NEWSPAPER ######## Con este método es más lento
# url = "http://www.abc.es/internacional/20150508/abci-hitler-aniversario-201505022206.html"
# articulo = Article(url)
# articulo.download()
# articulo.parse()
# print(articulo.text)
