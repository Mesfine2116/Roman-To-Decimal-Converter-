def roman_to_decimal(roman):
    roman_numerals = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    decimal = 0
    prev_value = 0

    for numeral in reversed(roman):
        value = roman_numerals.get(numeral)
        if not value:
            return "Invalid Roman numeral"
        if value < prev_value:
            decimal -= value
        else:
            decimal += value
        prev_value = value

    return decimal

def decimal_to_roman(decimal):
    roman_numerals = {1: 'I', 4: 'IV', 5: 'V', 9: 'IX', 10: 'X', 40: 'XL', 50: 'L', 90: 'XC', 100: 'C', 400: 'CD', 500: 'D', 900: 'CM', 1000: 'M'}
    result = ""
    for value, numeral in sorted(roman_numerals.items(), reverse=True):
        while decimal >= value:
            result += numeral
            decimal -= value
    return result

def print_header(title):
    print("\n")
    print(title)
    print()

def main():
    while True:
        print_header("Roman Numeral Converter")
        print("1. Convert Roman numeral to decimal")
        print("2. Convert decimal to Roman numeral")
        print("3. Exit")
        print()
        choice = input("Enter your choice: ")

        if choice == '1':
            print_header("Convert Roman to Decimal")
            roman_numeral = input("Enter a Roman numeral: ").upper()
            decimal_number = roman_to_decimal(roman_numeral)
            print("The decimal equivalent of", roman_numeral, "is:", decimal_number)
        elif choice == '2':
            print_header("Convert Decimal to Roman")
            decimal_number = int(input("Enter a decimal number: "))
            roman_numeral = decimal_to_roman(decimal_number)
            print("The Roman numeral equivalent of", decimal_number, "is:", roman_numeral)
        elif choice == '3':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()
