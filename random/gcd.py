def gcd(x,y):
    
    if(x>y):
        if x%y==0:
            return y
    else:
        if y%x==0:
            return x

    count=0
    #maxer=max(x,y)
    i=2
    gcd_divisor=1
    while(i<x and i<y):
        # print(i)
        # print(x)
        # print(y)
        
        if(x%i==0 and y%i==0):
            x/=i
            y/=i
            gcd_divisor*=i
            count+=1
        else:
            i+=1
    
    #print(count)
    if count==0:
        return 1
    else:
        return gcd_divisor

def euclideangcd(x,y):

    if(x>y):
        if x%y==0:
            return y
        else:
            euclideangcd(x%y,y)
    elif (y>x):
        if y%x==0:
            return x
        else:
            euclideangcd(x,y%x)

def actualeucligcd(x,y):

    if y==0:
        return x # returns x to the return actualeucligcd function call
    else:
        return actualeucligcd(y,x%y) # flipping them. if x=6, y=8 even then no loss since it will be flipped
                              # and next time x will be 8 and y will be 6
                              # also we switch a and b bcs we don't know which one is bigger
    


x=750
y=900

print(gcd(x,y))

print(actualeucligcd(x,y))