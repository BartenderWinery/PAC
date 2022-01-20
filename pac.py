"""Python artificial Chatbot: String recognizing method.

Searches though a library of responses for a similar object to say back to the user. The bot can perform responses, commands, return dyanmic data, and remember information about you or other sources 

This emulates intelligence, I do not claim or try to generate a bunch of data and librarys that don't work as expected. It only searchs for similar objects within a json file with the goal of developer ease.

Version: AS-Iv1

Github: https://github.com/BartenderWinery/PAC"""
try:
    import os, time, difflib
    analog=[]
    try:
        def process(msg,passage,library,ratio):
            """Processes a message to find the most similar message above a 0.8 ratio using difflib.

            The following is in order of the arguments for the process function;
            1: The message to process, currently. We only support a string.
            2: The passage context of the library; for example: "responses"
            3: The library to use; you need to load the library before loading it into the process function.

            Example:

                library=json.load(open("D:\\Develop\\PYTHON\\PAC\\memory\\library.json"))
                msg=input(">>: ")

                if msg:
                    print(pac.process(msg,"responses",library,0.8)+", "+pac.book(-1).ratio())  

                ==---------------------==    

                Input: hey
                Output: hello!, 1.0"""
            try:
                def loop(rcon,passes):
                    """Loop: Description not yet writen"""
                    if rcon>passes:
                        passes=rcon
                        return True
                    else:
                        return False
            except:
                print("PAC ERR-001; Loop failed.")
            try:
                def recon(rcon):
                    """Type classifying: Description not yet writen"""
                    match rcon[1]:
                        case "txt":
                            return rcon 
                        case "cmd":
                            if rcon[2]:
                                os.system(rcon[2])
                        case "format":
                            match rcon[2]:
                                case "time":
                                    quary = time.strftime("%H:%M:%S", time.localtime())
                                case "last":
                                    quary=analog[-2]
                                case _:
                                    #task=loop(package[1],passes)
                                    #if task==True:
                                    #    quary=task
                                    pass
                        case "remember":
                            pass
                    return [str(rcon[0]).format(quary),rcon[1],rcon[2]]
            except:
                print("PAC ERR-002; Recon error.")
            passport=library[passage]; passes=ratio
            for responses in passport:
                try:
                    package=[passport.get(responses).split(";"),difflib.SequenceMatcher(None, msg, responses).ratio()]
                    task=loop(package[1],passes)
                    if task==True:
                        analog.append(package[0][0])
                        return recon(package[0])
                except:
                    print("PAC ERR-003; Response library error.")
            else:
                return ["...?","None"]
    except:
        print("PAC ERR; Interal code error.")
    def book(str):
        """Global lookup of all past responses and inputs
        
        Argument syntax: The string to lookup, search by name or by number.
        
        Examples:

            print(book(-1))
            Result: "?"

            ==---------------------==

            print(book("how are you"))
            Result: "I'm good"

            ==---------------------==

            print(book("I'm good"))
            Result: "how are you"
            """
        pass
except ImportError:
    print("PAC ERR; Essential modules missing.")
except SyntaxError:
    print("PAC ERR; Syntax error.")
except KeyboardInterrupt:
    print("PAC; Keyboard Interrupt.")