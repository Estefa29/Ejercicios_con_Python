#  Realice un algoritmo que permita diseñar un sudoku, donde se debe de ingresar 
# inicialmente la posición aleatoria de los valores con los cuales se va iniciar, 
# luego deberá comenzar el juego y validar las jugadas, si excede el valor total por
#  columnas o filas deberá emitir un mensaje de error.
import numpy as np

def check_sudoku(grid):
    """ Return True if grid is a valid Sudoku square, otherwise False. """
    for i in range(9):
        # j, k index top left hand corner of each 3x3 tile
        j, k = (i // 3) * 3, (i % 3) * 3
        if len(set(grid[i,:])) != 9 or len(set(grid[:,i])) != 9\
                or len(set(grid[j:j+3, k:k+3].ravel())) != 9:
            return False
    return True

sudoku = """245327698
            839654127
            672918543
            496185372
            218473956
            753296481
            367542819
            984761235
            521839764"""
# Turn the provided string, sudoku, into an integer array
grid = np.array([[int(i) for i in line] for line in sudoku.split()])
print(grid)

if check_sudoku(grid):
    print('cuadricula valida')
else:
    print('cuadricula invalida')

    # Realice un algoritmo que permita hacer un ahorcadito,
    #  la matriz permitirá almacenar las palabras, se recomienda que las palabras tengan 
    # el mismo tamaño para evitar reasignar el valor o tamaño de la matriz.
import random
AHORCADO = ['''
    +---+
    |   |
        |
        |
        |
        |
=========''', '''
    +---+
    |   |
    O   |
        |
        |
        |
=========''', '''
    +---+
    |   |
    O   |
    |   |
        |
        |
=========''', '''
    +---+
    |   |
    O   |
    /|   |
        |
        |
=========''', '''
    +---+
    |   |
    O   |
    /|\  |
        |
        |
=========''', '''
    +---+
    |   |
    O   |
    /|\  |
    /    |
        |
=========''', '''
    +---+
    |   |
    O   |
    /|\  |
    / \  |
        |
=========''']
palabras = 'valoracion aprenderpython comida juego python web imposible variable curso volador cabeza reproductor mirada escritor billete lapicero celular valor revista gratuito disco voleibol anillo estrella'.split()

def buscarPalabraAleat(listaPalabras):
    
    palabraAleatoria = random.randint(0, len(listaPalabras) - 1)
    return listaPalabras[palabraAleatoria]

def displayBoard(AHORCADO, letraIncorrecta, letraCorrecta, palabraSecreta):
    print(AHORCADO[len(letraIncorrecta)])
    print ("")
    fin = " "
    print ('Letras incorrectas:', fin)
    for letra in letraIncorrecta:
        print (letra, fin)
    print ("")
    espacio = '_' * len(palabraSecreta)
    for i in range(len(palabraSecreta)):
        if palabraSecreta[i] in letraCorrecta:
            espacio = espacio[:i] + palabraSecreta[i] + espacio[i+1:]
    for letra in espacio: 
        print (letra, fin)
    print ("")

def elijeLetra(algunaLetra):

    while True:
        print ('Adivina una letra:')
        letra = input()
        letra = letra.lower()
        if len(letra) != 1:
            print ('Introduce una sola letra.') 
        elif letra in algunaLetra:
            print ('Ya has elegido esa letra ¿Qué tal si pruebas con otra?')
        elif letra not in 'abcdefghijklmnopqrstuvwxyz':
            print ('Elije una letra.')
        else:
            return letra

def empezar():

    print ('Quieres jugar de nuevo? (Si o No)')
    return input().lower().startswith('s')

print ('A H O R C A D O')
letraIncorrecta = ""
letraCorrecta = ""
palabraSecreta = buscarPalabraAleat(palabras)
finJuego = False
while True:
    displayBoard(AHORCADO, letraIncorrecta, letraCorrecta, palabraSecreta)

    letra = elijeLetra(letraIncorrecta + letraCorrecta)
    if letra in palabraSecreta:
        letraCorrecta = letraCorrecta + letra
        
        letrasEncontradas = True
        for i in range(len(palabraSecreta)):
            if palabraSecreta[i] not in letraCorrecta:
                letrasEncontradas = False
                break
        if letrasEncontradas:
            print ('¡Muy bien! La palabra secreta es "' + palabraSecreta + '"! ¡Has ganado!')
            finJuego = True
    else:
        letraIncorrecta = letraIncorrecta + letra
    
        if len(letraIncorrecta) == len(AHORCADO) - 1:
            displayBoard(AHORCADO, letraIncorrecta, letraCorrecta, palabraSecreta)
            print ('¡Se ha quedado sin letras!\nDespues de ' + str(len(letraIncorrecta)) + ' letras erroneas y ' + str(len(letraCorrecta)) + ' letras correctas, la palabra era "' + palabraSecreta + '"')
            finJuego = True
    
    if finJuego:
        if empezar():
            letraIncorrecta = ""
            letraCorrecta = ""
            finJuego = False
            palabraSecreta = buscarPalabraAleat(palabras)
        else:
            break
# este ejercicio lo modifique de internet

#    Realice un algoritmo que permita realizar un triqui de 3*3
#  es necesarias todas las validaciones.
from collections import deque

turno = deque(["0", "X"])
tablero = [
	[" ", " ", " "],
	[" ", " ", " "],
	[" ", " ", " "],
]

def mostrar_tablero():
	print("")
	for fila in tablero:		
		print (fila)

def actualizar_tablero(posicion, jugador):
	tablero[posicion[0]][posicion[1]] = jugador

def rotar_turno():
	turno.rotate()
	return turno[0]

def procesar_posicion(posicion):
	fila, columna = posicion.split(",")
	return [int(fila)-1, int(columna)-1]

def posicion_correcta(posicion):
	if 0 <= posicion[0] <= 2 and 0 <= posicion[1] <= 2:
		if tablero[posicion[0]][posicion[1]] == " ":
			return True
	return False

def ha_ganado(j):
	#compara las filas del tablero
	if tablero[0] == [j,j,j] or tablero[1] == [j,j,j] or tablero[2] == [j,j,j]:
		return True
	#compara las columnas
	elif tablero[0][0] == j and tablero[1][0] == j and tablero[2][0] == j:
		return True
	elif tablero[0][1] == j and tablero[1][1] == j and tablero[2][1] == j:
		return True
	elif tablero[0][2] == j and tablero[1][2] == j and tablero[2][2] == j:
		return True
	#compara las diagonales
	elif tablero[0][0] == j and tablero[1][1] == j and tablero[2][2] == j:
		return True
	elif tablero[0][2] == j and tablero[1][1] == j and tablero[2][0] == j:
		return True
	return False
def juego():
	mostrar_tablero()
	jugador = rotar_turno()
	while True:
		posicion = input("Juega {}, elige una posicion (fila, columna) de 1 a 3. 'salir' para salir".format(jugador))
		if posicion == 'salir':
			print ("Adios!!!")
			break
		try:
			posicion_l = procesar_posicion (posicion)			
		except:
			print ("Error, posicion {} no es válida. ".format(posicion))
			continue
		if posicion_correcta(posicion_l):
			actualizar_tablero(posicion_l, jugador)
			mostrar_tablero()
			if ha_ganado(jugador):
				print ("Jugador de {} ha ganado!!!".format(jugador))
				break
			jugador = rotar_turno()
		else:
			print ("Posicion {} no válida".format(posicion))
	
juego()
# tabla de multiplicación y que se pueda llenar sola de la tabla del 1 al 14
for i in range(1, 15):
    for j in range(1, 11):
        print(f'{i} x {j} = {i * j}')
# Realice un algoritmo que permita obtener el valor de cada uno de los vehículos 
# teniendo la siguiente tabla de información.
# vehiculos=[renault=0,chevrolet=0,mazda=0,audi=0,flat=0,toyota=0]
# precio=[MazdaPrecio=70000000,RenultPrecio=56000000,ChevroletPrecio=64000000,
# AudiPrecio=170000000,FlatPrecio=79000000,ToyotaPrecio=80000000]
# descuento[MazdaDes=0.10,RenultDes=0.20,ChevroletDes=0.11,AudiDes=0.10,FlatDes=0.7,ToyotaDes=0.12]
# Mazda=0
# Renult=0
# Chevrolet=0
# Audi=0
# Flat=0
# Toyota=0

MazdaPrecio=70000000
RenultPrecio=56000000
ChevroletPrecio=64000000
AudiPrecio=170000000
FlatPrecio=79000000
ToyotaPrecio=80000000


MazdaDes=0.10
RenultDes=0.20
ChevroletDes=0.11
AudiDes=0.10
FlatDes=0.7
ToyotaDes=0.12

Vehiculo = input("Ingrese el vehiculo que desea comprar: ")

if(Vehiculo=="Mazda" or "mazda"):
        print("Valor a pagar: ", MazdaPrecio
    - MazdaDes
)
elif(Vehiculo=="Renult" or "renult"):
        print("Valor a pagar: ", RenultPrecio
    - RenultDes
)
elif(Vehiculo=="Chevrolet" or "chevrolet"):
        print("Valor a pagar: ", ChevroletPrecio
    - ChevroletDes
)
elif(Vehiculo=="Audi" or "audi"):
        print("Valor a pagar: ", AudiPrecio
    - AudiDes
)
elif(Vehiculo=="Flat" or "flat"):
        print("Valor a pagar: ", FlatPrecio
    - FlatDes
)
elif(Vehiculo=="Toyota" or "toyota"):
        print("Valor a pagar: ", ToyotaPrecio
    - ToyotaDes
)
else:
    print("Por favor ingresa un valor valido")
    # lo intente hacer con una lista pero no supe

#     Se tiene una matriz con un tamaño para 100 registro de correos que le llega a un usuario 
# donde se almacena un código consecutivo, la fuente (correo del remitente), el asunto 
# y la descripción del correo y la fecha

correos=[]
for i in range(100):
    datos=(input("Ingrese asunto, descripción del correo y la fecha: "))
    correos.append(datos)


print(correos)
correos.reverse()
print(correos)

# https://www.youtube.com/watch?v=w0LqU99RRy8&t=281s