def area(length, width):
    return length * width

def volume(length, width, height):
    return length * width * height

def perimeter(length, width):
    return  (length + width) * 2

def surfaceArea(length, width, height):
    return 2 * (length * width + length * height + width * height)

def main():
    length = float(input("Enter the length: "))
    width = float(input("Enter the width: "))
    height = float(input("Enter the height: "))
    
    print("Area:", int(area(length, width)))
    print("Volume:", int(volume(length, width, height)))
    print("Perimeter:", int(perimeter(length, width)))
    print("Surface Area:", int(surfaceArea(length, width, height)))

if __name__ == "__main__":
    main()