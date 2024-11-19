# Creo la funcion
def san_martin():
   print("Juego de Elección: Cruce de los Andes de San Martín")

# Introducción
   print("Año 1817. Eres el líder del Ejército de los Andes, José de San Martín.")
   print("Debes tomar decisiones críticas para cruzar los Andes y liberar Chile.")

# Variable para almacenar la salud del ejército
   salud_ejercito = 100

# Variable para almacenar la moral del ejército
   moral_ejercito = 100

# Etapa 1: Preparación
   print(" Etapa 1: Preparación")
   print("Debes elegir un lugar para acampar y preparar al ejército.")
   print("A) Mendoza")
   print("B) San Juan")
   print("C) La Rioja")
   print("D) San Luis")

   eleccion = input("Elige una opción: ")

   if eleccion.upper() == "A":
       print("Excelente elección. Mendoza es un lugar estratégico.")
       salud_ejercito += 10
       print("Salud del ejercito + 10")
       moral_ejercito += 10
       print("Moral del ejercito + 10")
   elif eleccion.upper() == "B":
       print("Buena elección. San Juan ofrece recursos naturales.")
       salud_ejercito += 5
       print("Salud del ejercito + 5")
       moral_ejercito += 5
       print("Moral del ejercito + 5")
   elif eleccion.upper() == "C":
       print("Mala elección. La Rioja es un lugar peligroso.")
       salud_ejercito -= 10
       print("Salud del ejercito - 10")
       moral_ejercito -= 10
       print("Moral del ejercito + 10")
   elif eleccion.upper() == "D":
       print("Buena elección. San Luis ofrece una posición defensiva.")
       salud_ejercito += 5
       print("Salud del ejercito + 5")
       moral_ejercito += 5
       print("Moral del ejercito + 5")
   else:
       print("Opción inválida.")

# Etapa 2: Cruce de los Andes
   print(" Etapa 2: Cruce de los Andes")
   print("Debes elegir una ruta para cruzar los Andes.")
   print("A) Ruta del Portillo")
   print("B) Ruta de Uspallata")
   print("C) Ruta de Los Patos")
   print("D) Ruta de Villalobos")

   eleccion = input("Elige una opción: ")

   if eleccion.upper() == "A":
       print("Excelente elección. La ruta del Portillo es segura.")
       salud_ejercito += 10
       print("Salud del ejercito + 10")
       moral_ejercito += 10
       print("Moral del ejercito + 10")
   elif eleccion.upper() == "B":
       print("Buena elección. La ruta de Uspallata es rápida.")
       salud_ejercito += 5
       print("Salud del ejercito + 5")
       moral_ejercito += 5
       print("Moral del ejercito + 5")
   elif eleccion.upper() == "C":
       print("Mala elección. La ruta de Los Patos es peligrosa.")
       salud_ejercito -= 10
       print("Salud del ejercito - 10")
       moral_ejercito -= 10
       print("Moral del ejercito - 10")
   elif eleccion.upper() == "D":
       print("Buena elección. La ruta de Villalobos es sorprendente.")
       salud_ejercito += 5
       print("Salud del ejercito + 5")
       moral_ejercito += 5
       print("Moral del ejercito + 5")
   else:
       print("Opción inválida.")

