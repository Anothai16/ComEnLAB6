import RPi.GPIO as GPIO
import time
import drivers
from time import sleep
from array import array

name = list(['LAB 7',' LAB 7',\
'  LAB 7','   LAB 7',\
'    LAB 7','     LAB 7',\
'      LAB 7','       LAB 7','        LAB 7','         LAB 7','          LAB 7','           LAB 7'])

SW1  = 27  
SW2  = 17

GPIO.setmode(GPIO.BCM)
GPIO.setup(SW1, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(SW2, GPIO.IN, pull_up_down=GPIO.PUD_UP)

GPIO.add_event_detect(SW1, GPIO.FALLING)
GPIO.add_event_detect(SW2, GPIO.FALLING)
display = drivers.Lcd()
display.lcd_clear()
lcdnext = 0
try:
 while True:
   if GPIO.event_detected(SW1):
            display.lcd_clear()
            if lcdnext<11:
                lcdnext +=1
            display.lcd_display_string(name[lcdnext], 1)
            
   elif GPIO.event_detected(SW2):
            display.lcd_clear()
            if lcdnext>0:
                lcdnext -=1
            display.lcd_display_string(name[lcdnext], 1)
            

except KeyboardInterrupt:

   display.lcd_clear()
   print("\nBye...")
