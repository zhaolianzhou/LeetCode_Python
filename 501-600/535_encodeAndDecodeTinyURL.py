class Codec:

    def __init__(self):
        self.longurl=[]
        # self.shorturl=[]
    def encode(self,longUrl):
        """Encodes a URL to a shortened URL.
        :type longUrl: str
        :rtype: str
        """
        self.longurl.append(longUrl)
        return "http://tinyurl/"+str(len(self.longurl)-1)

    def decode(self,shortUrl):
        """Decodes a shortened URL to its original URL.
        :type shortUrl: str
        :rtype: str
        """
        index = shortUrl.split('/')[-1]
        return self.longurl[int(index)]

if __name__=="__main__":
    codec = Codec()
    url="https://leetcode.com/problems/design-tinyurl"
    print codec.encode(url)
    print codec.decode(codec.encode(url))