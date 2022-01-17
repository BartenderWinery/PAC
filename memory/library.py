import os
def check(path): #Checks if json files exists
    if not os.path.exists("library.json"):
        return "Library.json not found; Generating library at: "+path
    else:
        return "Library.json found; passing"
def gen(path): #Main checker
    print(check("library","Creating library at: "+path))
    os.system("echo > library.json")
    if os.path.exists("library.json"):
        return "Basic library successfully created."