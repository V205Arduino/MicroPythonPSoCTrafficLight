import time
from machine import Pin

time.sleep(1)           # sleep for 1 second
time.sleep_ms(500)      # sleep for 500 milliseconds
time.sleep_us(10) 



redLED = Pin('P9_0')                    # create pin object for pin P9_0. This is for the Red LED
redLED.init(Pin.OUT, Pin.PULL_DOWN)      # set pin as output and enable pull-down resistor.
redLED.low()                             # set value low.

yellowLED = Pin('P9_5')                    # create pin object for pin P9_5. This is for the yellow LED.
yellowLED.init(Pin.OUT, Pin.PULL_DOWN)      # set pin as output and enable pull-down resistor.
yellowLED.low()        

greenLED = Pin('P6_5')                    # create pin object for pin P6_5. This is for the green LED.
greenLED.init(Pin.OUT, Pin.PULL_DOWN)      # set pin as output and enable pull-down resistor.
greenLED.low()                             # set value low.

