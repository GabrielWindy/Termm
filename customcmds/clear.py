import os
# Second "example"
def onexec ( args:list ) -> None: # When the command is executed, it will run this function
    if len(args) == 0:
        if os.name == "nt":
            os.system("cls")
        else:
            os.system("clear")
    elif args[0] == "flsh":
        print("\033[2J\033[H")
    else:
        if os.name == "nt":
            os.system("cls")
        else:
            os.system("clear")
    

def main(t): # Our module is going to be executed from here. 't' is the termm API.
    
    clearCommand = t["Command"](name="clear", desc="Clear the screen", onexec=onexec, man="Use this command to clear out the screen.")
    #^ Creates the command class

    t["registerCommand"](clearCommand) # -> Register the command so we can execute it

    


