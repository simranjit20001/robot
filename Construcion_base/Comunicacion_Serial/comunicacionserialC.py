
import serial, time

#Envio de datos a Arduino
ser = serial.Serial('/dev/ttyUSB1', 115200) #En windows usar puerto COM (Ver el siguiente ejemplo)
ser.write(bytes(b'w'))

#Recepcion de datos a Arduino
import serial
arduino = serial.Serial('COM4', 9600) #En linux sustituir por puerto ttyUSBX (Ver el ejemolo anterior)
time.sleep(2)
rawString = arduino.readline()
print(rawString)
arduino.close()

