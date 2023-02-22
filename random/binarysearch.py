def binary_search(arr,start,end,target):
    if start==end:
        return -1
    
    total=end-start
    mid=int(total/2+start)

    if(arr[mid]==target):
        return mid
    elif(arr[mid]>target):
        return binary_search(arr,start,mid,target)
    elif(arr[mid]<target):
        return binary_search(arr,mid+1,end,target)


#arr=[1,2,3,4,5,6,7,8]
arr=[4,7,8,12,45,99]
#arr=[1]
length=len(arr)
print(binary_search(arr,0,length,45))

