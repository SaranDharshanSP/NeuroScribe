#include <WiFi.h>
#include <WebServer.h>
#include "XT_DAC_Audio.h"
#include "hello_A.h"
#include "hello_B.h"

const char* ssid = "SHRA-YES";
const char* password = "pokemonxy";

WebServer server(80);

XT_Wav_Class SoundA(sampleA);
XT_Wav_Class SoundB(sampleB);
XT_DAC_Audio_Class DacAudio(25, 0);

volatile int alphabet = -1;

void setup() {
  Serial.begin(115200);
  WiFi.begin(ssid, password);

  while (WiFi.status() != WL_CONNECTED) {
    delay(1000);
    Serial.println("Connecting to WiFi...");
  }
  Serial.println("Connected to WiFi");
  Serial.println(WiFi.localIP());

  server.on("/send_message", handleSendMessage);
  server.begin();
}

void handleSendMessage() {
  if (server.method() == HTTP_GET) {
    String alphabet_no = server.arg("play");
    if (alphabet_no.length() > 0) {
      alphabet = alphabet_no.toInt();
      Serial.println(alphabet);
      server.send(200, "text/plain", "Alphabet received");
    } else {
      server.send(400, "text/plain", "No Alphabet provided");
    }
  } else {
    server.send(405, "text/plain", "Method Not Allowed");
  }
}

void loop() {
  server.handleClient();
  
  // Handle sound playback based on the current value of alphabet
  if (alphabet == 0 && !SoundA.Playing) {
    Serial.println("Playing SoundA");
    DacAudio.Play(&SoundA);
  } else if (alphabet == 1 && !SoundB.Playing) {
    Serial.println("Playing SoundB");
    DacAudio.Play(&SoundB);
  }

  // Continuously fill the buffer to keep playing the sound
  DacAudio.FillBuffer();
}
