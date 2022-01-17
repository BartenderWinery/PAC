import os, json, time, memory.library as lib, difflib
path = os.path.dirname(os.path.abspath(__file__)); current_time = time.strftime("%H:%M:%S", time.localtime()); library = json.load(open(path+"\memory\library.json"))
class app:
    def preload():
        print("Github indepentance version: AS-Iv1; https://github.com/BartenderWinery/PAC; Non-copyright/license")
        modify.pre()
    def s():
        return input(">>: ")
    def load():
        modify.on()
        while path:
            modify.add()
            system.process(app.s(),"responses",None)
class system:
    def rcon(pack):
        match pack[1]:
            case "txt":
                if not pack[2]=="none":
                    print(pack[0])
                    trace = input(">>:")
                    if trace:
                        system.process(trace,"traces",pack[2])
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
    def process(msg,server,iso):
        if msg:
            modify.tone(msg)
            passed=[True,True]; overwrite=False
            try:
                con=0.8
                for responses in library["phrases"][server]:
                    try:
                        package=[library["phrases"][server].get(responses).split(";"),difflib.SequenceMatcher(None, msg, responses).ratio()]
                        if package[1]>con:
                            con=package[1]
                            system.rcon(package[0])
                            break
                    except:
                        print("ERR 003; Response library error.")
                else:
                    passed[0]=False
                for cmd in library["phrases"]["commands"]:
                    try:
                        package=[msg.split(";"),library["phrases"]["commands"].get(cmd).split(";")]
                        if package[0][0] == package[1][0]:
                            match package[0][0]:
                                case "run":
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
                                case "mods":
                                    print(json.dumps(mods, indent=3))
                                case "exit":
                                    os.system("taskkill /f /im python.exe")
                            if package[1][1]=="none":
                                overwrite=True
                    except:
                        print("ERR 004; CMD library error.")
                else:
                    passed[1]=False
                if passed==[False,False]:
                    match server:
                        case "responses":
                            if len(msg)>1 and overwrite==False:
                                print("...?")
                        case "traces":
                            system.process(None,"responses","none")
            except:
                print("ERR 002; Internal code error.")
class modify:
    try:
        global mods
        mods=json.load(open(path+"\mods\sys.json"))
        def pre():
            for pre in mods["preload"]:
                os.system("py "+path+"\mods\\"+pre)
        def on():
            for load in mods["onload"]:
                os.system("py "+path+"\mods\\"+load)
        def add():
            for addon in mods["addons"]:
                os.system("py "+path+"\mods\\"+addon)
        def tone(msg):
            for tone in mods["tones"]:
                os.system("py "+path+"\mods\\"+tone)
    except:
        print("ERR 005; No mods found. If you have some installed, make sure you have sys.json in the mods folder.")
try:
    app.preload()
except:
    print("ERR 001; Preload failed.")
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