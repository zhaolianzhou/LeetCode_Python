class Solution:
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        uniqueEmailList = []
        for item in emails:
            email, domain_name = item.split('@')
            remove_plus =email.split('+')[0]
            newEmail = remove_plus.replace('.', '')+'@'+domain_name
            if newEmail not in uniqueEmailList:
                uniqueEmailList.append(newEmail)

        return len(uniqueEmailList)


if __name__=="__main__":
    strs = ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]
    solu = Solution()
    print(solu.numUniqueEmails(strs))
