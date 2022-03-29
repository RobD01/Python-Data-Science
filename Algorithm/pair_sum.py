
# Online Python - IDE, Editor, Compiler, Interpreter

# To find pairs of numbers in an array that would sum to k

def pair (array, k):
    c = []                # temporary list to keep track
    if len(array) < 2:
        print ('array too short')       # rule out array that have no numbers
    for a in array:
        for b in array:
            if a + b == k:              # iterate through all numbers
                d = (a,b)               # temp variable to make a pair tuples that sum to k
                c.append(d)             # list to keep track of pairs
    e = set(c)                          # remove repeats
    print(e)

    if len(e) == 0:
        print ('No pairs')

    megaman = """Here's a megaman

    ░░░░░░░░░░▄▄█▀▀▄░░░░
    ░░░░░░░░▄█████▄▄█▄░░░░
    ░░░░░▄▄▄▀██████▄▄██░░░░
    ░░▄██░░█░█▀░░▄▄▀█░█░░░▄▄▄▄
    ▄█████░░██░░░▀▀░▀░█▀▀██▀▀▀█▀▄
    █████░█░░▀█░▀▀▀▀▄▀░░░███████▀
    ░▀▀█▄░██▄▄░▀▀▀▀█▀▀▀▀▀░▀▀▀▀
    ░▄████████▀▀▀▄▀░░░░
    ██████░▀▀█▄░░░█▄░░░░
    ░▀▀▀▀█▄▄▀░██████▄░░░░
    ░░░░░░░░░█████████░░░░
    """

    print (megaman)


a = [1,3,2,2,5,5,7]
b = 15

pair(a,b)
