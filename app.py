import pac, os, json, memory.library as lib
#Doesn't actually do anything of importance, simply a example how to use pac.py
path = os.path.dirname(os.path.abspath(__file__)); library = json.load(open(path+"\memory\library.json"))
print("Github indepentance version: AS-Iv1; https://github.com/BartenderWinery/PAC; Non-copyright/license")
def s():
    return input(">>: ")
class app:
    def load():
        while path:
            print(pac.process(s(),"responses",library,0.8)[0])
if __name__ == "__main__":
    if(os.path.exists(path+"\memory\library.json")):
        try:
            app.load()
        except KeyboardInterrupt:
            print(" Keyboard interruption")
            os.system("taskkill /f /im python.exe")
    else:
        print(lib.check(path))
        print(lib.gen(path))
        app.load()