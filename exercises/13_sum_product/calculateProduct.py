def calculateProduct(numbers):
    if(len(numbers) == 0):
        return 1
    product = 1
    for number in numbers:
        product *= number
    return product

def main():
    assert calculateProduct([]) == 1
    assert calculateProduct([2, 4, 6, 8, 10]) == 3840
    
if __name__ == "__main__":
    main()