def translate(data,librarys):
    with open(librarys[0]) as base:
        q={"aggression":0,"sadness":0,"fearful":0,"disgust":0,"enjoyment":0} #Create a baseline grandiant to mimic adaptive behavior
        #add profiling information to factor in grandiants towards a specific person, if fake, than only disgust can be majorly affected
        #all values within 10% are neutral
        #restrictions: enjoyment is incompatible with all other values; disgust can be related to sadness
        #if any value>10% than enjoyment cannot be above >10%
        match data[-1]:
            case ".":
                q["aggression"]+0.2
                q["enjoyment"]-0.1
                pass #Statement or command
            case "?":
                q["enjoyment"]-0.1
                pass #question
            case "!":
                pass #Statement or command
            case _:
                pass #Statement or command
        #TRANSLATES TEXT INTO EXECUTABLE FUNCTIONS, DON'T START MAKING AN AI
translate("How are you doing.",["D:\Programs\Visual Studio Code\development\PAC\\translations\\base.txt","D:\Programs\Visual Studio Code\development\PAC\\translations\localize.txt"])