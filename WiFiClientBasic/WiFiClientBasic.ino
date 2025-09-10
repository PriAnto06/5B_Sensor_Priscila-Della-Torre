/*
 *  This sketch sends a message to a TCP server
 *
 */

#include <WiFi.h>
#include <WiFiMulti.h>
#include <HTTPClient.h>
#include <string>
const  int pin = 35;
WiFiMulti WiFiMulti;

//const char *ssid = "Peine-3";
//const char *password = "etecPeine3";
//const char* serverName = "http://19.56.13.3:36000/api/sensor";
const char *ssid = "Peine-3";
const char *password = "etecPeine3";
const char* serverName = "http://10.9.120.87:5000/api/sensor";

void setup() {
  Serial.begin(115200);
  delay(10);
 pinMode(pin,INPUT);
  // We start by connecting to a WiFi network
  WiFiMulti.addAP(ssid, password);

  Serial.println();
  Serial.println();
  Serial.print("Waiting for WiFi... ");
  

  while (WiFiMulti.run() != WL_CONNECTED) {
    Serial.print(".");
    delay(500);
  }

  Serial.println("");
  Serial.println("WiFi connected");
  Serial.println("IP address: ");
  Serial.println(WiFi.localIP());

  delay(500);
}

void loop()
 {
 delay(1000);
 if(WiFi.status()== WL_CONNECTED)
 {
 HTTPClient http ;
 WiFiClient client;
 http.begin(client, serverName);
 http.addHeader("Content-Type", "application/json");
 Serial.println("Enviando dato");
 int valor =145;
std::string jsonStr = std::string("{\nombre\":\"termometro\",\"valor\":"+ std:: to_string(valor)+"}");
 //char *jsonStr = "{\"nombre\":\"luxometro\",\"valor\":145}";
 int httpResponseCode = http.POST(jsonStr.c_str());
 Serial.print("Respuesta: ");
 Serial.println(httpResponseCode);
 Serial.println(valor);
 http.end();
 }
 else
 {
   Serial.println("Desconectado");
 }
}

/*No se puede conectar, por que no hay internet*/
/*lo que hice fue conectar el sensor a la red pero no hay wifi*/
/*la direccion ip es de un servidor que se conecto el profe*/