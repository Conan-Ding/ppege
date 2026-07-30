import random

def mode(numbers):
    if not numbers:
        return None
    frequency = {}
    for number in numbers:
        if number in frequency:
            frequency[number] += 1
        else:
            frequency[number] = 1
    frequencyEntries = list(frequency.items())
    modeNum = numbers[0]
    for number, freq in frequencyEntries:
     if freq > frequency[modeNum]:
        modeNum = number
    return modeNum

def main():
    assert mode([]) == None
    assert mode([1, 2, 3, 4, 4]) == 4
    assert mode([1, 1, 2, 3, 4]) == 1
   
    random.seed(42)
    testData = [1, 2, 3, 4, 4]
    for i in range(1000):
        random.shuffle(testData)
        assert mode(testData) == 4

if __name__ == "__main__":
    main()
   