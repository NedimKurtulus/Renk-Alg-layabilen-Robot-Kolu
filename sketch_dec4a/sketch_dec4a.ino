#include <Servo.h>

Servo s1;
Servo s2;
Servo s3;
Servo s4;

void setup() {
  Serial.begin(9600);

  s1.attach(1);   // 1. servo
  s2.attach(2);   // 2. servo
  s3.attach(4);   // 3. servo
  s4.attach(5);   // 4. servo

  // Hepsi nötr konumda başlasın
  s1.write(90);
  s2.write(90);
  s3.write(90);
  s4.write(90);
}

void loop() {
  if (Serial.available()) {
    char komut = Serial.read();

    if (komut == 'G') {      // YEŞİL ALGILANDI
      servoSirayla();        // 4 servo sırayla çalışır
    }

    if (komut == 'R') {      // KIRMIZI ALGILANDI
      servoDurdur();         // Hepsi durur → 90 derece
    }
  }
}

// ----- 4 SERVO SIRAYLA ÇALIŞAN FONKSİYON -----
void servoSirayla() {

  // 1. servo
  s1.write(0);
  delay(3000);
  s1.write(90);
  delay(3000);

  // 2. servo
  s2.write(180);
  delay(3000);
  s2.write(90);
  delay(3000);

  // 3. servo
  s3.write(45);
  delay(3000);
  s3.write(90);
  delay(3000);

  // 4. servo
  s4.write(150);
  delay(3000);
  s4.write(90);
  delay(3000);
}

// ----- Tüm Servoları DURDURAN FONKSİYON -----
void servoDurdur() {
  s1.write(90);
  s2.write(90);
  s3.write(90);
  s4.write(90);
}
