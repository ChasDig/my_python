#  https://leetcode.com/problems/climbing-stairs/description/
#  codes_diagrams/leedcode/70


class Solution:
    def climbStairs(self, n: int) -> int:
        # 1: Solution with recursion O(2^n):
        # if n == 1:
        #     return 1
        #
        # if n == 2:
        #     return 2
        #
        # return self.climbStairs(n=n-1) + self.climbStairs(n=n-2)

        # 2: solution with Fibonacci sequence O(n):
        if n == 1:
            return 1

        first_num, second_num = 1, 1
        total = 0

        for _ in range(2, n + 1):
            total = first_num + second_num
            first_num = second_num
            second_num = total

        return total


# Tests:
test_nums = [1, 2, 3, 5, 9, 11, 14, 88, 55, 101]
solution = Solution()

for num in test_nums:
    print(solution.climbStairs(n=num))
