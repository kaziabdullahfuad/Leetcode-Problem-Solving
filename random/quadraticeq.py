from math import sqrt

def quadratic_explain():
    print(""" To solve the quadratic equation which is given in the form of x^2+bx+c. Enter the value of a b and c. Coefficient of x is a,for bx it's b and for the constant it's c. The formula goes as follows 
    x=(-b+-√b^2-4ac)/2a. The discriminant, b2 – 4ac is represented by the delta symbol, Δ.
    If the discriminant is a positive number, there will be 2 solutions.
    If the discriminant is zero, there will be 1 solution.
    If the discriminant is a negative number, there will not be any real solutions.
    """)

def calculate(a,b,c):
    
    try:
        discriminant=b**2-4*a*c
        delta=sqrt(discriminant)
        if discriminant>0:
            print(f"Since discriminant={discriminant} is greater than zero,there will be 2 solutions")
        elif discriminant==0:
            print("Since discriminant is equal to zero,there will be 1 solution")
        else:
            print(f"Since discriminant={discriminant} is negative, there will be no real solution")
        
        x1=(-b+delta)/2*a
        x2=(-b-delta)/2*a

        print("When x=-b+√b^2-4ac)/2a then x is ",x1)
        print("When x=-b-√b^2-4ac)/2a then x is ",x2)
    
    except:
        print("Error")


quadratic_explain()

#a,b,c=int(input("Enter the value for a b and c, space separated: ")).split() 
a,b,c=[int(x) for x in input("Enter the value for a b and , c, space separated: ").split()]#a=1,b=5,c=2

#print(type(a))
print(a,b,c)

calculate(a,b,c)
