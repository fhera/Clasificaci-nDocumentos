import os


with os.scandir("./Documentos") as it:
    for entry in it:
        if not entry.name.startswith('.') and entry.is_file():
            print(entry.name)