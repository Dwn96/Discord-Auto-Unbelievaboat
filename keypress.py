import random
import time
import pynput
from pynput.keyboard import Key, Controller

i=0
while i < 10 :

    smallDelay=random.uniform(2,4)

    keyboard=Controller()
    keyboard.type('!work')  
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    time.sleep(smallDelay)

    keyboard=Controller()
    keyboard.type('!slut')  
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    time.sleep(smallDelay)


    keyboard=Controller()
    keyboard.type('!crime')  
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    time.sleep(smallDelay)


    keyboard=Controller()
    keyboard.type('!dep all')  
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    time.sleep(smallDelay)

   
    delay=random.uniform(720,900)
    time.sleep(delay) #set delay of 12-15 minutes to allow for cooldown ,the run again from start
    i+=1


