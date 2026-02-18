from machine import Pin
import time

stepmotor= [[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]]
IN1 = Pin(14, Pin.OUT)
IN2 = Pin(25, Pin.OUT)
IN3 = Pin(26, Pin.OUT)
IN4 = Pin(27, Pin.OUT)

my_t=0.005

for i in range (0,1000):

        
        for i in stepmotor:
            
            IN1.value(i[0])
            IN2.value(i[1])
            IN3.value(i[2])
            IN4.value(i[3])
                
            time.sleep_ms(5)
