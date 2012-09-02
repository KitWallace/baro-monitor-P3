#!/usr/bin/python
from urllib import request
import time

class Weather :
    """ cut down version just for the barometer mock """
                                       
    def __init__(self,id,url) :
        self.url = url
        self.id = id 
        self.refresh()

    def refresh(self) :
            page = request.urlopen(self.url)
            report = page.read().decode('utf-8')         
            data = report.split(" ")
            self.baro = float(data[6])
            self.ts = time.time()
            self.updated = True
            print(self.baro,self.ts)
  
