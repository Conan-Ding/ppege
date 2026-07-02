def ordinalSuffix(number: int) -> str:
    if 10 <= number % 100 <= 20:
        return 'th'
    else:
        last_digit = number % 10
        if last_digit == 1:
            return 'st'
        elif last_digit == 2:
            return 'nd'
        elif last_digit == 3:
            return 'rd'
        else:
            return 'th'
        

def ordinalToCardinal(str: str) -> int:
    if str.endswith('st') or str.endswith('nd') or str.endswith('rd') or str.endswith('th'):
        return int(str[:-2])
    else:
        raise ValueError("Invalid ordinal string")
    
if __name__ == "__main__":
    # Example usage
    number = 23
    suffix = ordinalSuffix(number)
    print(f"The ordinal suffix for {number} is '{suffix}'.")

    ordinal_str = "21st"
    cardinal_number = ordinalToCardinal(ordinal_str)
    print(f"The cardinal number for '{ordinal_str}' is {cardinal_number}.")