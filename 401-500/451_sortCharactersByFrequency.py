import operator
class Solution(object):
    def frequencySort(self,s):
        result=dict()
        for c in s:
            if c in result:
                result[c]+=1
            else:
                result[c]=1
        rs = sorted(result.items(),key=operator.itemgetter(1),reverse=True)
        string_res=''
        for i in rs:
            string_res+=i[0]*i[1]
        return string_res


if __name__=="__main__":
    sol=Solution()
    print sol.frequencySort("aaaccc")
