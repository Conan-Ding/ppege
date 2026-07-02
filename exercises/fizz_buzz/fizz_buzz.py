def fizzBuzz(upTo=100):
    for number in range(1, upTo + 1):
        if number % 3 == 0 and number % 5 == 0:
            print("FizzBuzz")
        elif number % 3 == 0:
            print("Fizz")
        elif number % 5 == 0:
            print("Buzz")

if __name__ == "__main__":
    upTo = int(input("Enter a number: "))
    fizzBuzz(upTo)