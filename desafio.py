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

def registrar_solicitud():
    print("\n--- Registrar Solicitud ---")
    nombre = input("Nombre: ")
    dni = input("DNI: ")
    distrito = input("Distrito: ")
    recurso = input("Recurso solicitado: ")
    cant_personas_afect = input("Cantidad de personas afectadas: ")
    
    if not validar_datos(nombre, dni, distrito, recurso, cant_personas_afect):
        print("\nDatos inválidos.")
        return
    
    personas = int(cant_personas_afect)
    urgencia = calcular_urgencia(recurso, personas)
    numero = len(lista_solicitudes) + 1
    codigo = f"SOL-{numero:03d}"
    
    archivo = open("solicitudes.txt", "a", encoding="utf-8")
    archivo.write(codigo + "|" + nombre + "|" + dni + "|" + distrito + "|" + recurso + "|" + str(personas) + "|" + urgencia + "\n")
    archivo.close()
    
    lista_solicitudes.append([codigo, nombre, dni, distrito, recurso, str(personas), urgencia])
    print(f"\nSolicitud registrada correctamente. Código asignado: {codigo}")