#include <HTTPClient.h>
#include <MHZ19_uart.h>
#include <WiFi.h>
#include "DHT.h"
#define DHTPIN 2
#define DHTTYPE DHT22
DHT dht(DHTPIN, DHTTYPE);
unsigned long interval = 50; // unit:sec
const int rx_pin = 4;
const int tx_pin = 5;
const char* ssid = "SGP200W-10A8-bg";
const char* password = "W33JEsrN";
String server = "http://192.168.1.254:8000/";
struct tm timeInfo;


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
  dht.begin();
  // ディープスリープ時間の設定
  esp_sleep_enable_timer_wakeup(interval*1000000);
  WiFi.begin(ssid, password); //2.4GHz帯のSSIDとパスワードを入力
  delay(9500);
  //Serial.print("IP address: ");
  //Serial.println(WiFi.localIP());
  configTime(9 * 3600, 0, "ntp.nict.jp", "time.google.com", "ntp.jst.mfeed.ad.jp");
  int co2 = mhz19.getCO2PPM();
  float h = dht.readHumidity();
  float t = dht.readTemperature();


  getLocalTime(&timeInfo);
  Serial.print(timeInfo.tm_year + 1900);
  Serial.print("-");
  Serial.print(timeInfo.tm_mon + 1);
  Serial.print("-");
  Serial.print(timeInfo.tm_mday);
  Serial.print(" ");
  Serial.print(timeInfo.tm_hour);
  Serial.print(":");
  Serial.print(timeInfo.tm_min);
  Serial.print(":");
  Serial.println(timeInfo.tm_sec);

  Serial.print("CO2 : ");
  Serial.println(co2);
  Serial.print("Temp : ");
  Serial.println(t);
  Serial.print("Humi : ");
  Serial.println(h);

  //if (timeInfo.tm_min==0){
    //if (timeInfo.tm_hour==1){
      //connect(server+"/new");
    //}else{
      //connect(server+"/update");
    //}
  //}
  connect(server+"/update_1min?temperature="+t+"&humidity="+h+"&co="+co2);
  

  esp_deep_sleep_start();

}

void loop()
{


}