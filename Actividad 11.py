

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