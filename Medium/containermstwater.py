class Solution:
    def maxArea(self,height:list[int])->int: # brute force solution O(n*n) solution. O(n^2)
        # Area of a rectangle is found by length * width
        
        if(len(height)==1):
            return
        
        max_area=min(height[0],height[1])*1
        #print(max_area)

        # find the min height and distance and then dist*height.
        # see which one is the max
        for i in range(len(height)-1):
            for j in range(i+1,len(height)):
                minima_height=min(height[j],height[i])
                distance=j-i
                area=minima_height*distance
                if area>max_area:
                    max_area=area
                #print(max_area)

            #print(max_area)
        
        return max_area
                
    def maxareaopti(self,height:list[int])->int:
        left=0
        right=len(height)-1
        max_area=0 # since there won't be negative values

        while(left!=right):
            min_height=min(height[left],height[right])
            distance=right-left
            area=min_height*distance
            max_area=max(max_area,area)

            if(height[left]>height[right]):
                right-=1
            elif(height[left]<=height[right]):
                left+=1
        
        return max_area

obj=Solution()

height=[1,8,6,2,5,4,8,3,7]
#height=[1,3,8,7,2]

#print(obj.maxArea(height))

print(obj.maxareaopti(height))