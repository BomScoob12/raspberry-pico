from machine import Pin, PWM
import time
from micropython import const

DO = const(523)
ME = const(659)

pwmPiezo = PWM(Pin(13))
pwmPiezo.duty_u16(32768)

pwmPiezo.freq(ME)
time.sleep(0.5)

pwmPiezo.freq(DO)
time.sleep(0.5)


pwmPiezo.duty_u16(0)