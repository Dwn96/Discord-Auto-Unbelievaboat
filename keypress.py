import random
import time
import pynput
from pynput.keyboard import Key, Controller

timeout=time.time() + 60*60*6 #loop for 6 hours

while True:

    if time.time() > timeout:
        break

    smallDelay=random.uniform(2,4) #2-4 sec delay between each command

    time.sleep(5) # 5 sec delay before start to allow you to select focus


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
    print('End of round')

   
    delay=random.uniform(720,900)
    time.sleep(delay) #set delay of 12-15 minutes to allow for cooldown ,the run again from start
    
 


