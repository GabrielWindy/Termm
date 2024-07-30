def sep(string: str) -> list[str, list]:

    thing = string.split(' ', 1)
    cmd = thing.pop(0)
    return (cmd, thing)

def findInTable(haystack: list, needle):
    for hay in haystack:
        if hay == needle:
            return True
    return False