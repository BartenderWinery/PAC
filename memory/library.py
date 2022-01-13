import os, app
path = app.path
def check(os): #Checks if json files exists
    match os:
        case "library":
            if not os.path.exists("library.json"):
                return "Library.json not found; Generating library at: "+path
            else:
                return "Library.json found; passing"
def gen(package): #Main checker
    match package:
        case "librarys":
            print(check("library","Creating library at: "+path))
            os.system("echo > library.json")
            if os.path.exists("library.json"):
                return "Basic library successfully created."