import time
from machine import Pin





redLED = Pin('P9_0')                    # create pin object for pin P9_0. This is for the Red LED
redLED.init(Pin.OUT, Pin.PULL_DOWN)      # set pin as output and enable pull-down resistor.
redLED.low()                             # set value low.

yellowLED = Pin('P9_5')                    # create pin object for pin P9_5. This is for the yellow LED.
yellowLED.init(Pin.OUT, Pin.PULL_DOWN)      # set pin as output and enable pull-down resistor.
yellowLED.low()        

greenLED = Pin('P6_5')                    # create pin object for pin P6_5. This is for the green LED.
greenLED.init(Pin.OUT, Pin.PULL_DOWN)      # set pin as output and enable pull-down resistor.
greenLED.low()                             # set value low.
print("Start program")
while True: # repeat forever.
  
    redLED.low() # Turn off red for green light
    yellowLED.low()  # turn off yellow      
    greenLED.high() # turn on green
    print("Green Light!")
    time.sleep(5) # wait 5 seconds
  
    redLED.low() # turn off red light for yellow light
    yellowLED.high()   # turn yellow light on     
    greenLED.low() #turn green light off.
    print("Yellow Light")
    time.sleep(2) # wait 2 seconds

    redLED.high() # turn on Red light
    yellowLED.low()   # turn off yellow light     
    greenLED.low() # turn off green lignt
    print("Red Light")
    time.sleep(5) # wait 5 seconds
  
    
    
    
