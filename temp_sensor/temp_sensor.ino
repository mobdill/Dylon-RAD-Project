int tempPin = 1;       
                       
int tempReading;        
 
void setup(void) {
  
  Serial.begin(9600);   
 
  
  analogReference(EXTERNAL);
}
 
 
void loop(void) {
 
  tempReading = analogRead(tempPin);  
 
  Serial.print("Temp reading = ");
  Serial.print(tempReading);     
 
  float voltage = tempReading * analogReference; 
  voltage /= 1024.0; 
 
  Serial.print(" - ");
  Serial.print(voltage); Serial.println(" volts");
 
  float temperatureC = (voltage - 0.5) * 100 ;  
                                              
  Serial.print(temperatureC); Serial.println(" degrees C");
 
  float temperatureF = (temperatureC * 9.0 / 5.0) + 32.0;
  Serial.print(temperatureF); Serial.println(" degrees F");
 
  delay(1000);
}
