# To maximum sum in an array

def maxsum(array):
    if len(array) == 0:     # Rule out when array is empty
        print ('Empty Array')
    total = 0               # counter to keep track of total
    for a in array:
        if a > 0:           # rule out 0 and negatives. Only positive numbers can make a larger sum
            total += a
    print(total)

a = [1,2,3,4,-5, -20]       #ignores all negatives.         

maxsum(a)

    