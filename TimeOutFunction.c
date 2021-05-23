typedef struct{
  uint8_t Flag : 1;
  uint8_t overFlow : 1;
  uint16_t compareTimeValue;
}TimeOut;
uint16_t timer1msCounter = 0;
void initTimeOut(TimeOut* ts,uint16_t var){
  ts->Flag = 1;
  ts->compareTimeValue = timer1msCounter +var;
  if(ts->compareTimeValue < timer1msCounter){
    ts->overFlow = 1;
  }
}
/*
         0     50     100
case 1      ts     c      ts > c  flag
case 2      c      ts      overflow = 1
case 2   ts c             ts > c flag
*/
uint8_t checkTimeout(TimeOut* ts){
  //time out check
  if(ts->Flag == 0){return 0xFF;}
  if(ts->overFlow != 0){
    if(ts->compareTimeValue > timer1msCounter){
      ts->overFlow = 0;
    }
  }else if(ts->compareTimeValue < timer1msCounter){
    return 0xFF;
  }
  return 0;
}