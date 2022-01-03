print("Github indepentance version: AS-Iv1; https://github.com/BartenderWinery/PAC; Non-copyright/license")
import os, json, time, library as lib
from difflib import SequenceMatcher
path = os.path.dirname(os.path.abspath(__file__))
current_time = time.strftime("%H:%M:%S", time.localtime())
processing = False
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
        print(lib.check("library"))
        print(lib.check("memory"))
        print(lib.gen("librarys"))
        load()
if __name__ == "__main__":
    load()