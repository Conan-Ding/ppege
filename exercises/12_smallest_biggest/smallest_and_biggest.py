def getSmallest(numbers):
    if(len(numbers) == 0):
        return None
    smallest = numbers[0]
    for number in numbers:
        if number < smallest:
            smallest = number
    return smallest

def getBiggest(numbers):
    if(len(numbers) == 0):
        return None
    biggest = numbers[0]
    for number in numbers:
        if number > biggest:
            biggest = number
    return biggest

def main():
    assert getSmallest([1, 2, 3]) == 1
    assert getSmallest([3, 2, 1]) == 1
    assert getSmallest([28, 25, 42, 2, 28]) == 2
    assert getSmallest([1]) == 1
    assert getSmallest([]) == None

if __name__ == "__main__":
    main()