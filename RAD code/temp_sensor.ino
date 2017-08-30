int tempPin = 1;        //the analog pin the TMP36's Vout (sense) pin is connected to
                       
int tempReading;        // the analog reading from the sensor
 
void setup(void) {
  
  Serial.begin(9600);   
 
  
  analogReference(EXTERNAL);
}
 
 
void loop(void) {
 
  tempReading = analogRead(tempPin);  
 
  Serial.print("Temp reading = ");
  Serial.print(tempReading);     
 
  // converting that reading to voltage, which is based off the reference voltage
  float voltage = tempReading * analogReference; //analogReference_voltage
  voltage /= 1024.0; 
 
  //print out the voltage
  Serial.print(" - ");
  Serial.print(voltage); Serial.println(" volts");
 
  //print out the temperature
  float temperatureC = (voltage - 0.5) * 100 ;  
                                              
  Serial.print(temperatureC); Serial.println(" degrees C");
 
  //conversion to Fahrenheight
  float temperatureF = (temperatureC * 9.0 / 5.0) + 32.0;
  Serial.print(temperatureF); Serial.println(" degrees F");
 
  delay(1000);
}
