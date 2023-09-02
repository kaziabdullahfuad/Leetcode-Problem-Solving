rows=int(input("Enter the number of rows:"))

for i in range(0,rows): # no of rows

    # no of spaces
    for j in range(rows-i-1):
        print(" ",end="")
    
    # no of asteriks
    for k in range(2*i+1): # 2*i+1 always makes odd numbers
        print("*",end="")
    
    print()
    