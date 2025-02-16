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
        if is_small_case(s[i]):
            swap_val = swap_char(s[i])
            result += swap_val
    return result


if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)