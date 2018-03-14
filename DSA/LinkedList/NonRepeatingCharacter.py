MAX_CHAR = 256

def NonRepeatingCharacter():

    inDLL = []#*MAX_CHAR
    repeated = [False]*MAX_CHAR
    N = int(input())
    c = input() # Taking a stream of chracters with spaces in between eg: (a a b c) ( a a c v).....
    for i in range(0,len(c),2):
        x = c[i]
        if not repeated[ord(x)]:
            if not x in inDLL:
                inDLL.append(x)
            else:
                inDLL.remove(x)
                repeated[ord(x)] = True
        if len(inDLL)!=0:
            print (inDLL[0],end=' ')
        else:
            print("-1", end = ' ')


T =int(input())

for i in range(T):
    NonRepeatingCharacter()
    print()
