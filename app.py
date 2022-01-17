import os, json, time, memory.library as lib, difflib
path = os.path.dirname(os.path.abspath(__file__)); current_time = time.strftime("%H:%M:%S", time.localtime()); library = json.load(open(path+"\memory\library.json")); mods=[]
def load():
    def rcon(pack):
        match pack[1]:
            case "txt":
                if not pack[2]=="none":
                    print(pack[0])
                    trace = input(">>:")
                    if trace:
                        listen(trace,"traces",pack[2])
                else:
                    print(pack[0]) #Trace isolation not yet supported
            case "cmd":
                match pack[2]: 
                    case "console":
                        print(pack[0])
                        os.system(pack[2])
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
            def listen(msg,server,iso):
                if not msg==None:
                    message=msg
                else:
                    message = input(">>:")
                if(message):
                    i=[True,True]
                    try:
                        con=0.8
                        for responses in library["phrases"][server]:
                            try:
                                package=[library["phrases"][server].get(responses).split(";"),difflib.SequenceMatcher(None, message, responses).ratio()]
                                if package[1] > con:
                                    con=package[1]
                                    rcon(package[0])
                                    break
                            except:
                                print("ERR; 002 - Please check if yfou added the correct arguments to ASI librarys.")
                        else:
                            i[0]=False
                        for cmd in library["phrases"]["commands"]:
                            try:
                                package=[message.split(";"),library["phrases"]["commands"].get(cmd).split(";")]
                                if package[0][0] == package[1][0]:
                                    match package[0][0]:
                                        case "run": #Remove ; feature and instead use all but first string word in future
                                            os.system(package[0][1])
                                            os.system("echo:")
                                            print(package[1][1])
                                            break
                                        case "cls":
                                            os.system("call cls")
                                            print(package[1][1])
                                            break
                                        case "console":
                                            print(package[1][1])
                                            os.system("start "+path+"\\console.bat")
                                            break
                                        case "reboot":
                                            os.system("py "+path+"\\app.py")
                                        case "exit":
                                            os.system("taskkill /f /im python.exe")
                            except:
                                print("ERR; 003 - CMD librarys error/Keyboard interruption.")
                        else:
                            i[1]=False
                        if i[0]==False and i[1]==False:
                            match server:
                                case "responses":
                                    print("...?")
                                case "traces":
                                    listen(None,"responses","none")
                    except:
                        print("Error; 001; Internal code error!")
                
            listen(None,"responses","none")
    else:
        print(lib.check("library"))
        print(lib.gen("librarys"))
        load()
if __name__ == "__main__":
    try:
        load()
    except KeyboardInterrupt:
        print(" Keyboard interruption")
        os.system("taskkill /f /im python.exe")