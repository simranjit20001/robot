#En primer lugar se importan las llamadas a los archivos de algoritmo, asi como las librerias necesarias
from aloritmoaestrella import main as ast
import serial, time
import numpy as np
arduino = serial.Serial("COM5", 115200)
time.sleep(2)


#Se definen las variables a usar
   
maze =     [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]


i = 0
while True:
    if i == 0:
        x = int(input("Introduzca la coordenada x del inicio "))
        y = int(input("Introduzca la coordenada y del inicio "))
        x1 = int(input("Introduzca la coordenada x1 del destino "))
        y1 = int(input("Introduzca la coordenada y1 del destino "))
        start = (x, y)
        end = (x1, y1)
        print(ast(maze, start, end))
        i = 1
    info = arduino.readline()
    info_lista = info.decode()
    cadena=info_lista.split(',')
    distancia = float(cadena[1])
    angulo = float(cadena[0])*np.pi/180
    if distancia < 20 and distancia > 2:
        print("Estamos detectando obstaculos  ", distancia)
        x3 = int(abs(distancia * np.cos( angulo )))
        y3 = int(distancia * np.sin( angulo ))
        print(x3, y3)
        lista_borrable = []
        for i in maze[x3]:
            lista_borrable.append(i)
            print(lista_borrable)
        lista_borrable[y3] = 1
        print(lista_borrable)
        maze[x3] = lista_borrable
        print(maze)
    else:
        print(distancia)
mi_path = r"ruta mapeado"


for filan in 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15:
    for fila in maze[filan]:
        f = open(mi_path, 'a+')
        fila2 = str(fila)
        f.write(fila2)
        f.close()