class FizzBuzz_412:
    def __init__(self):
        pass
    def fizzBuzz(self,n):
        result =[]
        for i in range(n):
            if (i+1)%15==0:
                result.append("FizzBuzz")
            elif (i+1)%3==0:
                result.append("Fizz")
            elif (i+1)%5==0:
                result.append("Buzz")
            else:
                result.append(str(i+1))
        return result

myfizz = FizzBuzz_412()
print myfizz.fizzBuzz(15)