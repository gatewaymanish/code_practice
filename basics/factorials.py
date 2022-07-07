

def fact(n):
    res = n
    while n > 1:
        res = res * (n-1)
        n -= 1
    print(res)


fact(5)




# factorial recurssion
def fact(n):
    if n == 1:
        return 1
    return n * fact(n-1)

print(fact(5))