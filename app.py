print("Github indepentance version: Development; https://github.com/BartenderWinery/PAC; Non-copyright/license")
print("This bot is still in its early stages! Please don't use any symbols or complex quuestions yet!")
import os, json, time
from time import sleep
from difflib import SequenceMatcher
path = os.path.dirname(os.path.abspath(__file__))
current_time = time.strftime("%H:%M:%S", time.localtime())
processing = False
def check(os,msg): #Checks if json files exists
    match os:
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
            print(check("library","Creating library at: "+path))
            print(check("tone","Creating tone librarys at: "+path))
            with open(os.path.join(path, "library.json"), 'w') as fp:
                pass
            with open(os.path.join(path, "tone.json"), 'w') as fp:
                pass
            sleep(0.5)
            if(os.path.exists("library.json")):
                return "Basic library successfully created."
            if(os.path.exists("tone.json")):
                return "Tone librarys successfully created."
def load(): #main loading function
    if(os.path.exists("library.json")&os.path.exists("tone.json")):
        with open(path+"\library.json") as library:
            library = json.load(library)
        while not processing: #Listens for messsages in input & reloads input for repeated use
            def listen():
                def rcon(responses): #Check for commands
                    if ':' in library.get(responses):
                        match library.get(responses):
                            case "I can respond to the following messages:":
                                print(library)
                            case "It is currently:":
                                print(str(current_time))
                            case "Clearing the screen:":
                                os.system("call cls")
                message = input(">>:")
                if(message):
                    new=0.8
                    for responses in library: #Runs though list for matchs
                        Sim=SequenceMatcher(None, message, responses).ratio()
                        if Sim > new:
                            new=Sim
                            print(library.get(responses))
                            rcon(responses)
            listen()
    else:
        print(check("library","No library found; generating basic library..."))
        print(check("tone","No tone librarys found; generating tone librarys..."))
        print(gen("librarys"))
        sleep(1)
        load()
if __name__ == "__main__":
    load()