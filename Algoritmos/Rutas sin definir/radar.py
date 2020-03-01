# Grafica "en vivo" para actualizar datos
# recibidos por puerto serial
# Plantilla para proyecto, datos de prueba aleatorios
# http://blog.espol.edu.ec/edelros/category/arduino/radar-ultrasonido/
# Tarea: Actualizar los datos en la función una trama para ri,yi
#        Con los obtenidos desde el puerto Serial

import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
import random as rnd

# PARAMETROS DE LA GRAFICA
# angulo
avance = 20
angulo = avance
a = avance
b = 180-avance
# alcance del radar
alcance = 50

# Datos a graficar
xi = [avance]
yi = [0]

# GRAFICA figura
# tiempo entre tramas
retraso = 1000
figura = plt.figure()
grafica = figura.add_subplot(111, projection='polar')
grafica.set_xlim(0,np.pi)
grafica.set_ylim(0,alcance)
grafica.set_title('Radar de Ultradonido')

# Linea de barrido y ventana de datos a graficar
tamano = (180//avance)//2
# El gráfico usa radianes
ri = np.array(xi[-tamano:])/180*np.pi
di = yi[-tamano:]
barrido, = grafica.plot(ri, di, 'y')

# linea del pulso y puntoreferencia:
pulsox = [0,ri[-1]]
pulsoy = [0,di[-1]]
PulsoLinea, = grafica.plot(pulsox,pulsoy,'g')
PulsoPunto, = grafica.plot(ri[-1],yi[-1],'go')

# Nueva Trama
def unatrama(i, xi, yi,angulo,avance):

    # ---DATOS EJEMPLO|INICIO

    # Posición en ángulo
    if len(xi)>0:
        angulo = xi[-1]
    else:
        angulo = 0
    # Dirección de barrido
    direccion = 1
    if (len(xi)>=2):
        sentido = xi[-1]-xi[-2]
        direccion = np.sign(sentido)
        if angulo>=(180-avance) and sentido>0:
            direccion = -1
        if angulo<=avance and sentido<0:
            direccion = 1

    angulo = angulo + direccion*avance
   
    # alcance del radar
    alcance = 50
    # Recibe un dato nuevo| ejemplo usa aleatorio
    undato = int(rnd.random()*alcance)+1
    # ---DATOS EJEMPLO|INICIO

    # actualiza datos xi, yi
    xi.append(angulo) 
    yi.append(undato)# numero del dato ejemplo

    # ventana de datos a graficar
    tamano = (180//avance)//2

    # Linea de radar, el gráfico usa radianes
    ri = np.array(xi[-tamano:])/180*np.pi
    di = yi[-tamano:]
    barrido.set_xdata(ri)
    barrido.set_ydata(di)
    
    # Linea y punto del Pulso
    pulsox = [0,ri[-1]]
    pulsoy = [0,yi[-1]]
    
    PulsoLinea.set_xdata(pulsox)
    PulsoLinea.set_ydata(pulsoy)

    PulsoPunto.set_xdata(pulsox[1])
    PulsoPunto.set_ydata(pulsoy[1])  

    # Presenta valores últimos valores en pantalla
    print(xi[-1],yi[-1])

    # Si los datos son más de 1000
    # Elimina el más antiguo del historial
    if len(xi)>1000:
        xi.pop(0)
        yi.pop(0)
    
    return()

# Animación
ani = animation.FuncAnimation(figura,
                              unatrama,
                              fargs=(xi, yi,angulo,avance),
                              interval=retraso,
                              blit=True)

plt.show()