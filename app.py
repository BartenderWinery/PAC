print("Github indepentance version: Development; https://github.com/BartenderWinery/PAC; Non-copyright/license")
print("This bot is still in its early stages! Please don't use any symbols or complex quuestions yet!")
import os, json
from time import sleep
from sklearn.metrics.pairwise import cosine_similarity
path = os.path.dirname(os.path.abspath(__file__))
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
        def rcon(massage,responses): #cosine_similarity process; future: loop though each word for similarity total score
            pass
        while not processing: #Listens for messsages in input & reloads input for repeated use
            def listen():
                message = input(">>:")
                if(message):
                    print(message.split(" "))
                    for responses in library:
                        #print(responses)
                        if message.lower() == responses:
                            print(library.get(responses))
            listen()
    else:
        print(check("library","No library found; generating basic library..."))
        print(check("tone","No tone librarys found; generating tone librarys..."))
        print(gen("librarys"))
        sleep(1)
        load()
if __name__ == "__main__":
    load()