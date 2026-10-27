def prime(x):
    if x<0:
        raise ValueError("Can't be negative")
    elif x<=1:
        return False
    for i in range(2,x):
        if x%i==0:
            return False
        return True

try:
    x=int(input("Enter a Number:"))
    y=prime(x)
    if y:
        print("Prime")
    else:
        print("Not a Prime")
except ValueError as e:
    print(e)