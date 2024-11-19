def preguntados():

    import json
    import random

    # Cargar preguntas desde el archivo JSON
    with open('C:/Users/Ignacio/Desktop/CARPETA FINAL/preguntas_preguntados.json', 'r', encoding='utf-8') as file:
        preguntas_por_categoria = json.load(file)

    # Inicializamos puntajes de los jugadores en 0
    puntaje_1 = 0
    puntaje_2 = 0

    # Inicializar la lista de preguntas usadas para no repetirlas
    preguntas_usadas_1 = []
    preguntas_usadas_2 = []

    # Mensaje inicial
    print("""                                                                                                  
     #####    #####    ######    #####   ##  ##   ##  ##   ######     ##     ####      ####     ####
     ##  ##   ##  ##   ##       ##       ##  ##   ### ##     ##      ####    ## ##    ##  ##   ##
     ##  ##   ##  ##   #####    ##       ##  ##   ######     ##     ##  ##   ##  ##   ##  ##    ####
     #####    #####    ##       ## ###   ##  ##   ######     ##     ##  ##   ##  ##   ##  ##       ##
     ##       ## ##    ##       ##  ##   ##  ##   ## ###     ##     ######   ## ##    ##  ##       ##
     ##       ##  ##   ######    #####   ######   ##  ##     ##     ##  ##   ####      ####     ####  

                                        PARA COMENZAR INGRESE "1"                                                                                                                                                                                      
    """)

    start = int(input())

    if start == 1:
        # Ingreso de nombres de jugadores
        jugador1 = input("Ingrese el nombre del jugador 1: ")
        jugador2 = input("Ingrese el nombre del jugador 2: ")

        # Comienzo del juego
        while puntaje_1 < 6 and puntaje_2 < 6:
            # Turno del jugador 1
            print(f"Turno de {jugador1}")
            while True:
                categoria_actual = random.choice(list(preguntas_por_categoria.keys()))
                preguntas_no_usadas = [
                    pregunta for pregunta in preguntas_por_categoria[categoria_actual] if pregunta not in preguntas_usadas_1
                ]

                if not preguntas_no_usadas:
                    print(f"No hay más preguntas disponibles en la categoría {categoria_actual} para {jugador1}")
                    continue

                pregunta_aleatoria = random.choice(preguntas_no_usadas)
                preguntas_usadas_1.append(pregunta_aleatoria)

                print(f"Categoría: {categoria_actual}")
                print(pregunta_aleatoria["pregunta"])
                for opcion in pregunta_aleatoria["opciones"]:
                    print(opcion)

                respuesta_usuario = input("¿Cuál es tu respuesta? (A/B/C/D): ").upper()

                if respuesta_usuario == pregunta_aleatoria["respuesta"]:
                    print("¡Correcto!")
                    puntaje_1 += 1
                    break
                else:
                    print("¡Incorrecto!")
                    break

            print(f"{jugador1} tiene {puntaje_1} puntos.\n")

            # Turno del jugador 2
            print(f"Turno de {jugador2}")
            while True:
                categoria_actual = random.choice(list(preguntas_por_categoria.keys()))
                preguntas_no_usadas = [
                    pregunta for pregunta in preguntas_por_categoria[categoria_actual] if pregunta not in preguntas_usadas_2
                ]

                if not preguntas_no_usadas:
                    print(f"No hay más preguntas disponibles en la categoría {categoria_actual} para {jugador2}")
                    continue

                pregunta_aleatoria = random.choice(preguntas_no_usadas)
                preguntas_usadas_2.append(pregunta_aleatoria)

                print(f"Categoría: {categoria_actual}")
                print(pregunta_aleatoria["pregunta"])
                for opcion in pregunta_aleatoria["opciones"]:
                    print(opcion)

                respuesta_usuario = input("¿Cuál es tu respuesta? (A/B/C/D): ").upper()

                if respuesta_usuario == pregunta_aleatoria["respuesta"]:
                    print("¡Correcto!")
                    puntaje_2 += 1
                    break
                else:
                    print("¡Incorrecto!")
                    break

            print(f"{jugador2} tiene {puntaje_2} puntos.\n")

        # Final del juego
        if puntaje_1 >= 6:
            print(f"{jugador1} ha ganado el juego!")
        elif puntaje_2 >= 6:
            print(f"{jugador2} ha ganado el juego!")