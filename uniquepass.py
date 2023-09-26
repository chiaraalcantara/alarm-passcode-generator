import random 

numberlist = [1111, 2222, 3333, 4444]
newpasslist = []

def uniquePass(numberlist, numpass):
    while (numpass > 0):
        newpass = random.randint(1000, 9999)
        if newpass in numberlist: 
            newpass = random.randint(1000, 9999)
        newpasslist.append(newpass)
        numpass-=1
    for password in newpasslist: 
        print(password)

uniquePass(numberlist, 10)
