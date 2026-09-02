numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Two-pointer approach for in-place rearrangement
i = 0  # Pointer for even numbers

for j in range(len(numbers)):
    if numbers[j] % 2 == 0:
        numbers[i], numbers[j] = numbers[j], numbers[i]  # Swap
        i += 1  # Move even pointer forward

print("List with even numbers on the left and odd numbers on the right:\n", numbers)