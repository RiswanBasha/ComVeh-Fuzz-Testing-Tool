variables 
{ 
message 0x140 msg_0x140= {DLC=8,DIR=Tx,byte(0) = 0x01,byte(1) = 0x02,byte(2) = 0x03,byte(3) = 0x04,byte(4) = 0x05,byte(5) = 0x06,byte(6) = 0x07,byte(7) = 0x08};
message 0x10 msg_0x10= {DLC=8,DIR=Tx,byte(0) = 0x01,byte(1) = 0x02,byte(2) = 0x03,byte(3) = 0x04,byte(4) = 0x05,byte(5) = 0x06,byte(6) = 0x07,byte(7) = 0x08};
int time = 10000; //ms time

float time_0x140 = 1000.000000;
float time_0x10 = 10.000000;

msTimer clk_mst_0x140;
msTimer clk_t_0x140;
msTimer clk_mst_0x10;
msTimer clk_t_0x10;

int check_0x140;
int count_0x140 = 1;
int check_0x10;
int count_0x10 = 1;

}

on timer clk_mst_0x140
{
output(msg_0x140);
cancelTimer(clk_mst_0x140);
setTimer(clk_mst_0x140,time_0x140);
count_0x140++;
}
on timer clk_mst_0x10
{
output(msg_0x10);
cancelTimer(clk_mst_0x10);
setTimer(clk_mst_0x10,time_0x10);
count_0x10++;
}


on timer clk_t_0x140
{
int i,c=1;
cancelTimer(clk_mst_0x140);
write("%d",check_0x140);
write("%d",count_0x140);
if(count_0x140>=check_0x140)
{
writeToLogEx("    \nTestcase_1--> Message ID = 0x%02x || DLC = %x || Timestamp = %f || DIR=Tx ",msg_0x140.id,msg_0x140.dlc,timeNowNS());
for(i=0;i<msg_0x140.dlc;i++)
{
writeToLogEx("          bytes(%d) = 0x%02x",i,msg_0x140.byte(i));
}
writeToLogEx("          The message ID 0x%0x is ""SUCCESS""",msg_0x140.id);
}
else
{
writeToLogEx("    \nTestcase_1--> Message ID = 0x%02x || DLC = %x || Timestamp = %f || DIR=Tx ",msg_0x140.id,msg_0x140.dlc,timeNowNS());
for(i=0;i<msg_0x140.dlc;i++)
{
writeToLogEx("          bytes(%d) = 0x%02x",i,msg_0x140.byte(i));
}
writeToLogEx("          The message ID 0x%0x is ""FAIL""",msg_0x140.id);
c++;
}
}

on timer clk_t_0x10
{
int i,c=1;
cancelTimer(clk_mst_0x10);
write("%d",check_0x10);
write("%d",count_0x10);
if(count_0x10>=check_0x10)
{
writeToLogEx("    \nTestcase_2--> Message ID = 0x%02x || DLC = %x || Timestamp = %f || DIR=Tx ",msg_0x10.id,msg_0x10.dlc,timeNowNS());
for(i=0;i<msg_0x10.dlc;i++)
{
writeToLogEx("          bytes(%d) = 0x%02x",i,msg_0x10.byte(i));
}
writeToLogEx("          The message ID 0x%0x is ""SUCCESS""",msg_0x10.id);
}
else
{
writeToLogEx("    \nTestcase_2--> Message ID = 0x%02x || DLC = %x || Timestamp = %f || DIR=Tx ",msg_0x10.id,msg_0x10.dlc,timeNowNS());
for(i=0;i<msg_0x10.dlc;i++)
{
writeToLogEx("          bytes(%d) = 0x%02x",i,msg_0x10.byte(i));
}
writeToLogEx("          The message ID 0x%0x is ""FAIL""",msg_0x10.id);
c++;
}
}

void msg_0x140()
{
check_0x140=time/time_0x140;
setTimer(clk_mst_0x140,time_0x140);
setTimer(clk_t_0x140,time);
}

void msg_0x10()
{
check_0x10=time/time_0x10;
setTimer(clk_mst_0x10,time_0x10);
setTimer(clk_t_0x10,time);
}

on start
{ 
msg_0x140();
msg_0x10();
}