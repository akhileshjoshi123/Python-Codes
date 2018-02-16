'''
Write a function to find the longest common prefix string amongst an array of strings.
Assume the input array exclusively consists of non zero length strings containing alphanumeric
characters.

'''

array = ["antibiotics", "antioxidant" , "ant" , "antitheoretical"]


test = len(set([s[:1] for s in array])) 
#checks first character of every string in list

smallestString = min(array,key=len) 
#shortest string (prefix cant be greater than len(shortest string))


def commonprefix(arr,smallestString):
    for i in range(0,len(arr)):
        if arr[i].startswith(smallestString) == False:
            smallestString = smallestString[:-1]
            commonprefix(arr,smallestString)    
    return smallestString


if len(array) == 0 or "" in l:
    print("prefix can't be found")
elif test > 1:
    print("prefix can't be found")
else:
    print("prefix is :" , commonprefix(array,smallestString))
