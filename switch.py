from machine import Pin
import time
led = Pin(16,Pin.OUT)
sw = Pin(15,Pin.IN)
while True:
    status = sw.value()
    if status == 0:
        led.value(1)
        time.sleep(0.5)
        led.value(0)
        time.sleep(0.5)
        