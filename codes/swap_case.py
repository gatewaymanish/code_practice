def is_small_case(c):
    if 97 <= ord(c) <= 122:
        return True
    return False


def swap_char(c):
    if is_small_case(c):
        swap_val = chr(ord(c) - 32)
    else:
        swap_val = chr(ord(c) + 32)
    return swap_val


def swap_case(s):
    result = ''
    for i in range(len(s)):
        swap_val = swap_char(s[i])
        result += swap_val
    return result


# if __name__ == '__main__':
#     s = input()
#     result = swap_case(s)
#     print(result)


## OOPS approach

class SwapCase:
    def __init__(self):
        self.string = input('Enter a string to swap all letters: ')

    @staticmethod
    def is_small_case(char):
        if 97 <= ord(char) <= 122:
            return True
        return False

    @staticmethod
    def swap_char_case(char):
        if is_small_case(char):
            swap_val = chr(ord(char) - 32)
        else:
            swap_val = chr(ord(char) + 32)
        return swap_val

    def swap_case(self):
        res = ''
        for i in range(len(self.string)):
            swap_val = swap_char(self.string[i])
            res += swap_val
        print(res)


obj = SwapCase()
obj.swap_case()


## copilot version
class TextFormatter:
    def __init__(self, text):
        """Initialize with the given text."""
        self.text = text

    def swap_case(self):
        """Swaps uppercase letters to lowercase and vice versa without using swapcase()."""
        swapped_text = ""
        for char in self.text:
            if 'A' <= char <= 'Z':  # Uppercase letter
                swapped_text += chr(ord(char) + 32)  # Convert to lowercase
            elif 'a' <= char <= 'z':  # Lowercase letter
                swapped_text += chr(ord(char) - 32)  # Convert to uppercase
            else:
                swapped_text += char  # Keep non-alphabet characters unchanged
        return swapped_text

# Usage Example
# if __name__ == "__main__":
#     formatter = TextFormatter("Hello World!")
#     print(formatter.swap_case())  # Output: hELLO wORLD!
