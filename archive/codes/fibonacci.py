# program to create fibonacci sequence up to n numbers
# example if n = 10, output should be [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]


# fibonacci sequence
def fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        fib_sequence = [0, 1]
        while len(fib_sequence) < n:
            next_fib = fib_sequence[-1] + fib_sequence[-2]
            fib_sequence.append(next_fib)
        return fib_sequence         

    
# Example usage
n = 10  # Change this to the desired number of Fibonacci numbers
result = fibonacci(n)
print(result)   


'''
# pseudocode for fibonacci sequence
function fibonacci(n):
    if n <= 0:
        return empty list
    else if n == 1:
        return list with [0]
    else if n == 2:
        return list with [0, 1]
    else:
        initialize fib_sequence as list [0, 1]
        while length of fib_sequence < n:
            next_fib = fib_sequence[last] + fib_sequence[second last]
            append next_fib to fib_sequence
        return fib_sequence
'''
