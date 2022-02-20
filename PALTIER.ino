unsigned long Time;

//connect LM35 tempature sensor into A0
void setup() {
  Serial.begin(9600);// Starting Serial communication
}
 
void loop() {
  Time = millis();

  int sensor0 = analogRead(A0); // Read the data from the sensor (range 0 to 1023).
  float tempature0 = (sensor0 * 0.48828125); // the T equation 500/1024
  Serial.print("tempature0 is: "); 
  Serial.println(tempature0); // print the number on the serial monitor
ז  
  int sensor1 = analogRead(A1); // Read the data from the sensor (range 0 to 1023).
  float tempature1 = (sensor1 * 0.48828125); // the T equation 500/1024
  Serial.print("tempature1 is: "); 
  Serial.println(tempature1); // print the number on the serial monitor
  delay(500);
}
