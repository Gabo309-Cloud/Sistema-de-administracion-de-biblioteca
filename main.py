from biblioteca import (
    cargar_libros,
    registrar_libro,
    mostrar_libros,
    buscar_libro,
    prestar_libro,
    devolver_libro
)

def menu():
    libros = cargar_libros()

    while True:
        print("\n================================")
        print("     SISTEMA DE BIBLIOTECA")
        print("================================")
        print("1. Registrar libro")
        print("2. Mostrar libros")
        print("3. Buscar libro")
        print("4. Prestar libro")
        print("5. Devolver libro")
        print("6. Salir")
        print("================================")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            registrar_libro(libros)

        elif opcion == "2":
            mostrar_libros(libros)

        elif opcion == "3":
            buscar_libro(libros)

        elif opcion == "4":
            prestar_libro(libros)

        elif opcion == "5":
            devolver_libro(libros)

        elif opcion == "6":
            print("Gracias por utilizar el sistema.")
            break

        else:
            print("Opción inválida. Intente nuevamente.")


if __name__ == "__main__":
    menu()