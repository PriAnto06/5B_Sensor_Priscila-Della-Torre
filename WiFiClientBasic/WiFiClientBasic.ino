/*
 *  This sketch sends a message to a TCP server
 *
 */

#include <WiFi.h>
#include <WiFiMulti.h>
#include <HTTPClient.h>
#include <format>

WiFiMulti WiFiMulti;

//const char *ssid = "Peine-3";
//const char *password = "etecPeine3";
//const char* serverName = "http://19.56.13.3:36000/api/sensor";
const char *ssid = "ETEC-UBA";
const char *password = "ETEC-alumnos@UBA";
const char* serverName = "http://10.9.120.87:7000/api/sensor";

void setup() {
  Serial.begin(115200);
  delay(10);

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
 String jsonStr = std::format("{\nombre\":\"luxometro\",\"valor\":"+ string(valor)+"}")
 //char *jsonStr = "{\"nombre\":\"luxometro\",\"valor\":145}";
 int httpResponseCode = http.POST(jsonStr);
 Serial.print("Respuesta: ");
 Serial.println(httpResponseCode);
 http.end();
 }
 else
 {
   Serial.println("Desconectado");
 }
}