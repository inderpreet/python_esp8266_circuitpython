import machine
import time

led = machine.Pin(15, machine.Pin.OUT)

for i in range(10):
    led.on()
    time.sleep(0.1);
    led.off()
    time.sleep(0.1);


