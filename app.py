import os, json, time, memory.library as lib, difflib
path = os.path.dirname(os.path.abspath(__file__)); current_time = time.strftime("%H:%M:%S", time.localtime()); library = json.load(open(path+"\memory\library.json")); mods=[]
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
                    i=[True,True]
                    try:
                        con=0.8
                        for responses in library["phrases"]["responses"]:
                            try:
                                package=[library["phrases"]["responses"].get(responses).split(";"),difflib.SequenceMatcher(None, message, responses).ratio()]
                                if package[1] > con:
                                    con=package[1]
                                    print(rcon(package[0]))
                                    break
                            except:
                                print("ERR; 002 - Please check if you added the correct arguments to ASI librarys.")
                        else:
                            i[0]=False
                        for cmd in library["phrases"]["commands"]:
                            try:
                                package=[message.split(";"),library["phrases"]["commands"].get(cmd).split(";")]
                                if package[0][0] == package[1][0]:
                                    match package[0][0]:
                                        case "run":
                                            os.system(package[0][1])
                                            print(package[1][1])
                                        case "cls":
                                            os.system("call cls")
                                            print(package[1][1])
                                        case "exit":
                                           os.system("call taskkill /f /pid "+str(os.getpid()))
                            except:
                                print("ERR; 003 - Please check if you added the correct arguments to CMD librarys.")
                        else:
                            i[1]=False
                        if not i[0] and i[1]:
                            print("...?")
                    except:
                        print("Error; 001; Internal code error!")
            listen()
    else:
        print(lib.check("library"))
        print(lib.gen("librarys"))
        load()
if __name__ == "__main__":
    load()