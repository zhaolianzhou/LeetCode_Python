from operator import itemgetter
class Solution(object):
    def findLonelyPixel(self,picture):
        n=len(picture)
        m=len(picture[0])
        row = [0]*n
        col = [0]*m
        pic = [[False]*m for i in range(n)]
        result = 0
        for i in range(n):
            for j in range(m):
                if picture[i][j]=='B':
                    row[i]+=1
                    col[j]+=1
                    pic[i][j]=True
                    result+=1
        for i in range(n):
            if row[i]>1:
                for j in range(m):
                    if pic[i][j]==True:
                        result-=1
                        pic[i][j]=False
        for j in range(m):
            if col[j]>1:
                for i in range(n):
                    if pic[i][j]==True:
                        result-=1
                        pic[i][j]=False
        return result



if __name__=="__main__":
    solu = Solution()
    pic=[['B','B','B'],['B','B','B'],['B','B','B']]
    print solu.findLonelyPixel(pic)