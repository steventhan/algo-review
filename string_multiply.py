class Solution:
    def multiply(self, num1, num2):

        result = [0] * (len(num1) + len(num2))
        ptr = len(result) - 1
        for i, d2 in enumerate(num2[::-1]):
            temp_ptr = ptr
            for j, d1 in enumerate(num1[::-1]):
                result[temp_ptr] += int(d2) * int(d1)
                result[temp_ptr-1] += result[temp_ptr] // 10
                result[temp_ptr] %= 10
                temp_ptr -= 1
            ptr -= 1

        non_zero = 0
        for i in range(len(result)):
            if result[i] != 0:
                non_zero = i
                break
        print(result)
        return "".join([str(i) for i in result[i:]])

sol = Solution()

print(sol.multiply("34", "56"), 34*56)
