#! python3

class Solution:
    def plus_one(self, digits):
        str_digits = []
        for i in digits:
            str_digits.append(str(i))
        join_list = ''.join(str_digits)
        num_list = int(join_list) + 1
        new_digits = []
        for x in str(num_list):
            new_digits.append(x)
        print(int(new_digits))

test = Solution()
nums = [9]
test.plus_one(nums)
