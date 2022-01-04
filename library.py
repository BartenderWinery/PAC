import os
path = os.path.dirname(os.path.abspath(__file__))
class memory:
    pass
def check(os): #Checks if json files exists
    match os:
        case "library":
            if not (os.path.exists("library.json")):
                return "Library.json not found; Generating library at: "+path
            else:
                return "Library.json found; passing"
        case "memory":
            if not (os.path.exists("memory.txt")):
                return "memory.txt not found; Generating memory librarys at: "+path
            else:
                return "memory.txt found; passing"
def gen(package): #Main checker
    match package:
        case "librarys":
            print(check("library","Creating library at: "+path))
            print(check("memory","Creating memory librarys at: "+path))
            os.system("echo > library.json")
            os.system("echo > memory.txt")
            if(os.path.exists("library.json")):
                return "Basic library successfully created."
            if(os.path.exists("memory.txt")):
                return "Memory librarys successfully created."

                #def rcon(responses): #Check for commands
                #if ':' in library.get(responses):
                #    match library.get(responses):
                #        case "I can respond to the following messages:":
                #            print(library)
                #        case "It is currently:":
                #            print(str(current_time))
                #        case "Clearing the screen:":
                #            os.system("call cls")

                #if(message):
                #    new=0.8
                #    for responses in library: #Runs though list for matchs
                #        Sim=SequenceMatcher(None, message, responses).ratio()
                #        if Sim > new:
                #            new=Sim
                #            print(library.get(responses))
                #            rcon(responses)