def translate(data):
    match data[-1]:
        case ".":
            pass #Statement or command
        case "?":
            pass #question
        case "!":
            pass #Statement or command
        case _:
            pass #No mark reconizable, no joke spam able to be detected yet
translate("How are you doing.")