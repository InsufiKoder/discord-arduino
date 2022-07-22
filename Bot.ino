int blue = 13;
int red = 12;
int yellow = 11;
int val = 0;
void setup() {
  Serial.begin(9600);
  Serial.flush();
  pinMode(blue, OUTPUT);
  pinMode(red, OUTPUT);
  pinMode(yellow, OUTPUT);
  digitalWrite(blue, LOW);
  digitalWrite(red, LOW);
  digitalWrite(yellow, LOW);
 
}
void loop() {
  if (Serial.available() > 0){
    val = char(Serial.read())-'0';
    if(val == 1){
      digitalWrite(blue, HIGH);  
      }
    if(val == 0){
      digitalWrite(blue, LOW);
      }
    if(val == 2){
      digitalWrite(red, HIGH);
      }
    if(val == 3){
      digitalWrite(red, LOW);
      }
    if(val == 4){
      digitalWrite(yellow, HIGH);
      }
    if(val == 5){
      digitalWrite(yellow, LOW);
      }
  }
}