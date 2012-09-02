import pickle
import time

def get(name) :   
        file = open("obj/"+name+".pkl","rb")
        return pickle.load(file)

class Persistant(object) :
   
    def __init__(self,name) :
        self.name = name
        self.ts = time.time()

   
    def put(self) :
        file = open("obj/"+self.name+".pkl","wb")
        self.ts = time.time()
        pickle.dump(self,file)
        return self

