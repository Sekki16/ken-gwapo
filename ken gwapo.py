def binary_division(dividend, divisor):
    quotient = 0
    remainder = 0

    for bit in dividend:
        remainder <<= 1
        remainder |= int(bit)
        if remainder >= divisor:
            remainder -= divisor
            quotient <<= 1
            quotient |= 1
        else:
            quotient <<= 1

    return bin(quotient)[2:], bin(remainder)[2:]

def binary_multiplication(num1, num2):
    result = 0
    for bit in num2:
        result <<= 1
        if bit == '1':
            result += int(num1, 2)
    return bin(result)[2:]

def binary_subtraction(minuend, subtrahend):
    result = ""
    borrow = 0

    # Make the lengths of both numbers equal
    minuend = minuend.zfill(len(subtrahend))
    subtrahend = subtrahend.zfill(len(minuend))

    for i in range(len(minuend) - 1, -1, -1):
        diff = int(minuend[i]) - int(subtrahend[i]) - borrow
        if diff < 0:
            diff += 2
            borrow = 1
        else:
            borrow = 0
        result = str(diff) + result

    return result

def binary_addition(num1, num2):
    result = ""
    carry = 0

    # Make the lengths of both numbers equal
    num1 = num1.zfill(len(num2))
    num2 = num2.zfill(len(num1))

    for i in range(len(num1) - 1, -1, -1):
        total = int(num1[i]) + int(num2[i]) + carry
        result = str(total % 2) + result
        carry = total // 2

    if carry:
        result = '1' + result

    return result

def twos_complement(num):
    inverted_num = ''.join('1' if bit == '0' else '0' for bit in num)
    return binary_addition(inverted_num, '1')

def binary_to_decimal(binary):
    decimal = 0
    for digit in binary:
        decimal = decimal * 2 + int(digit)
    return decimal

def decimal_to_binary(decimal):
    binary = ""
    if decimal == 0:
        return "0"
    while decimal > 0:
        binary = str(decimal % 2) + binary
        decimal //= 2
    return binary

def binary_to_octal(binary):
    decimal = binary_to_decimal(binary)
    octal = ""
    while decimal > 0:
        octal = str(decimal % 8) + octal
        decimal //= 8
    return octal

def binary_to_hexadecimal(binary):
    decimal = binary_to_decimal(binary)
    hexadecimal = ""
    while decimal > 0:
        remainder = decimal % 16
        if remainder < 10:
            hexadecimal = str(remainder) + hexadecimal
        else:
            hexadecimal = chr(ord('A') + remainder - 10) + hexadecimal
        decimal //= 16
    return hexadecimal

def octal_to_binary(octal):
    decimal = 0
    for digit in octal:
        decimal = decimal * 8 + int(digit)
    return decimal_to_binary(decimal)

def hexadecimal_to_binary(hexadecimal):
    decimal = 0
    for digit in hexadecimal:
        if '0' <= digit <= '9':
            decimal = decimal * 16 + int(digit)
        else:
            decimal = decimal * 16 + (ord(digit.upper()) - ord('A') + 10)
    return decimal_to_binary(decimal)

def main():
    while True:
        print("\nMenu-1 (Main Menu)")
        print("[1] Binary Operations")
        print("[2] Number System Conversion")
        print("[3] Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            binary_operations()
        elif choice == '2':
            conversion()
        elif choice == '3':
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

def binary_operations():
    while True:
        print("\nMenu-2 (Binary Operations)")
        print("[1] Division")
        print("[2] Multiplication")
        print("[3] Subtraction")
        print("[4] Addition")
        print("[5] Negative (2's Complement)")
        print("[6] Back to Main Menu")
        choice = input("Enter your choice: ")

        if choice == '1':
            dividend = input("Enter the dividend (binary): ")
            divisor = input("Enter the divisor (binary): ")
            quotient, remainder = binary_division(dividend, divisor)
            print("Quotient:", quotient)
            print("Remainder:", remainder)
        elif choice == '2':
            num1 = input("Enter the first number (binary): ")
            num2 = input("Enter the second number (binary): ")
            result = binary_multiplication(num1, num2)
            print("Result:", result)
        elif choice == '3':
            minuend = input("Enter the minuend (binary): ")
            subtrahend = input("Enter the subtrahend (binary): ")
            difference = binary_subtraction(minuend, subtrahend)
            print("Difference:", difference)
        elif choice == '4':
            num1 = input("Enter the first number (binary): ")
            num2 = input("Enter the second number (binary): ")
            result = binary_addition(num1, num2)
            print("Result:", result)
        elif choice == '5':
            num = input("Enter the number (binary): ")
            complement = twos_complement(num)
            print("2's complement:", complement)
        elif choice == '6':
            break
        else:
            print("Invalid choice. Please enter a valid option.")

def conversion():
    while True:
        print("\nMenu-3 (Conversion)")
        print("[1] Binary to X")
        print("[2] Decimal to X")
        print("[3] Octal to X")
        print("[4] Hexa to X")
        print("[5] Back to Main Menu")
        choice = input("Enter your choice: ")

        if choice == '1':
            binary = input("Enter the binary number: ")
            decimal = binary_to_decimal(binary)
            print("Decimal:", decimal)
            print("Octal:", binary_to_octal(binary))
            print("Hexadecimal:", binary_to_hexadecimal(binary))
        elif choice == '2':
            decimal = int(input("Enter the decimal number: "))
            print("Binary:", decimal_to_binary(decimal))
            print("Octal:", decimal_to_binary(decimal))
            print("Hexadecimal:", decimal_to_binary(decimal))
        elif choice == '3':
            octal = input("Enter the octal number: ")
            print("Binary:", octal_to_binary(octal))
            print("Decimal:", binary_to_decimal(octal_to_binary(octal)))
            print("Hexadecimal:", binary_to_hexadecimal(octal_to_binary(octal)))
        elif choice == '4':
            hexadecimal = input("Enter the hexadecimal number: ")
            print("Binary:", hexadecimal_to_binary(hexadecimal))
            print("Decimal:", binary_to_decimal(hexadecimal_to_binary(hexadecimal)))
            print("Octal:", binary_to_octal(hexadecimal_to_binary(hexadecimal)))
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()
