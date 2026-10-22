lista_solicitudes = []
archivo_creador = open("solicitudes.txt", "a", encoding="utf-8")
archivo_creador.close()

def cargar_solicitudes():
    archivo = open("solicitudes.txt", "r", encoding="utf-8")
    for linea in archivo:
        datos = linea.strip().split("|")
        if len(datos) >= 7:
            lista_solicitudes.append(datos)
    archivo.close()