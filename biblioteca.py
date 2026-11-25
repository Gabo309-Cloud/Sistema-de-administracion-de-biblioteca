import json
import os

ARCHIVO = "datos.json"

def cargar_libros():
    if os.path.exists(ARCHIVO):
        with open(ARCHIVO, "r", encoding="utf-8") as archivo:
            return json.load(archivo)
    return []


def guardar_libros(libros):
    with open(ARCHIVO, "w", encoding="utf-8") as archivo:
        json.dump(libros, archivo, indent=4, ensure_ascii=False)


def registrar_libro(libros):
    print("\n--- REGISTRAR LIBRO ---")

    titulo = input("Ingrese el título: ").strip()
    autor = input("Ingrese el autor: ").strip()

    if not titulo or not autor:
        print("El título y el autor son obligatorios.")
        return

    nuevo_libro = {
        "id": max((libro["id"] for libro in libros), default=0) + 1,
        "titulo": titulo,
        "autor": autor,
        "disponible": True
    }

    libros.append(nuevo_libro)
    guardar_libros(libros)

    print("Libro registrado correctamente.")


def mostrar_libros(libros):
    print("\n--- LISTA DE LIBROS ---")

    if not libros:
        print("No hay libros registrados.")
        return

    for libro in libros:
        estado = "Disponible" if libro["disponible"] else "Prestado"

        print(f"ID: {libro['id']}")
        print(f"Título: {libro['titulo']}")
        print(f"Autor: {libro['autor']}")
        print(f"Estado: {estado}")
        print("------------------------")


def buscar_libro(libros):
    print("\n--- BUSCAR LIBRO ---")

    busqueda = input("Ingrese el título o autor: ").strip().lower()

    encontrados = [
        libro for libro in libros
        if busqueda in libro["titulo"].lower()
        or busqueda in libro["autor"].lower()
    ]

    if encontrados:
        mostrar_libros(encontrados)
    else:
        print("No se encontraron libros.")


def prestar_libro(libros):
    print("\n--- PRESTAR LIBRO ---")

    try:
        identificador = int(input("Ingrese el ID del libro: "))
    except ValueError:
        print("Debe ingresar un número válido.")
        return

    for libro in libros:
        if libro["id"] == identificador:
            if libro["disponible"]:
                libro["disponible"] = False
                guardar_libros(libros)
                print("Préstamo registrado correctamente.")
            else:
                print("El libro ya se encuentra prestado.")
            return

    print("No existe un libro con ese ID.")


def devolver_libro(libros):
    print("\n--- DEVOLVER LIBRO ---")

    try:
        identificador = int(input("Ingrese el ID del libro: "))
    except ValueError:
        print("Debe ingresar un número válido.")
        return

    for libro in libros:
        if libro["id"] == identificador:
            if not libro["disponible"]:
                libro["disponible"] = True
                guardar_libros(libros)
                print("Devolución registrada correctamente.")
            else:
                print("El libro ya se encuentra disponible.")
            return

    print("No existe un libro con ese ID.")
