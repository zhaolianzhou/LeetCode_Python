import math
def generalizedGCD(num, arr):
    # WRITE YOUR CODE HERE
    arr.sort()

    def getAllDividers(n):
        divider_lists = []
        for i in xrange(1, int(math.sqrt(n) + 1)):
            if n % i == 0:
                yield i
                if i * i != n:
                    divider_lists.append(n / i)
        for divider in reversed(divider_lists):
            yield divider

    dividers = list(getAllDividers(arr[0]))

    for i in reversed(dividers):
        for j in range(0, num):
            if arr[j] % i != 0:
                break
        if j == num-1 and arr[j] % i == 0:
            return i

if __name__ == "__main__":
    strs = [2, 4, 6, 8, 10]
    print(generalizedGCD(5, strs))