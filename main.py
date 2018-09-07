from time import sleep
from aiy.voicehat import *

def main():
    button = get_button()
    led    = get_led()
    
    led.set_state(LED.ON)
    
    try:
        while True:
            pass
    except:
        
        print ("End of program!")
    
    
if (__name__ == '__main__'):
    main()