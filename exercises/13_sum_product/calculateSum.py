def calculateSum(numbers):
    if(len(numbers) == 0):
        return 0
    total = 0
    for number in numbers:
        total += number
    return total

def main():
    assert calculateSum([]) == 0
    assert calculateSum([2, 4, 6, 8, 10]) == 30

if __name__ == "__main__":
    main()
