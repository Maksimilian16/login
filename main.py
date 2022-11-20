import json


def askin():
    LorR = input("Do U have an account? \n A. Yes\n B. No\n")
    if LorR == "A":
        Log()
    if LorR == "B":
        Reg()
with open('nicks.json', 'r+', encoding='utf-8') as f:
    text = json.load(f)


def Log():
    name = input("print ur name: ")
    passw = input("print ur password: ")
    if name in text and passw == text[name]:
        print("you succesfully logged in")
    else:
        print("name or password is wrong💔")


def Reg():
    Reg_name = input("print name that you want: ")
    if Reg_name in text:
        print("this nickname already is registed")
    else:
        password = input("print ur password: ")
        s = {Reg_name: password}
        text.update(s)
        with open('nicks.json', 'w', encoding='utf-8') as f:
            json.dump(text, f)

askin()
