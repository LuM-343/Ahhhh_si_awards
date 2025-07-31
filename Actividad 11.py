# Programación Avanzada - Actividad No. 11
# Luis Manuel Velásquez González 1502325
# Alejandro Daniel de León González 1502425

nombres = []
peliculas = {
    "Terror": {},
    "Mejor Guión": {},
    "Mejor Fotografia": {},
    "Animación": {},
    "Romance": {},
    "Comedia": {}
}

def analisis(dato):
    while dato == "":
        print("Ingresa un nombre válido")
        dato = input("Ingresala de nuevo: ").lower().strip()
    return dato

def analisis_categoria(numero):
    while numero < 1 or numero > 6:
        print("La categoría no existe")
        numero = int(input("Ingresala de nuevo: "))
    categorias = list(peliculas.keys())
    return categorias[numero - 1]

def registro():
    while True:
        try:
            print("\nCategorías disponibles")
            for idx, categoria in enumerate(peliculas, 1):
                print(f"{idx}. {categoria}")
            categoria_num = int(input("Ingresa el número de la categoría: "))
            categoria = analisis_categoria(categoria_num)

            pelicula = input("Ingresa la película nueva: ").strip().lower()
            pelicula = analisis(pelicula)
            if pelicula in peliculas[categoria]:
                print("Película ya ingresada")
            else:
                peliculas[categoria][pelicula] = 0
                print(f"Película '{pelicula}' registrada en categoría '{categoria}'")
            break
        except ValueError:
            print("Dato no válido, vuelve a intentarlo")

def votar():
    while True:
        try:
            nombre = input("Ingresa tu nombre: ").strip().lower()
            nombre = analisis(nombre)
            if nombre in nombres:
                print("Lo siento, ya votaste. Ojalá gane tu película favorita")
                return

            print("\nCategorías disponibles para votar:")
            for idx, categoria in enumerate(peliculas, 1):
                print(f"{idx}. {categoria}")
            categoria_num = int(input("Ingresa el número de la categoría: "))
            categoria = analisis_categoria(categoria_num)
            
            print("\nPelículas nominadas:")
            for idx, pelicula in enumerate(peliculas[categoria], 1):
                print(f"{idx}. {pelicula.title()}")
            opcion = int(input("Selecciona el número de la película por la que deseas votar: "))
            seleccion = list(peliculas[categoria].keys())[opcion - 1]

            peliculas[categoria][seleccion] += 1
            nombres.append(nombre)
            print(f"Voto registrado por '{seleccion}' en la categoría '{categoria}'")
            break
        except (ValueError, IndexError):
            print("Dato no válido, vuelve a intentarlo")

def mostrar_ganadores():
    print("\n Ganadores por categoría:")
    for categoria in peliculas:
        if peliculas[categoria]:
            ganadora = max(peliculas[categoria], key=peliculas[categoria].get)
            votos = peliculas[categoria][ganadora]
            print(f"{categoria}: {ganadora.title()} ({votos} votos)")
        else:
            print(f"{categoria}: No hubo películas nominadas")

def ver_resultados():
    for clave, valor in peliculas.items():
        print(f"\nResultados de la categoría {clave}")
        i=1
        for pel, votos in valor.items():
            print(f"{i}. La película {pel} tuvo {votos} votos")
            i+=1
        if i==1:
            print("No hay películas nominadas")
    print("*"*60)

print("-"*50)
print("Bienvenido a los Ahhh Si Awards")
print("---Ahhhhhhh Siiiii---")
print("-"*50)

while True:
    print("\nOpciones disponibles")
    print("1. Agregar nueva película")
    print("2. Votar por una película")
    print("3. Ver votos en tiempo real")
    print("4. Ver los ganadores")
    print("5. Salir")

    opcion=input("Ingresa una opción: ")
    if opcion=="1":
        print("\nRedirigiendote al portal de nominación ...")
        registro()
    elif opcion=="2":
        print("\nRediregiendote al portal de votación...")
        votar()
    elif opcion=="3":
        print("\n¿Quién ganará?, ¡Qué nervios!")
        ver_resultados()
    elif opcion=="4":
        print("\nY el ganador es....")
        mostrar_ganadores()
    elif opcion=="5":
        print("\nGracias por participar en los Quiche Awards")
        print("Te esperamos el otro año")
        break
    else:
        print("\nOpción no válida")