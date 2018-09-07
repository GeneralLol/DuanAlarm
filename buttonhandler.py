'''
This module is used for handling the button. 
'''
import RPi.GPIO as GPIO
from   aiy.voicehat import *

class Button:
    status     = bool()         #status indicates whether it is supposed to be on or off. 
    LED_pin    = 25             #Pin for the LED in the button in the Google AIY kit. 
    button_pin = 23#The button is handled through the Google AIY lib because that one might actually work. 
    
    def __init__(self):
        self.status = True
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.LED_pin   , GPIO.OUT)
        self.status = get_button(self.button_pin)
    
    def read_button(self):
        self.status = GPIO.input(self.button_pin)
    
    #Turns on the button light as prompted
    def light(self, stat):
        if (stat):
            GPIO.output(self.LED_pin, 1)
        else:
            GPIO.output(self.LED_pin, 0)
    
    def cleanup(self):
        GPIO.cleanup()