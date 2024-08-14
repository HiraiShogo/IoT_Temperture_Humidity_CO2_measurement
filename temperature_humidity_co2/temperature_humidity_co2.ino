#include <HTTPClient.h>
#include <MHZ19_uart.h>
#include <WiFi.h>
#include <Wire.h>

#define SHT31_ADDR 0x45

unsigned long interval = 50; // unit:sec
const int rx_pin = 4;
const int tx_pin = 5;
const char* ssid = "SGP200W-10A8-bg";
const char* password = "W33JEsrN";
String server = "http://192.168.1.254:8000/";



MHZ19_uart mhz19;
HTTPClient http; 

void connect(String url){
  http.begin(url);
  int httpCode = http.GET();
  //if (httpCode > 0) {
    //String payload = http.getString();
    //Serial.println(payload);
  //}
}

void setup()
{
  Serial.begin(9600);
  mhz19.begin(rx_pin, tx_pin);
  Wire.begin(21,22);
  byte command[2] = { 0x24, 0x00 };
  byte data[7];

  Wire.beginTransmission(SHT31_ADDR);
  Wire.write(command, sizeof(command));
  Wire.endTransmission();

  int i = 0;
  Wire.requestFrom(SHT31_ADDR, 6);
  while (Wire.available() && i < 6) {
      data[i++] = Wire.read();
  }
  data[i] = 0;

  // ディープスリープ時間の設定
  esp_sleep_enable_timer_wakeup(interval*1000000);
  WiFi.begin(ssid, password); //2.4GHz帯のSSIDとパスワードを入力
  delay(9500);
  

  int co2 = mhz19.getCO2PPM();
  float t = -50.0 + (175.0 * (unsigned int)(data[0] * 256 + data[1]) / 65535.0);
  float h = (100.0 * (unsigned int)(data[3] * 256 + data[4])) / 65535.0;



  Serial.print("CO2 : ");
  Serial.println(co2);
  Serial.print("Temp : ");
  Serial.println(t);
  Serial.print("Humi : ");
  Serial.println(h);


  connect(server+"/update_1min?temperature="+t+"&humidity="+h+"&co="+co2);
  

  esp_deep_sleep_start();

}

void loop()
{


}