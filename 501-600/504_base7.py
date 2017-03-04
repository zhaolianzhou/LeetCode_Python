class Solution():
    def convertToBase7(self,num):
        if num == 0:
            return "0"
        result=""
        old = num
        num=abs(num)
        while num>0:
            result=str(num%7)+result
            num=num/7
        if old<0:
            result="-"+result
        return result

if __name__=="__main__":
    solu=Solution()
    print solu.convertToBase7(0)
