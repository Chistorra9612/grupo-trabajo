import os
import json
import re
import datetime

# Diccionario global para almacenar los clientes (tabla hash)
clientes = {}

# Función para validar el nombre del cliente
def validar_nombre_cliente(nombre_cliente):
    if not nombre_cliente or len(nombre_cliente) == 0:
        return False, "El nombre del cliente no puede estar vacío."
    
    # Asegurarnos de que no haya caracteres especiales
    if not re.match("^[a-zA-Z0-9_]+$", nombre_cliente):
        return False, "El nombre del cliente solo puede contener letras, números y guiones bajos."
    
    return True, ""

# Función para crear un nuevo cliente
def crear_cliente(nombre_cliente, descripcion_servicio):
    if nombre_cliente in clientes:
        print(f"El cliente {nombre_cliente} ya existe en la tabla hash.")
        return
    
    nombre_archivo = f"{nombre_cliente}.json"
    
    cliente_data = {
        "nombre_cliente": nombre_cliente,
        "descripcion_servicio": descripcion_servicio
    }
    
    # Guardamos el cliente en la tabla hash (diccionario)
    clientes[nombre_cliente] = nombre_archivo
    
    # Escribir el archivo JSON para el cliente
    with open(nombre_archivo, 'w') as archivo:
        json.dump(cliente_data, archivo, indent=4)
    
    print(f"Cliente {nombre_cliente} creado con éxito.")

# Función para leer la información de un cliente existente
def leer_cliente(nombre_cliente):
    if nombre_cliente not in clientes:
        print(f"El cliente {nombre_cliente} no existe en la tabla hash.")
        return
    
    nombre_archivo = clientes[nombre_cliente]
    
    if os.path.exists(nombre_archivo):
        with open(nombre_archivo, 'r') as archivo:
            cliente_data = json.load(archivo)
            print(json.dumps(cliente_data, indent=4))
    else:
        print(f"El archivo para el cliente {nombre_cliente} no se encontró.")

# Función para modificar la información de un cliente
def modificar_cliente(nombre_cliente, nueva_descripcion):
    if nombre_cliente not in clientes:
        print(f"El cliente {nombre_cliente} no existe en la tabla hash.")
        return
    
    nombre_archivo = clientes[nombre_cliente]
    
    if os.path.exists(nombre_archivo):
        with open(nombre_archivo, 'r') as archivo:
            cliente_data = json.load(archivo)
        
        # Modificar la descripción del servicio
        cliente_data["descripcion_servicio"] = nueva_descripcion
        
        # Guardar el historial de cambios
        guardar_historial(nombre_cliente, f"Descripción cambiada a: {nueva_descripcion}")
        
        # Escribir los cambios en el archivo
        with open(nombre_archivo, 'w') as archivo:
            json.dump(cliente_data, archivo, indent=4)
        
        print(f"Información del cliente {nombre_cliente} modificada.")
    else:
        print(f"El archivo para el cliente {nombre_cliente} no se encontró.")

# Función para borrar un cliente
def borrar_cliente(nombre_cliente):
    if nombre_cliente not in clientes:
        print(f"El cliente {nombre_cliente} no existe en la tabla hash.")
        return
    
    nombre_archivo = clientes[nombre_cliente]
    
    if os.path.exists(nombre_archivo):
        os.remove(nombre_archivo)
        print(f"El archivo para el cliente {nombre_cliente} ha sido borrado.")
        
        # Eliminar al cliente de la tabla hash
        del clientes[nombre_cliente]
        print(f"El cliente {nombre_cliente} ha sido borrado de la tabla hash.")
    else:
        print(f"El archivo para el cliente {nombre_cliente} no se encontró.")

# Función para guardar el historial de cambios
def guardar_historial(nombre_cliente, cambio):
    fecha_hora = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    historial_archivo = f"{nombre_cliente}_historial.txt"
    
    with open(historial_archivo, 'a') as archivo_historial:
        archivo_historial.write(f"{fecha_hora}: {cambio}\n")

# Función para listar todos los clientes
def listar_clientes():
    if clientes:
        print("\nClientes existentes en la tabla hash:")
        for cliente in clientes:
            print(cliente)
    else:
        print("No hay clientes registrados en la tabla hash.")

# Función principal para interactuar con el programa
def menu():
    while True:
        print("\nOpciones:")
        print("1. Crear un nuevo cliente")
        print("2. Leer la información de un cliente existente")
        print("3. Modificar la información de un cliente")
        print("4. Borrar un cliente")
        print("5. Listar todos los clientes")
        print("6. Salir")
        
        opcion = input("Elige una opción: ")
        
        if opcion == '1':
            nombre_cliente = input("Introduce el nombre del cliente: ")
            valido, mensaje = validar_nombre_cliente(nombre_cliente)
            if not valido:
                print(mensaje)
                continue
            descripcion_servicio = input("Introduce la descripción del servicio: ")
            crear_cliente(nombre_cliente, descripcion_servicio)
        elif opcion == '2':
            nombre_cliente = input("Introduce el nombre del cliente: ")
            leer_cliente(nombre_cliente)
        elif opcion == '3':
            nombre_cliente = input("Introduce el nombre del cliente: ")
            nueva_descripcion = input("Introduce la nueva descripción del servicio: ")
            modificar_cliente(nombre_cliente, nueva_descripcion)
        elif opcion == '4':
            nombre_cliente = input("Introduce el nombre del cliente a borrar: ")
            borrar_cliente(nombre_cliente)
        elif opcion == '5':
            listar_clientes()
        elif opcion == '6':
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida, por favor elige de nuevo.")

# Ejecutar el menú
if __name__ == "__main__":
    menu()
