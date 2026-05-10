from machine import Pin
import time
p1 = Pin(15, Pin.OUT) 
p2 = Pin(14, Pin.OUT) 
p3 = Pin(13, Pin.OUT)  
ps = [p1,p2,p3]

while True:
    for p in ps:
        p.toggle()
    time.sleep(1)
    