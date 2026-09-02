# Write
# a
# function
# to
# find
# the
# longest
# common
# prefix
# string
# amongst
# an
# array
# of
# strings.
#
# Input: strs = ["flower", "flow", "flight"]
# Output: "fl"


class MyClass:
    def __init__(self, arr):
        self.arr = arr

        sorted(self.arr)
        result = ''
        tmp = ''
        mydict = {}
        i = 0
        for s in self.arr:
            if len(tmp) == 0:
                tmp = s[i]
            if tmp == s[i] and i < len(s):
                tmp += s[i+1]


