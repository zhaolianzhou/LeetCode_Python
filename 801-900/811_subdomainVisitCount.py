class Solution:
    def subdomainVisits(self, cpdomains):
        """
        :type cpdomains: List[str]
        :rtype: List[str]
        """
        domain_pair = {}
        for domain in cpdomains:
            count, full_domain = domain.split(' ')
            sub_domains = full_domain.split('.')
            current_sub = ''
            for item in sub_domains[::-1]:
                if current_sub == '':
                    current_sub = item
                else:
                    current_sub = item+'.'+current_sub
                if current_sub in domain_pair:
                    domain_pair[current_sub]+= int(count)
                else:
                    domain_pair[current_sub] = int(count)

        result = []
        for k, v in domain_pair.items():
            result.append(str(v)+' '+k)

        return result

if __name__ == "__main__":
    strs = ["900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"]
    solu = Solution()
    print(solu.subdomainVisits(strs))

