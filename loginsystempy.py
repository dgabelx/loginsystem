
def login(name,password):
    success = False
    file = open("user_details.txt","r")
    for i in file:
        a,b = i.split(",")
        b = b.strip()
        if(a==name and b==password):
            success=True
            break
    file.close()
    if(success):
        print("login successfull!")
        print("welcome to davids coding program")
    else:
        print("worng username or password")
def register(name, password):
    file = open("user_details.txt", "a")
    file.write("\n"+name+","+password)
    file.close()
def access(option):
    if(option=="login"):
        name=input("Enter your name: ")
        password=input("Enter your password: ")
        login(name,password)
    else:
        print("Enter your name and password to register")
        name = input("Enter your name: ")
        password= input ("Enter your password:")
        register(name, password)
def begin():
    global option
    print("Welcome to Davids coding program")
    option = input("Login or Register (type login or reg):")
    if(option!="login" and option!="reg"):
        begin()

begin()
access(option)    
