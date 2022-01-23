from machine import Pin,PWM
from utime import sleep
from micropython import const

a = Pin(18,Pin.OUT)
b = Pin(19,Pin.OUT)
c = Pin(13,Pin.OUT)
d = Pin(14,Pin.OUT)
e = Pin(15,Pin.OUT)
f = Pin(17,Pin.OUT)
g = Pin(16,Pin.OUT)
dp = Pin(12,Pin.OUT)
ME = const(659)

def one(count = 1):
    while(count > 0):
        b.on()
        c.on()
        sleep(0.8)
        b.value(0)
        c.value(0)
        count -= 1
        
        
def two(count = 1):
    while (count > 0):
        a.on()
        b.on()
        g.on()
        e.on()
        d.on()
        sleep(0.8)
        a.value(0)
        b.value(0)
        g.value(0)
        e.value(0)
        d.value(0)
        count -= 1

def thr(count = 1):
    while (count > 0):
        a.on()
        b.on()
        g.on()
        c.on()
        d.on()
        sleep(0.8)
        a.value(0)
        b.value(0)
        g.value(0)
        c.value(0)
        d.value(0)
        count -= 1

def fou(count = 1):
    while (count > 0):
        b.on()
        c.on()
        g.on()
        f.on()
        sleep(0.8)
        b.value(0)
        c.value(0)
        g.value(0)
        f.value(0)
        count -= 1
        
def fiv(count = 1):
    while (count > 0):
        a.on()
        c.on()
        d.on()
        f.on()
        g.on()
        sleep(0.8)
        a.value(0)
        c.value(0)
        d.value(0)
        f.value(0)
        g.value(0)
        count -= 1
        
def six(count = 1):
    while (count > 0):
        a.on()
        c.on()
        d.on()
        e.on()
        f.on()
        g.on()
        sleep(0.8)
        a.value(0)
        c.value(0)
        d.value(0)
        e.value(0)
        f.value(0)
        g.value(0)
        count -= 1

def sev(count = 1):
    while (count > 0):
        a.on()
        c.on()
        b.on()
        sleep(0.8)
        a.value(0)
        c.value(0)
        b.value(0)
        count -= 1
        
def egh(count = 1):
    while (count > 0):
        a.on()
        b.on()
        c.on()
        d.on()
        e.on()
        f.on()
        g.on()
        sleep(0.8)
        a.value(0)
        b.value(0)
        c.value(0)
        d.value(0)
        e.value(0)
        f.value(0)
        g.value(0)
        count -= 1

def nin(count = 1):
    while (count > 0):
        a.on()
        b.on()
        c.on()
        d.on()
        f.on()
        g.on()
        sleep(0.8)
        a.value(0)
        b.value(0)
        c.value(0)
        d.value(0)
        f.value(0)
        g.value(0)
        count -= 1
        
def zeo(count = 1):
    while (count > 0):
        a.on()
        b.on()
        c.on()
        d.on()
        e.on()
        f.on()
        sleep(0.8)
        a.value(0)
        b.value(0)
        c.value(0)
        d.value(0)
        e.value(0)
        f.value(0)
        count -= 1
        
def clear(count = 1):
    while (count > 0):
        a.value(0)
        b.value(0)
        c.value(0)
        d.value(0)
        e.value(0)
        f.value(0)
        g.value(0)
        sleep(1)
        count -= 1

def sound():       
    pwmPiezo = PWM(Pin(8))
    pwmPiezo.duty_u16(32768)
    pwmPiezo.freq(ME)
    sleep(0.2)
    pwmPiezo.duty_u16(0)
        
while True:
    clear()
    sound()
    one()
    sound()
    two()
    sound()
    thr()
    sound()
    fou()
    sound()
    fiv()
    sound()
    six()
    sound()
    sev()
    sound()
    nin()
    sound()
    zeo()
    sound()
    
    
