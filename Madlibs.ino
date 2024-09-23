int relayPin = 7;  // Pin where the relay is connected

void setup() {
  pinMode(relayPin, OUTPUT);  // Set relay pin as output
  digitalWrite(relayPin, LOW);  // Ensure relay is off at start
  Serial.begin(9600);  // Start serial communication at 9600 baud rate
}

void loop() {
  if (Serial.available() > 0) {
    char command = Serial.read();  // Read the command from Python
    if (command == '1') {
      // Trigger the relay for 5 seconds, then turn it off
      digitalWrite(relayPin, HIGH);  // Turn on relay
      delay(1000);  // Keep relay on for 1 seconds
      digitalWrite(relayPin, LOW);  // Turn off relay
    }
  }
}
