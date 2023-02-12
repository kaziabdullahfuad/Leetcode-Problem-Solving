class Solution:
    
    def twoSum(self,nums: list[int], target: int)-> list[int]: # O(n^2) solution since double loop
        
        index_list=[]
        
        for i in range(len(nums)-1):
            for j in range(i+1,len(nums)): # i+1 since it needs to increment
                if nums[i]+nums[j]==target:
                    index_list.append(i)
                    index_list.append(j)

        return index_list
            
    def twosumopti(self,nums,target): # uses hashmap(dictionaries in python) and O(n) sol
            temp_dict={} # mapping value:index
            result=[]

            for i in range(len(nums)):
                diff=target-nums[i]
                if diff in temp_dict:
                    result.append(temp_dict[diff])
                    result.append(i)
                else:
                    temp_dict[nums[i]]=i # adding the arr value as key and index as value

            #print(temp_dict)
            return result






mysol=Solution()

# arr=[2,3,4]
# target=10

# mysol.twoSum(arr,10)

# print(arr)

#nums=[2,7,11,15]
nums=[3,2,4]
#nums=[3,3]

target=9
target=6

print(mysol.twosumopti(nums,target))

