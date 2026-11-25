import random
s=input("Enter your message: ")
chars="qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM"
words=s.split(" ")
n=int(input("1. Code\n2. Decode\n0.Exit\n(0-2) "))
while True:
    if n==1:
        
        x=""
        for haha in words:
            r1=""
            r2=""
            for i in range(3):
                r1+=random.choice(chars)
                r2+=random.choice(chars)
            if len(haha)>=3:
                x=x+r1+haha[1:]+haha[0]+r2+" "
            else:
                x=x+haha[::-1]+" "
        print(x)
        break
    elif n==2:
        x=""
        for haha in words:
            if len(haha)>=3:
                x=x+haha[-4]+haha[3:-4]+" "
            else:
                x=x+haha[::-1]+" "
        print(x)
        break
    elif n==0:
        break
    else:
        print("Invalid choice")
        break