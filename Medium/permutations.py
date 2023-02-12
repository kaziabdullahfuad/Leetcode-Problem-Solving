class Solution:
    def __init__(self) -> None:
        self.result=[]

    def permute(self,nums:list[int])->list[list[int]]:
        self.backtracking(nums,[])
        return self.result
    
    def backtracking(self,nums,path):
        
        if not nums:
            self.result.append(path)
        
        for i in range(len(nums)):
            
            self.backtracking(nums[:i]+nums[i+1:],path+[nums[i]])
            

        
        
    
    

sol=Solution()

nums=[1,2,3]

holder=nums[1:]

print(holder)

print(sol.permute(nums))

#print(path)


