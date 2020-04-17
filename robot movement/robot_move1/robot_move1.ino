const int inputPin1  = 10;    // Pin 15 of L293D IC
const int inputPin2  = 11;    // Pin 10 of L293D IC
//Motor B
const int inputPin3  = 5;   // Pin  7 of L293D IC
const int inputPin4  = 6;   // Pin  2 of L293D IC
int trigger_pin=13; //Sensor Trig pin connected to Arduino pin 13
int echo_pin=12; //Sensor Echo pin connected to Arduino pin 11
int distance;
int dtime;

void setup()
{
 pinMode(inputPin1, OUTPUT);
 pinMode(inputPin2, OUTPUT);
 pinMode(inputPin3, OUTPUT);
 pinMode(inputPin4, OUTPUT);
 Serial.begin(9600);
 pinMode(trigger_pin, OUTPUT);
 pinMode(echo_pin, INPUT);
 
}
void left()
{
 analogWrite(inputPin1, 220);
analogWrite(inputPin2, 120);

analogWrite(inputPin3, 220);
 analogWrite(inputPin4, 0);



}
void right()
{
analogWrite(inputPin1, 255);
 analogWrite(inputPin2, 0);

 analogWrite(inputPin3, 0);
 analogWrite(inputPin4, 255);

}
void forward()
{
 analogWrite(inputPin1, 255);
 analogWrite(inputPin2, 0);
 analogWrite(inputPin3, 255);
 analogWrite(inputPin4, 0);
}
void back()
{ analogWrite(inputPin1, 0);
 analogWrite(inputPin2, 255);
 analogWrite(inputPin3, 0);
 analogWrite(inputPin4, 255);

}
void astop()
{
analogWrite(inputPin1, 0);
 analogWrite(inputPin2, 0);
 analogWrite(inputPin3, 0);
 analogWrite(inputPin4, 0);
}

void udist()
{
  digitalWrite (trigger_pin, HIGH);
  delayMicroseconds (10);
  digitalWrite (trigger_pin, LOW);
  dtime = pulseIn (echo_pin, HIGH);
  distance=dtime*0.017;
  Serial.println(distance);
}
char t;
void loop()
{
  udist();
 if (Serial.available())
  { t = Serial.read();

 // 1- front,2-back,3-left,4-right
 switch ( t )
 {
   case '1': {

       forward();
       break;
     }
   case '2': {
       back();
       break;
     }
   case '4': {
       left();
       break;
     }
   case '3': 
       right();
       break;
       
   case '5': {
         astop();
       }
     }

 }}
