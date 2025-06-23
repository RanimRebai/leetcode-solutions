#solved on 2025-06-22
#beats 83% in memory

class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        nums = list()
        i = 0
        while i < len(s):
            if s[i] == 'I':
                if i + 1 < len(s) and s[i + 1] == 'V':
                    nums.append(4)
                    i += 2
                elif i + 1 < len(s) and s[i + 1] == 'X':
                    nums.append(9)
                    i += 2
                else:
                    nums.append(1)
                    i += 1
            elif s[i] == 'X':
                if i + 1 < len(s) and s[i + 1] == 'L':
                    nums.append(40)
                    i += 2
                elif i + 1 < len(s) and s[i + 1] == 'C':
                    nums.append(90)
                    i += 2
                else:
                    nums.append(10)
                    i += 1
            elif s[i] == 'C':
                if i + 1 < len(s) and s[i + 1] == 'D':
                    nums.append(400)
                    i += 2
                elif i + 1 < len(s) and s[i + 1] == 'M':
                    nums.append(900)
                    i += 2
                else:
                    nums.append(100)
                    i += 1
            elif s[i] == 'V':
                nums.append(5)
                i += 1
            elif s[i] == 'L':
                nums.append(50)
                i += 1
            elif s[i] == 'D':
                nums.append(500)
                i += 1
            elif s[i] == 'M':
                nums.append(1000)
                i += 1
        return sum(nums)
