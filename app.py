print("Github indepentance version: Development; https://github.com/BartenderWinery/PAC; Non-copyright/license")
import os, logic
from time import sleep
processing = False
def check(r,msg): #Checks if json files exists
    match r:
        case "library":
            if not (os.path.exists("library.json")):
                return msg
            else:
                return "Library.json found; passing"
        case "tone":
            if not (os.path.exists("tone.json")):
                return msg
            else:
                return "tone.json found; passing"
def gen(package): #Main checker
    match package:
        case "librarys":
            sleep(0.5)
            print(check("library","Creating library at: "+os.path.dirname(os.path.abspath(__file__))))
            print(check("tone","Creating tone librarys at: "+os.path.dirname(os.path.abspath(__file__))))
            with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "library.json"), 'w') as fp:
                pass
            with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "tone.json"), 'w') as fp:
                pass
            sleep(0.5)
            if(os.path.exists("library.json")):
                return "Basic library successfully created."
            if(os.path.exists("tone.json")):
                return "Tone librarys successfully created."
def load(): #main loading function
    if(os.path.exists("library.json")&os.path.exists("tone.json")):
        while not processing: #Listens for messsages in input & reloads input for repeated use
            def listen():
                message = input(">>:")
                if(message):
                    print(message.split(" "))
            listen()
    else:
        print(check("library","No library found; generating basic library..."))
        print(check("tone","No tone librarys found; generating tone librarys..."))
        print(gen("librarys"))
        sleep(1)
        load()
if __name__ == "__main__":
    load()