import os
path = os.path.dirname(os.path.abspath(__file__))
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