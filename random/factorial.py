def factorial(n):
    if(n==1 or n==0):
        return 1

    prev=factorial(n-1)
    print(n)
    print(prev)
    return n*prev


#print(factorial(4))
print("The one total in main is: ",factorial(4))