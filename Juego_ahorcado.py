import random as rand   #Importamos la libreria random para seleccionar palabras al azar y la renombramos rand

def obtener_palabra_aleatoria(tematica):
    tematicas = {       #Aqui se almacenan las tematicas que el usuario puede elegir con sus respectivas palabras
        "animales": ["perro","gato","cerdo","caballo","pez"],
        "frutas": ["manzana", "banano", "pera", "mango", "durazno"],
        "paises": ["colombia", "argentina", "brasil", "españa", "estados unidos"],
        "colores": ["amarillo", "blanco", "negro", "morado", "rojo"]
    }
    #Esta parte selecciona una palabra aleatoria de la tematuca elegida
    palabras= tematicas [tematica]
    palabra_aleatoria = rand.choice(palabras)
    return palabra_aleatoria

def seleccionar_tematica():     #Para que el ususario eliga una tematica entre las opciones disponibles
    print("Elige una tematica: ")
    print("1. Animales")
    print("2. Frutas")
    print("3. Países")
    print("4. Colores")

    while True: #Ciclo para asegurar que la opcion elegida por el usuario es valida
        opcion = input("Ingresa el numero de la tematica: ")
        if opcion == "1":
            return "animales"
        elif opcion == "2":
            return "frutas"
        elif opcion == "3":
            return "paises"
        elif opcion == "4":
            return "colores"
        else:
            print("Opcion invalida, por favor, elige 1,2,3 o 4.")


def mostrar_tablero(palabra_secreta, letras_adivinadas):
    #Muestra el tablero actual del juego indicandole al usuario que letras lleva adivinadas y cuanto espacios vacio le faltan
    tablero=""
    for letra in palabra_secreta:
        if letra in letras_adivinadas:  #Recorreo todas las letras de la palabra, si esta en la palabra se agrega al tablero
            tablero+= letra 
        else:
            tablero+=" _ "
    print(tablero)  #Muestra el tablero al jugador

def jugar_ahorcado():   #Funcion principal que ejecuta el juego
    tematica = seleccionar_tematica()
    palabra_secreta = obtener_palabra_aleatoria(tematica)
    letras_adivinadas=[]    #Almacena las letras adivinadas por el jugador
    intentos_restantes= 6   #Numero de intentos que tiene el jugador al iniciar la partida 

    while intentos_restantes>0: #Ciclo principal del juego, se repite mientras tenga intentos disponibles
        mostrar_tablero(palabra_secreta, letras_adivinadas)
        letra = input("Ingrese una letra: ").lower()    #Pedimos al usuario que ingrese una letra

        if letra in letras_adivinadas:  #Le avisa al usuario si la letra que ingreso ya se habia ingresado anteriormente
            print(f"Ya has introducido la letra {letra}, Intente de nuevo")
            continue 

        if letra in palabra_secreta:    #Si la letra esta en la palabra secreta con el append se agrega a letras adivinadas
            letras_adivinadas.append(letra)
            if set(letras_adivinadas)==set(palabra_secreta): #El Set se usa para comprobar si letras adivinadas y palabras secretas son iguales
                print("Felicidades, has adivinado la palabra correctamente")
                break   #Salida del ciclo
        else:   #Si la letra no esta en  la palabra secreta se reduce el numero de intentos
            intentos_restantes-=1
            print(f"La letra {letra} esta incorrecta, te quedan {intentos_restantes}")

    if intentos_restantes==0:
        print(f"Has perdido, la palabra secreta era: {palabra_secreta}")

jugar_ahorcado()    #Llamamos a la funcion principal para ejecutar el juego