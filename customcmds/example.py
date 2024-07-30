def onexec ( args:list ) -> None: # When the command is executed, it will run this function
    print("You can make your own commands!")
# Do note that if you use multiple commands, you will need multiple functions for each one of them.
# (Or you can make it inside the creator for the command class)

def main(t): # Our module is going to be executed from here. t is the termm API.
    
    exampleCommand = t["Command"](name="example", desc="An example command", onexec=onexec, man="Example command. Use it as a base to create your own commands!")
    #^ Creates the command class

    t["registerCommand"](exampleCommand) # -> Register the command so we can execute it

    


