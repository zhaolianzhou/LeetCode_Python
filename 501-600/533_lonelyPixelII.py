from operator import itemgetter
class Solution(object):
    def findLonelyPixel(self,picture,N):
        n=len(picture)
        m=len(picture[0])
        row = [0]*n
        col = [0]*m
        result = 0
        for i in range(n):
            for j in range(m):
                if picture[i][j]=='B':
                    row[i]+=1
                    col[j]+=1

        resultList=[]
        for j in range(m):
            if col[j]==N:
                R = []
                curr_row=0
                for i in range(n):
                    if picture[i][j]=='B':
                        if not R and row[i]==N:
                            R=picture[i]
                            result+=1
                            curr_row+=1
                        elif picture[i]==R and row[i]==N:
                            result+=1
                            curr_row += 1
                        else:
                            result-=curr_row
                            break
        return result

if __name__=="__main__":
    solu = Solution()
    pic=["WBWBBW","WBWBBW","WBWBBW","WWBWBW"]
    print solu.findLonelyPixel(pic,3)