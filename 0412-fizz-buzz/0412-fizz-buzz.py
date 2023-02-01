# Time: O(n)
# Space: O(n)

class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        fizzBuzzArr = []
        for num in range(1, n + 1):
            if num % 3 == 0 and num % 5 == 0:
                fizzBuzzArr.append("FizzBuzz")
            elif num % 3 == 0:
                fizzBuzzArr.append("Fizz")
            elif num % 5 == 0:
                fizzBuzzArr.append("Buzz")
            else:
                fizzBuzzArr.append(str(num))
        return fizzBuzzArr