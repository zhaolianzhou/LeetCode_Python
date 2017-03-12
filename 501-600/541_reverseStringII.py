class Soluction():
    def reverseStr(self,s,k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        n = len(s)
        if n < k:
            return s[::-1]
        if n < 2*k:
            tem = s[:k]
            result=tem[::-1]+s[k:]
            return result
        i = 0
        round = n/(2*k)
        print n
        print round
        result=""
        while i < round*2:
            tem1=s[i*k:(i+1)*k]
            tem2 = s[(i+1)*k:(i+2)*k]
            print tem1
            print tem2
            result+=tem1[::-1]+tem2
            i+=2

        if n-2*k*round < k:
            temlast = s[2*k*round:]
            result+=temlast[::-1]
        else:
            temlast = s[2*k*round:2*k*round+k]
            result+=temlast[::-1]+s[2*k*round+k:]
        return result


s = "abcdefg"
sol = Soluction()
print sol.reverseStr(s,1)