int counter = 0;
int hola = 5;
void setup() {
  Serial.begin(9600);
}
void loop() {
  hola = Serial.read();
  Serial.println("hola");
  Serial.println(hola);

  
 
  }
