import random 
import pandas as pd

oldpasscodes = pd.read_csv(filepath)

def uniquePass(numberlist, numpass):
    newpasslist = []
    while (numpass > 0):
        newpass = random.randint(1000, 9999)
        if newpass in numberlist: 
            newpass = random.randint(1000, 9999)
        newpasslist.append(newpass)
        numpass-=1
    for password in newpasslist: 
        print(password)

def main(filepath):
    oldpasscodes = pd.read_csv(filepath)
    return oldpasscodes