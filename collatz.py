def collatz(number):
    try:
        return n / 1
    except ValueError:
        print('Error: must input a numeral.')
    if number % 2 == 0:
        print(number // 2)
    elif number % 2 == 1:
        print(3 * number + 1)

n = input()
n = int(n)
collNumber = collatz(n)
print(collNumber)
