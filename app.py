print("Github indepentance version: AS-Iv1; https://github.com/BartenderWinery/PAC; Non-copyright/license")
import os, json, time, library as lib
from difflib import SequenceMatcher
from library import memory
path = os.path.dirname(os.path.abspath(__file__))
current_time = time.strftime("%H:%M:%S", time.localtime())
class command:
    def rcon(self,msg,cmd):
        pass
def rcon(self,msg):
    pass
def load(): #main loading function
    if(os.path.exists("library.json")&os.path.exists("memory.txt")):
        with open(path+"\library.json") as library:
            library = json.load(library)
        while path: #Listens for messsages in input & reloads input for repeated use
            def listen():
                message = input(">>:")
            listen()
    else:
        print(lib.check("library"))
        print(lib.check("memory"))
        print(lib.gen("librarys"))
        load()
if __name__ == "__main__":
    load()