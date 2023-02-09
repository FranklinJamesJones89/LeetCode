#! python3

class Solution:
    def is_anagram(self, s, t):
        s_count = 0
        for x in s:
            if x in t:
                s_count += 1
        for y in t:
            if y not in s:
                s_count -= 1

        if s_count == len(s):
            print('True')
        elif len(s) < len(t):
            print('False')

def anagram(string):
    new_string = string[::-1]
    if string == new_string:
        print('True')
    else:
        print('False')

anagram('mom')

