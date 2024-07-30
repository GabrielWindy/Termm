# String or whatever tools for the main file
import random

def sep(string: str) -> list[str, list]:

    thing = string.split(' ', 1)
    cmd = thing.pop(0)
    return (cmd, thing)

def findInTable(haystack: list, needle):
    for hay in haystack:
        if hay == needle:
            return True
    return False

header_splash = [
    "Have a nice day!",
    "Did you know 'ex' also quits Termm?",
    "If you type in 'cmds' you will see the list of avaible commands.",
    "You can modify those random messages at strutils.py",
    "If the battle is sure to result in victory then you must fight!",
    "Yes, later on this will be ported to either C++ or Rust (with lua for commands)",
]

def pickSplash() -> str:
    return random.choice(header_splash)