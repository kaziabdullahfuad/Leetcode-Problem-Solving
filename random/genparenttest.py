class Solution:
    def generateParenthesis(self,n):
        result=[]
        holder=[]
        opener=0
        closer=0
        word=""
        total_size=n*2
        each=n
        self.making(result,word,total_size,each,opener,closer,holder)
        return result
        
    
    # def making(self,result,word,total_size,each,opener):
    #     if len(word)==total_size:
    #         result.append(word)
    #         return
        
    #     if opener<each:
    #         word+="("
    #         self.making(result,word,total_size,each,opener+1)
    #     else:
    #         word+=")"
    #         self.making(result,word,total_size,each,opener)

    # def making(self,result,word,total_size,each,opener,closer):
    #     if len(word)==total_size:
    #         result.append(word)
    #         return
        
    #     if opener<each:
    #         word+="("
    #         self.making(result,word,total_size,each,opener+1,closer)
    #     elif closer<opener and closer<each:
    #         word+=")"
    #         self.making(result,word,total_size,each,opener,closer+1)

    def making(self,result,word,total_size,each,opener,closer,holder):
        
        if len(holder)==total_size:
            result.append("".join(holder))

        holder.append("(")
        self.making(result,word,total_size,each,opener+1,closer,holder)
        holder.pop()
        holder.append(")")
        self.making(result,word,total_size,each,opener,closer+1,holder)
        holder.pop()

        
       
sol1=Solution()
print(sol1.generateParenthesis(3))
