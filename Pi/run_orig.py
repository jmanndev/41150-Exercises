"""
This program will let you test your ESC and brushless motor.
Make sure your battery is not connected if you are going
to calibrate it at first.
Since you are testing your motor, I hope you don't have your propeller
attached to it otherwise you are in trouble my friend...?
This program is made by AGT @instructable.com.
DO NOT REPUBLISH THIS PROGRAM...
actually the program itself is harmful
pssst Its not, its safe.
"""

import os#importing os library so as to communicate with the system
import time #importing time library to make Rpi wait because its too impatient
os.system ("sudo pigpiod") #Launching GPIO library
time.sleep(1) # As i said it is too impatient and so if this delay is removed you will get an error
import pigpio #importing GPIO library

ESC=17  #Connect the ESC in this GPIO pin
ESC2=18  #Connect the ESC in this GPIO pin

pi = pigpio.pi();
pi.set_servo_pulsewidth(ESC, 0)
pi.set_servo_pulsewidth(ESC2, 0)

max_throttle = 2000 #change this if your ESC's max value is different or leave it be
idle_throttle = 1500
min_throttle = 1000  #change this if your ESC's min value is different or leave it b

print ("Example RUN")
print ("Switch OFF the ESC")

responce = raw_input("press Enter to continue")
print ("generating IDLE signal, 1500")
pi.set_servo_pulsewidth(ESC, idle_throttle)
pi.set_servo_pulsewidth(ESC2, idle_throttle)

print ("Switch ON the ESC")
responce = raw_input("press Enter to continue")

print ("System detects the neutral throttle signal, makes a long beep sound")
print ("System detects battery voltage and makes several short beeps")
print ("which denotes the number of battery cells")
print ("when self test is finished 123 tone should be emitted")
print ("ready for start")
#responce = raw_input("press Enter to continue")

print ("running for 5s on 1250")
pi.set_servo_pulsewidth(ESC, 1250)
pi.set_servo_pulsewidth(ESC2, 1250)
time.sleep(5)
#pi.set_servo_pulsewidth(ESC, 1500)
#time.sleep(5)

print ("running for 5s on 1750")
pi.set_servo_pulsewidth(ESC, 1750)
pi.set_servo_pulsewidth(ESC2, 1750)
time.sleep(5)
#pi.set_servo_pulsewidth(ESC, 1500)
#time.sleep(5)

print ("running for 5s on 2000")
pi.set_servo_pulsewidth(ESC, 2000)
pi.set_servo_pulsewidth(ESC2, 2000)
time.sleep(5)
#pi.set_servo_pulsewidth(ESC, 1500)
#time.sleep(5)

print ("stopping")
pi.set_servo_pulsewidth(ESC, 0)
pi.set_servo_pulsewidth(ESC2, 0)
pi.stop()

print ("FINISH")



