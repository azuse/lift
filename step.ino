int pin_1 = 4;
int pin_2 = 5;
int pin_3 = 6;//stop
int pin_4 = 7;
int pin_high1 = 8;
int pin_high2 = 9;
int pin_high3 = 10;
int state = 0;
char text_receieved;


void setup() {
  // put your setup code here, to run once:
  pinMode(pin_1, OUTPUT); 
  pinMode(pin_2, OUTPUT); 
  pinMode(pin_3, OUTPUT); 
  pinMode(pin_4, OUTPUT); 
  pinMode(pin_high1, OUTPUT); 
  pinMode(pin_high2, OUTPUT); 
  pinMode(pin_high3, OUTPUT); 
  Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
  digitalWrite(pin_high1,HIGH);
  digitalWrite(pin_high2,HIGH);
  digitalWrite(pin_high3,HIGH);
  text_receieved = Serial.read();
  /*if (text_receieved == 'a') 
  {
    state = 1;
    digitalWrite(pin_3,LOW);
    delay(1000);*/
    if (text_receieved == 'w')
    {
      state = 1;
    digitalWrite(pin_3,HIGH);
      digitalWrite(pin_1,HIGH);
      //analogWrite(pin_2,100);
      Serial.println('w');
      Serial.println(state);
  delay(1000);
      
    }
    if (text_receieved == 's')
    {
      state = 1;
    digitalWrite(pin_3,HIGH);
      digitalWrite(pin_1,LOW);
      //analogWrite(pin_2,100); 
      Serial.println('s');
      Serial.println(state);
  delay(1000);
    }
 
  if(text_receieved == 'b')
  {
    state = 0;
    digitalWrite(pin_3,LOW);
    digitalWrite(pin_1,LOW);
    //digitalWrite(pin_2,LOW);
    Serial.println('b');
    Serial.println(state);
  delay(1000);
  } 
}

