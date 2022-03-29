# Find most count of each element in array, and find element with highest count

def count (array):
    count = {}
    
    maxcount = 0            #max data
    maxitem = None
    maxdict = {}
    
    for a in array:
        if a not in count:
            
            count[a] = 1
        else:
            count[a] += 1
        
        if count[a] > maxcount:
            maxcount = count[a]
            maxitem = a
            maxdict[maxitem] = maxcount

    print(count)                #freq of all items
    print(maxdict)              # just the max

    
a = [1,1,1,1,1,2,2,3]

count(a)