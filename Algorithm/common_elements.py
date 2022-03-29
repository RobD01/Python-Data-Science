# for each array, find what what elements they have in common

def common(array1,array2):
    c = []
    for a in array1:
        if a in b:
            c.append(a)
    print (c)
        
    

a = [1,3,4,6,7,9]
b = [1,2,4,5,9,10]

common(a,b)

