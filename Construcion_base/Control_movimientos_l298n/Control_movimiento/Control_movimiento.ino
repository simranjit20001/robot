// Configuramos los pines que vamos a usar
int motorDer1=2;//El pin 2 a In1 del L298N
int motorDer2=3;//El pin 3 a In2 del L298N
int motorIzq1=7;//El pin 7 a In3 del L298N
int motorIzq2=4;//El pin 4 a In4 del L298N
int derecho=5;  //El pin 5 a EnA del L298N
int izquierdo=6;//El pin 6 aEnB del L298N
#include <NewPing.h>
 
/*Aqui se configuran los pines donde debemos conectar el sensor*/
#define TRIGGER_PIN  12
#define ECHO_PIN     11
#define MAX_DISTANCE 200
 
/*Crear el objeto de la clase NewPing*/
NewPing sonar(TRIGGER_PIN, ECHO_PIN, MAX_DISTANCE);
char hola;

void setup() 
{ 
  Serial.begin(115200);
  //Configuramos los pines como salida
  pinMode(motorDer1, OUTPUT); 
  pinMode(motorDer2, OUTPUT);
  pinMode(motorIzq1, OUTPUT); 
  pinMode(motorIzq2, OUTPUT); 
  pinMode(derecho, OUTPUT);
  pinMode(izquierdo, OUTPUT);

} 
void izquierda(){ 
  digitalWrite(motorDer1,HIGH);
  digitalWrite(motorDer2,LOW);
  digitalWrite(motorIzq1,HIGH);
  digitalWrite(motorIzq2,LOW);
  analogWrite(derecho,200);//Velocidad motor
  analogWrite(izquierdo,200);
}
void derecha(){ 
  digitalWrite(motorDer1,LOW);
  digitalWrite(motorDer2,HIGH);
  digitalWrite(motorIzq1,LOW);
  digitalWrite(motorIzq2,HIGH);
  analogWrite(derecho,200);
  analogWrite(izquierdo,200);
  
}
void detras(){ 
  digitalWrite(motorDer1,HIGH);
  digitalWrite(motorDer2,LOW);
  digitalWrite(motorIzq1,LOW);
  digitalWrite(motorIzq2,HIGH);
  analogWrite(derecho,200);
  analogWrite(izquierdo,200);
}
void delante(){ 
  digitalWrite(motorDer1,LOW);
  digitalWrite(motorDer2,HIGH);
  digitalWrite(motorIzq1,HIGH);
  digitalWrite(motorIzq2,LOW);
  analogWrite(derecho,200);
  analogWrite(izquierdo,200);
}
void parar(){ 
  digitalWrite(motorDer1,LOW);
  digitalWrite(motorDer2,LOW);
  digitalWrite(motorIzq1,LOW);
  digitalWrite(motorIzq2,LOW);
  analogWrite(derecho,200);
  analogWrite(izquierdo,200);
}

void loop() {
if (Serial.available() >0){

 hola = Serial.read();
 if (hola == 'w') {
    Serial.println("Delante");  
    delante();
  }
 if (hola == 's') {
    Serial.println("Detras");  
    detras();
 } if (hola == 'd') {
    Serial.println("Derecha");  
    derecha();
  }
 if (hola == 'a') {
    Serial.println("Izquierda");  
    izquierda();
  }
 if (hola == 'p') { 
    Serial.println("Parar");
    parar();
 }
}
 }
