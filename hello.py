def sayHello(userName):
    print("Hello", userName)

def getUserInput():
    userName = input("Enter your name: ")
    return userName


myName = getUserInput()
sayHello(myName)