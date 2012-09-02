#!/usr/bin/env python3
import time
import speak

from persistant import *
from switch import *

Switch("clock").put()

while True :
   sw = get("clock")
   if sw.on :
      hours = int(time.strftime('%I'))
      minutes = int(time.strftime('%M'))
      time_message = \
          str(int(hours)) + " oh clock " if minutes == 0 else \
          "a quarter past " + str(int(hours)) if minutes == 15 else \
          "half past " + str(int(hours)) if minutes == 30 else \
          str(minutes) + "minutes past " + str(int(hours)) if minutes < 30 else \
          "a quarter to " +str (int(hours) + 1) if minutes == 45 else \
          str(60 - minutes) + "minutes to " + str(int(hours) + 1) 

      message = "The Raspberry Pi time is " + time_message
      speak.say(message)
      
   time.sleep(60)

