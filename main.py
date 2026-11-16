from src.diccionarios.menu import iniciar_menu as iniciar_diccionarios
from src.objetos.menu import iniciar_menu as iniciar_objetos


def main():
    while True:
        print("\n========================================")
        print("         PIZZERIA MARTINPAU")
        print("========================================")
        print("Selecciona la version del programa:")
        print("1. Version con diccionarios")
        print("2. Version con objetos y clases")
        print("3. Salir")
        print("========================================")

        opcion = input("Elige una opcion: ").strip()

        if opcion == "1":
            iniciar_diccionarios()
        elif opcion == "2":
            iniciar_objetos()
        elif opcion == "3":
            print("Hasta pronto!")
            break
        else:
            print("Opcion no valida. Introduce 1, 2 o 3.")


if __name__ == "__main__":
    main()
