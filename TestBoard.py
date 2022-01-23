from machine import Pin
import time
LED = machine.Pin(16,machine.Pin.OUT)
LEDA = machine.Pin(15,machine.Pin.OUT)
LEDB = machine.Pin(25,machine.Pin.OUT)
while True:
    LED.value(1)
    time.sleep(0.5)
    LED.value(0)
    time.sleep(0.5)
    LEDB.value(1)
    time.sleep(0.5)
    LEDB.value(0)
    time.sleep(0.5)
    LEDA.value(1)
    time.sleep(0.5)
    LEDA.value(0)
    time.sleep(0.5)
