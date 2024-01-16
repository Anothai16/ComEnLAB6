import RPi.GPIO as GPIO2
import time

SW = 22
LED = 18
led_state = False


GPIO2.setmode(GPIO2.BCM)
GPIO2.setup(LED, GPIO2.OUT)
GPIO2.setup(SW, GPIO2.IN, pull_up_down=GPIO2.PUD_DOWN)
switch_state = GPIO2.input(LED)

try:
    while True:
        new_switch_state = GPIO2.input(SW)
        if new_switch_state != switch_state:
            switch_state = new_switch_state
            if switch_state == GPIO2.LOW:
                led_state = not led_state
                if led_state:
                    GPIO2.output(LED, True)
                    print ("LED ON")
                else:
                    GPIO2.output(LED, False)
                    print ("LED OFF")
except KeyboardInterrupt:
    GPIO2.cleanup()
print("\nBye")
