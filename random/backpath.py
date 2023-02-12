def printpath(path):
    
    for i in path:
        for j in i:
            print(j,end=' ')
        print('')
 
def findGoal(path,row,column):

    if(row==len(path) or column==len(path)):
        return
    
    if(path[row][column]=='X'):
        return 
    
    if(path[row][column]=='G'):
        print("Found it")
        return
    
    findGoal(path,row,column+1) # to go right increment column by 1
    findGoal(path,row+1,column) # to go down increment row by 1

    print("Monka")
        


# path=[['-'],['-'],['-'], # multiple rows single column
#       ['-'],['-'],['X'],
#       ['X'],['-'],['G']]

path2=[['S','-','-'], # 3 rows 3 column
       ['-','-','X'],
       ['X','-','G']]

#printpath(path)
#print(len(path2))
#printpath(path2)

findGoal(path2,0,0)


    