# Etapa 3: Batalla de Chacabuco
   print(" Etapa 3: Batalla de Chacabuco")
   print("Debes elegir una estrategia para la batalla.")
   print("A) Ataque frontal")
   print("B) Flanqueo")
   print("C) Retirada")
   print("D) Emboscada")

   eleccion = input("Elige una opción: ")

   if eleccion.upper() == "A":
       print("Excelente elección. El ataque frontal es efectivo.")
       salud_ejercito += 10
       print("Salud del ejercito + 10")
       moral_ejercito += 10
       print("Moral del ejercito + 10")
   elif eleccion.upper() == "B":
       print("Buena elección. El flanqueo es sorprendente.")
       salud_ejercito += 5
       print("Salud del ejercito + 5")
       moral_ejercito += 5
       print("Moral del ejercito + 5")
   elif eleccion.upper() == "C":
       print("Mala elección. La retirada es cobardía.")
       salud_ejercito -= 10
       print("Salud del ejercito - 10")
       moral_ejercito -= 10
       print("Moral del ejercito - 10")
   elif eleccion.upper() == "D":
       print("Buena elección. La emboscada es efectiva.")
       salud_ejercito += 5
       print("Salud del ejercito + 5")
       moral_ejercito += 5
       print("Moral del ejercito + 5")
   else:
       print("Opción inválida.")

# Etapa 4: Avance hacia Santiago
   print(" Etapa 4: Avance hacia Santiago")
   print("Debes elegir una ruta para avanzar hacia Santiago.")
   print("A) Ruta directa por la carretera")
   print("B) Ruta alternativa por los cerros")
   print("C) Ruta fluvial por el río Mapocho")
   print("D) Ruta de infiltración en la noche")

   eleccion = input("Elige una opción: ")

   if eleccion.upper() == "A":
      print("Excelente elección. La ruta directa es rápida.")
      salud_ejercito += 10
      print("Salud del ejercito + 10")
      moral_ejercito += 10
      print("Moral del ejercito + 10")
   elif eleccion.upper() == "B":
      print("Buena elección. La ruta alternativa es segura.")
      salud_ejercito += 5
      print("Salud del ejercito + 5")
      moral_ejercito += 5
      print("Moral del ejercito + 5")
   elif eleccion.upper() == "C":
      print("Mala elección. La ruta fluvial es lenta.")
      salud_ejercito -= 10
      print("Salud del ejercito - 10")
      moral_ejercito -= 10
      print("Moral del ejercito - 10")
   elif eleccion.upper() == "D":
      print("Buena elección. La ruta de infiltración es sorprendente.")
      salud_ejercito += 5
      print("Salud del ejercito + 5")
      moral_ejercito += 5
      print("Moral del ejercito + 5")
   else:
      print("Opción inválida.")

# Etapa 5: Batalla de Maipú
   print(" Etapa 5: Batalla de Maipú")
   print("Debes elegir una estrategia para la batalla.")
   print("A) Ataque frontal")
   print("B) Flanqueo")
   print("C) Retirada")
   print("D) Emboscada")

   eleccion = input("Elige una opción: ")

   if eleccion.upper() == "A":
      print("Excelente elección. El ataque frontal es efectivo.")
      salud_ejercito += 10
      print("Salud del ejercito + 10")
      moral_ejercito += 10
      print("Moral del ejercito + 10")
   elif eleccion.upper() == "B":
      print("Buena elección. El flanqueo es sorprendente.")
      salud_ejercito += 5
      print("Salud del ejercito + 5")
      moral_ejercito += 5
      print("Moral del ejercito + 5")
   elif eleccion.upper() == "C":
      print("Mala elección. La retirada es cobardía.")
      salud_ejercito -= 10
      print("Salud del ejercito - 10")
      moral_ejercito -= 10
      print("Moral del ejercito - 10")
   elif eleccion.upper() == "D":
      print("Buena elección. La emboscada es efectiva.")
      salud_ejercito += 5
      print("Salud del ejercito + 5")
      moral_ejercito += 5
      print("Moral del ejercito + 5")
   else:
      print("Opción inválida.")

# Resultado final
   print("Resultado final:")
   print("Salud del ejército:", salud_ejercito)
   print("Moral del ejército:", moral_ejercito)

   if salud_ejercito > 80 and moral_ejercito > 80:
      print("¡Felicidades! Has ganado la campaña y liberado Chile.")
   else:
      print("Lo siento. Has perdido la campaña y el ejército está debilitado.")

   print("Fin de la historia")