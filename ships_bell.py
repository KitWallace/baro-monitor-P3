#!/usr/bin/env python3 
import time
import speak

from persistant import *
from switch import *

bell_sound = "/home/pi/projects/part3clone/barometer-monitor/shipbell.wav"
silence = "/home/pi/projects/part3clone/barometer-monitor/silent-burst.wav"
Switch("bells").put()

while True :
   if get("bells").on :
      hours = time.strftime('%I')
      minutes = time.strftime('%M')
      mhours = int(hours) if hours !=0 else 24
      mhours = mhours % 4 * 2 
      bells = mhours if int(minutes) == 0 else mhours + 1 if int(minutes) == 30 else None
      bells = 8 if bells == 0 else bells
      if bells is not None :
#           btext = ", ".join (["Bong Bong" + speak.ssml_break(500) for i in range(bells // 2) ])
#           btext = btext + " Bong " if bells % 2 == 1  else btext
#           speak.say(speak.escape_XML(btext))
            for pair in range(bells // 2) :
               speak.play(bell_sound)
               speak.play(bell_sound)
               speak.play(silence)
            if bells % 2 == 1 :
               speak.play(bell_sound)

   time.sleep(60)

