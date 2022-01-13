import os, json, time, memory.library as lib, difflib
path = os.path.dirname(os.path.abspath(__file__)); current_time = time.strftime("%H:%M:%S", time.localtime()); library = json.load(open(path+"\memory\library.json"))
def load():
    def rcon(pack):
        match pack[1]:
            case "txt":
                return pack[0]
            case "cmd":
                match pack[2]: 
                    case "test":
                        os.system("echo:")
                        os.system("echo Test passed!")
                    case _:
                        os.system(pack[2])
                return pack[0]
            case "format":
                match pack[2]:
                    case "time":
                        quary=current_time
                    case _:
                        con=0.8
                        for mem in library["memory"]:
                            package=[library["memory"].get(mem).split(";"),difflib.SequenceMatcher(None, pack[2], mem).ratio()]
                            if package[1] > con:
                                con=package[1]
                                quary=package[0]
                return str(pack[0]).format(quary)
    print("Github indepentance version: AS-Iv1; https://github.com/BartenderWinery/PAC; Non-copyright/license")
    if(os.path.exists(path+"\memory\library.json")):
        while path:
            def listen():
                message = input(">>:")
                if(message):
                    #try:
                        con=0.8
                        for responses in library["phrases"]["responses"]:
                            package=[library["phrases"]["responses"].get(responses).split(";"),difflib.SequenceMatcher(None, message, responses).ratio()]
                            if package[1] > con:
                                con=package[1]
                                print(rcon(package[0]))
                    #except:
                    #    print("Error; 001; Initial code error!")
            listen()
    else:
        print(lib.check("library"))
        print(lib.gen("librarys"))
        load()
if __name__ == "__main__":
    load()