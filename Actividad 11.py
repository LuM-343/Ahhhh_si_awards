# Programación Avanzada - Actividad No. 11
# Luis Manuel Velásquez González 1502325
# Alejandro Daniel de León González 1502425

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

print("-"*50)
print("Bienvenido a los Quiche Awards")
print("---Ahhhhhhh Siiiii---")
print("-"*50)

while True:
    print("\nOpciones disponibles")
    print("1. Agregar nueva película")
    print("2. Votar por una película")
    print("3. Ver los ganadores")
    print("4. Salir")

    opcion=input("Ingresa una opción: ")
    if opcion=="1":
        print("\nRedirigiendote al portal de nominación ...")
        registro()
    elif opcion=="2":
        print("\nRediregiendote al portal de votación...")
        votar()
    elif opcion=="3":
        print("\nY el ganador es....")
        mostrar_ganadores()
    elif opcion=="4":
        print("\nGracias por participar en los Quiche Awards")
        print("Te esperamos el otro año")
        break
    else:
        print("\nOpción no válida")