boolean hareketdurumu =0;
boolean sonhareketdurumu =0;

void setup() {
pinMode(7,INPUT);
Serial.begin(9600);
  
}

void loop() {
hareketdurumu = digitalRead(7);

if (hareketdurumu != sonhareketdurumu) {
if (hareketdurumu == HIGH) {
Serial.print(1);
delay(30000);
} 


}
sonhareketdurumu = hareketdurumu; 
}
