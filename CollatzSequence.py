print("name : monalisa\n usn : 1AY24AI073\n section : O ")
def collatz(n):
    while n != 1:
        print(n, end=' -> ')
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
    print(1)

# Example usage:
try:
    number = int(input("Enter a positive integer: "))
    if number > 0:
        collatz(number)
    else:
        print("Please enter a number greater than 0.")
except ValueError:
    print("Invalid input. Please enter an integer.")
