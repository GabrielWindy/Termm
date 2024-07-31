import os
import importlib.util
import strutils
import sys

# defines

class Command:
    def __init__(self, name: str, desc: str, onexec, man: str):
        self.name = name
        self.desc = desc
        self.onexec = onexec
        self.man = man
    def execute(self, params):
        try:
            self.onexec(params)
        except Exception as ex:
            print(f"Error executing {self.name}:\n{ex}")


loading_path  = ".\\customcmds" # Default loading path for custom cmds
loaded_modules = [] # List of loaded modules, for the 'modules' command
commands = [] # List of loaded in commands

if not os.path.exists(loading_path): os.mkdir(loading_path) # Fix possible folder exclusion problems

# funcs
def isMain() -> bool:
    return __name__ == "__main__"

def getCommand (cmd: str) -> Command | bool:
    for _cmd in commands:
        if _cmd.name == cmd:
            return _cmd
    return False

def run (cmd: str, args: list = []):
    try_command = getCommand(cmd)
    if not try_command:
        print(f"Command '{cmd}' not found!")
    else:
        try_command.execute(args)

def registerCommand (cmd: Command):
    if type(cmd) != Command or strutils.findInTable(commands, cmd):
        print("Attempted to register an invalid command, ignoring...")
        return
    commands.append(cmd)
## pre init header ##

print(f"""Termm v0.0.1 (Pre-Release)
{strutils.pickSplash()}
--------------------------------------------------------------------
""")

## default commands ##

# man

def __manExec (args: list):
    if len(args) == 0:
        print("Usage: man <command>")
        return
    
    _cmd = getCommand(args[0])
    if not _cmd:
        print("Command not found!")
        return
    print(_cmd.man)

_man = Command("man", "Manual", __manExec, "Command used to describe a certain command.\nUsage: man <command>")

if isMain(): registerCommand(_man)

# cmds

def __commdsExec (args: list):
   print("---------------------------------------------------------")
   print("                   Command | Description")
   print("exit | Quits Termm")
   for cmd in commands:
       print(f"{cmd.name} | {cmd.desc}")
   print("\n---------------------------------------------------------")

_commds = Command("cmds", "List of commands", __commdsExec, "List all avaible registered commands")

if isMain(): registerCommand(_commds)

# sys

def __sysExec (args: list):
    os.system(''.join(str(e) for e in args))

_sys = Command("sys", "Execute OS command", __sysExec, "Execute a system command.\nUsage: sys <command>")

if isMain(): registerCommand(_sys)



##########################################################
# Load Custom Cmds


def loadCustoms ():
    
    custom_cmds = [f for f in os.listdir(loading_path) if f.endswith(".py")]

    for cmdd in custom_cmds:
        
        path_to = os.path.join(loading_path, cmdd)
        cmdd_name = cmdd[:-3] # Remove the .py
        if strutils.findInTable(loaded_modules, path_to): continue

        spec = importlib.util.spec_from_file_location(cmdd_name, path_to)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        if hasattr(module, "main") and callable(module.main):
            module.main(globals()) # Provides all the funcs it needs and the variables
            print("Loaded in module '", cmdd_name, "'")
        loaded_modules.append(path_to)

        

if isMain(): loadCustoms() # Prevent double loading if a plugin so happens to import termm (bad idea)

# modules

def __modulesExec (args: list):
    if len(args) == 0:
        pass
    elif args[0] == "rescan":
        print("Scanning for new modules...")
        loadCustoms()
        print("Done!")
        return
    elif args[0] == "open":
        os.startfile(loading_path)
        return
    
    if len(loaded_modules) == 0:
        print("No modules loaded.")
    print("---------------------------------------------------------")
    print("                   Module Name")
    for mod in loaded_modules:
        print(f"==> {mod}")
    print("\n---------------------------------------------------------")

_modules = Command("modules", "List of modules", __modulesExec, "Shows the list of currently loaded modules.\nUse 'rescan' as am argument to rescan for any possible new modules.\nUse 'open' as an argument to open the loading path in your file explorer.")


if isMain(): registerCommand(_modules)
###################### MAIN LOOP ###################################

while True:
    if not isMain():
        break

    command = input(">")
    if command == "exit" or command == "ex":
        sys.exit(0)        


    command, args = strutils.sep(command)
    
    if not command == '': run(command, args)

