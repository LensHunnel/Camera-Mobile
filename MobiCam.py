#!/usr/bin/python 
#+-+-+-+-+-+-+-+-+-+-+-+-+-+
#|N|e|c|r|o|m|a|n|c|i|e|n|-+
#+-+-+-+-+-+-+-+-+-+-+-+-+-+
## Control.py
# controls motor using a H-Bridge
#
# Author : Lens Hunnel
# Date   : 11/03/2014
# Import required Python libraries
import wiringpi2 as wiringpi  
from time import sleep  

wiringpi.wiringPiSetupGpio()    
wiringpi.pinMode(18,2)      # hardware pwm only works on GPIO port 18    
wiringpi.pwmWrite(18,0)     # duty cycle between 0 and 1024   
                            # 0 = off and 1024 = constantly on   
  
pause_time = 0.002          # you can change this to slow down/speed up  
  
try:  
    while True:  
        for i in range(0,1025):         # 1025 because it stops at 1024  
            wiringpi.pwmWrite(18,i)  
            sleep(pause_time)  
        for i in range(1024,-1,-1):     # from 1024 to zero in steps of -1  
            wiringpi.pwmWrite(18,i)  
            sleep(pause_time)  
  
finally:  
    wiringpi.pwmWrite(18,0)             # switch PWM output to 0  
    wiringpi.pinMode(18,0)              # GPIO18 to input