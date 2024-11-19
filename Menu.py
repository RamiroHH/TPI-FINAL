from juegos.aventura_guemes import guemes
from juegos.san_martin import san_martin
from juegos.juego_preguntados import preguntados

menu = -1 
while menu != 0:
    print("\nBIENVENIDO AL MENÚ DE JUEGOS")
    print("Elige una opción:")
    print("1. Tu aventura histórica")
    print("2. Preguntados")
    print("0. Salir")

    try:
        menu = int(input("Ingresa tu elección: "))
        if menu == 1:
            print("\nElige tu personaje:")
            print("1. San Martín")
            print("2. Güemes")
            opcion_aventura = int(input("Ingresa tu elección: "))

            if opcion_aventura == 1:
                san_martin() 
            elif opcion_aventura == 2:
                guemes() 
            else:
                print("Opción inválida. Por favor, elige 1 o 2.")

        elif menu == 2:
            preguntados() 
        elif menu == 0:
            print("¡Gracias por jugar! Adiós.")
        else:
            print("Opción inválida. Por favor, elige 1, 2 o 0.")
    except ValueError:
        print("Entrada inválida. Por favor, ingresa un número.")
