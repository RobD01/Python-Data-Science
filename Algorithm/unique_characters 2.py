# given a string, list all characters that are not repeated

def unique(string):
    
    charcount = {}
    unique = []
    
    newstring = string.replace(' ','').lower()
    
    for a in newstring:
        if a not in charcount:
            charcount[a] = 1
        else:
            charcount[a] += 1
    
    print(f'Count: {charcount}')
    
    for a in charcount:
        if charcount[a] == 1:
            unique.append(a)
            
    print(f'Unique: {unique}')
    
        

string = "ad1a aaaaa ddd dd22223"

unique(string)

    