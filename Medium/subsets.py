class Solution:
    # def subsets(self,nums: list[int]) ->list[list[int]]:
    #     result=[[]]

    #     # for i in range(len(nums)):
    #     #     length=len(result)
    #     #     for j in range(length):
    #     #         #result.append([nums[i]]+result[j])
    #     #         result.append(result[j]+[nums[i]])

    #     for num in nums:
    #         result+=[i+[num] for i in result]


    #     return result

    def subsets(self,nums: list[int]) ->list[list[int]]:
        current=[]
        index=0
        result=[[]]
        result.pop()
        
        self.backtrack(nums,index,current,result)

        return result
    
    def backtrack(self,nums,index,current,result):
        
        if(index==len(nums)):
            result.append(current.copy())
            return

        current.append(nums[index])

        self.backtrack(nums,index+1,current,result)

        current.pop()

        self.backtrack(nums,index+1,current,result)
        
            

obj=Solution()

nums=[1,2,3]


print(obj.subsets(nums))

 

 

