/* Radar Ultrasonido
 *  integrando: Servo - Barrido
 *  y Sensor Ultrasonido HC-SR04
 *  http://blog.espol.edu.ec/edelros/category/arduino/radar-ultrasonido/
 *  La lectura del ultrasonido se convierte en una función UnPulso()
 *  Los datos de las lecturas se envian por Serial
 *  Tarea: Desarrollar el procesamiento de los datos en Python
 */

#include <Servo.h> 

// Servo Pin y Objeto
int servoPin = 3; 
Servo Servo1; 

int avance = 20;
int angulo = avance;
int espera = 1000; //ms

int a = angulo;
int b = 180 - avance;

// Disparo del PULSO, Sensor del Retorno de pulso
int TriggerPin = 12;
int EchoPin = 11;

// tiempos: pulso, sin pulso, eco
int tpulsoON = 15;
int tpulsoOFF = 2000;
int dt_apaga = 10;
float dt_Echo;

void setup(){
    Serial.begin(9600);

    Servo1.attach(servoPin); 

    pinMode(TriggerPin, OUTPUT);
    pinMode(EchoPin, INPUT);
}
void loop(){
    Servo1.write(angulo);
    dt_Echo = UnPulso();
    
    delay(espera);
    angulo = angulo + avance;
    
    // Sentido de rotación
    if (angulo>=b or angulo<=a){
        avance = -avance;
    }
    
    // Salida a Serial
    Serial.print(angulo);
    Serial.print(",");
    Serial.println(dt_Echo);
}
 
float UnPulso(){
    // tiempo entre PULSOs: tpulsoOFF
    digitalWrite(TriggerPin, LOW);
    delayMicroseconds(tpulsoOFF);
    // Dispara PULSO de duración: tpulsoON  
    digitalWrite(TriggerPin, HIGH);
    delayMicroseconds(tpulsoON); 
    digitalWrite(TriggerPin, LOW); 
    delayMicroseconds(dt_apaga);  
    
    // Lectura sensor pulso: tiempo de echo 
    dt_Echo = pulseIn(EchoPin, HIGH);
    return dt_Echo;
}
