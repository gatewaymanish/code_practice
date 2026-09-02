def is_leap(year):
    leap = True

        if year % 4 != 0:
            leap = False
            break
        if year % 100 != 0:
            leap = False
            break
        if year % 400 != 0:
            leap = False
            break

        year = year - 4
    return leap


# year = int(input())
year = 1990
print(is_leap(year))