import RPi.GPIO as GPIO2
import time

SW = 22
LEDr = 14
LEDg = 15
LEDb = 18
count = 0
s = 0
led_state = False


GPIO2.setmode(GPIO2.BCM)
GPIO2.setup(LEDr, GPIO2.OUT)
GPIO2.setup(LEDg, GPIO2.OUT)
GPIO2.setup(LEDb, GPIO2.OUT)
GPIO2.setup(SW, GPIO2.IN, pull_up_down=GPIO2.PUD_UP)

try:
    while True:
        if GPIO2.wait_for_edge(SW, GPIO2.FALLING):
            GPIO2.output(LEDr, False)
            GPIO2.output(LEDg, False)
            GPIO2.output(LEDb, False)
            s=s+1
            s=s%8
            count = count + 1
            GPIO2.output(LEDr, False)
            GPIO2.output(LEDg, False)
            GPIO2.output(LEDb, False)
            if(s==1):
                GPIO2.output(LEDr, False)
                GPIO2.output(LEDg, False)
                GPIO2.output(LEDb, True)
            if(s==2):
                GPIO2.output(LEDr, False)
                GPIO2.output(LEDg, True)
                GPIO2.output(LEDb, False)
            if(s==3):
                GPIO2.output(LEDr, False)
                GPIO2.output(LEDg, True)
                GPIO2.output(LEDb, True)
            if(s==4):
                GPIO2.output(LEDr, True)
                GPIO2.output(LEDg, False)
                GPIO2.output(LEDb, False)
            if(s==5):
                GPIO2.output(LEDr, True)
                GPIO2.output(LEDg, False)
                GPIO2.output(LEDb, True)
            if(s==6):
                GPIO2.output(LEDr, True)
                GPIO2.output(LEDg, True)
                GPIO2.output(LEDb, False)
            if(s==7):
                GPIO2.output(LEDr, True)
                GPIO2.output(LEDg, True)
                GPIO2.output(LEDb, True)
except KeyboardInterrupt:
    GPIO2.cleanup()
print("\nBye")
