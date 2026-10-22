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

def validar_datos(nombre, dni, distrito, recurso, personas_str):
    if not nombre.strip() or not dni.strip() or not distrito.strip() or not recurso.strip():
        return False
    if not personas_str.isdigit() or int(personas_str) <= 0:
        return False
    return True

def calcular_urgencia(recurso, personas):
    if recurso.lower() in ["agua", "medicamentos", "medicinas"]:
        if personas >= 20:
            return "Crítico"
        elif personas >= 5:
            return "Alto"
        else:
            return "Medio"
    else:
        if personas >= 20:
            return "Alto"
        elif personas >= 5:
            return "Medio"
        else:
            return "Bajo"

def leer_solicitudes():
    print("\nLista de Solicitudes")
    archivo = open("solicitudes.txt", "r", encoding="utf-8")
    lineas = archivo.readlines()
    archivo.close()
    if not lineas:
        print("No hay registros guardados en el archivo.")
        return
    for linea in lineas:
        print(linea.strip())

def buscar_solicitud():
    print("\nBúsqueda Secuencial")
    codigo_buscado = input("Ingrese el código a buscar (Ej: SOL-001): ").strip()
    encontrado = False
    for s in lista_solicitudes:
        if s[0].lower() == codigo_buscado.lower():
            print(f"\nSolicitud encontrada")
            print(f"Código   : {s[0]}")
            print(f"Nombre   : {s[1]}")
            print(f"DNI      : {s[2]}")
            print(f"Distrito : {s[3]}")
            print(f"Recurso  : {s[4]}")
            print(f"Personas : {s[5]}")
            print(f"Urgencia : {s[6]}")
            encontrado = True
            break
    if not encontrado:
        print("\nSolicitud no encontrada.")

def listar_ordenadas():
    print("\nListado Priorizado")
    if not lista_solicitudes:
        print("No hay registros para ordenar.")
        return
    copia_lista = []
    for s in lista_solicitudes:
        copia_lista.append(list(s))
    for i in range(1, len(copia_lista)):
        actual = copia_lista[i]
        j = i - 1
        while j >= 0 and int(copia_lista[j][5]) < int(actual[5]):
            copia_lista[j + 1] = copia_lista[j]
            j -= 1
        copia_lista[j + 1] = actual
    for s in copia_lista:
        print(f"Código: {s[0]} | Nombre: {s[1]} | Recurso: {s[4]} | Personas: {s[5]} | Urgencia: {s[6]}")