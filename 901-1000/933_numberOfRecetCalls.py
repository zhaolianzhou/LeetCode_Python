class RecentCounter:

    def __init__(self):
        self.calls = []
        self.count = 0
        return None

    def ping(self, t):
        """
        :type t: int
        :rtype: int
        """
        if not len(self.calls):
            self.calls.append(t)
            self.count += 1
        else:
            while len(self.calls):
                if t-self.calls[0] > 3000:
                    self.calls.pop(0)
                    self.count -= 1
                else:
                    break

            self.calls.append(t)
            self.count += 1
        return self.count


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)