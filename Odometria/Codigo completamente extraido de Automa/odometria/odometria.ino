#include <SoftwareSerial.h>
#include <Servo.h>
int LeftSensor;
int RightSensor;
int cont_izq;
int cont_der; //contador de pulsos
int estado_der; //estado 0 es negro 1 es blanco
int estado_izq;
Servo servo_6; //motor rueda izquierda
Servo servo_9;//motor rueda derecha
void setup(){
Serial.begin(19200);
delay(1000);
pinMode(2, INPUT); //sensor rueada izquierda
pinMode(3, INPUT);//sensor rueda derecha
cont_der = 0; //contador de pulsos
cont_izq = 0;
estado_der = 0; //estado 0 es negro 1 es blanco
estado_izq = 0;
servo_6.attach(6);
servo_9.attach(9);
}
void Forward(){
servo_6.write(0);
servo_9.write(180);
}
void Motor_Stop(){
servo_6.write(90);
servo_9.write(90);
}
void odometria(){
//CALCULO LA POSICION X,Y y ORIENTACION THETA
float pi= 3.1416;
float diametro=5.70; //cm
float resolucion= 20; //ticks por vuelta del encoder
float dist_entre_ruedas=8.5;//cm
float f= pi*diametro/resolucion; //FACTOR DE CONVERSION
float dist_rueda_izq=f*cont_izq;
float dist_rueda_der=f*cont_der;
float dist_centro_robot=(dist_rueda_izq + dist_rueda_der)/2;
float theta= (dist_rueda_izq - dist_rueda_der)/dist_entre_ruedas;
float x=dist_centro_robot*cos(theta);
float y=dist_centro_robot*sin(theta);
//MUESTRO POR EL SERIE LA POSICION X Y
Serial.print("x = ");
Serial.println(x);
Serial.print("y = ");
Serial.println(y);
Serial.print("cont_izq = ");
Serial.println(cont_izq);
Serial.print("cont_der = ");
Serial.println(cont_der);
delay(1000);
}
void loop(){
if( millis() < 4000){ // la ejecucion de movimientos durara 4 segundos
if( millis() < 2000) Forward(); //tiempo en el que se mueven los motores
if( millis() > 2000) Motor_Stop(); //tiempo en el que espero que termine de moverse el robot
LeftSensor = digitalRead(2); // Read value from left sensor
RightSensor = digitalRead(3); // Read value from right sensor
if((LeftSensor==1) & (estado_izq==0)){ //cambio de estado a 0
cont_izq=cont_izq+1;
estado_izq=1;
}
if((LeftSensor==0) & (estado_izq==1)){ //cambio de estado a 1
cont_izq=cont_izq+1;
estado_izq=0;
}
if((RightSensor==1) & (estado_der==0)){ //cambio de estado a 0
cont_der=cont_der+1;
estado_der=1;
}
if((RightSensor==0) & (estado_der==1)){ //cambio de estado a 1
cont_der=cont_der+1;
estado_der=0;
}
}
else{ //una vez que han pasado 4 segundos muestro el resultado
Motor_Stop();
odometria();
}
}
