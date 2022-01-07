import os, json, time, memory.library as lib
path = os.path.dirname(os.path.abspath(__file__)); current_time = time.strftime("%H:%M:%S", time.localtime()); library = json.load(open(path+"\memory\library.json"))
def load(): #main loading function
    print("Github indepentance version: AS-Iv1; https://github.com/BartenderWinery/PAC; Non-copyright/license")
    if(os.path.exists(path+"\memory\library.json")):
        while path:
            def listen():
                message = input(">>:")
            listen()
    else:
        print(lib.check("library"))
        print(lib.gen("librarys"))
        load()
if __name__ == "__main__":
    load()