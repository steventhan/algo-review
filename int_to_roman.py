class Solution:
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        digit_count = 0
        result = ""
        for c in str(num)[::-1]:
            if c != "0":
                result = self.break_down(c, 10**digit_count) + result
            digit_count += 1
        return result

    def break_down(self, digit, count):
        mapping = {
            1: "I",
            4: "IV",
            5: "V",
            9: "IX",
            10: "X",
            40: "XL",
            50: "L",
            90: "XC",
            100: "C",
            400: "CD",
            500: "D",
            900: "CM",
            1000: "M"
        }
        digit = int(digit)

        if 0 < digit < 4:
            return mapping[count]*(digit)
        elif 5 < digit < 9:
            return mapping[5*count] + mapping[count]*(digit-5)
        else:
            return mapping[digit*count]

sol = Solution()
# for i in range(1, 10):
#     print(sol.break_down(str(i), 1000))
print(sol.intToRoman("1994"))
