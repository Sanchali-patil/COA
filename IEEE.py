# B2: IEEE 754 Floating Point Converter
# Single Precision (32-bit)


import struct
import math


# -----------------------------------
# 1. Decimal to IEEE 754
# -----------------------------------

def decimal_to_ieee(number):

    try:
        packed = struct.pack('>f', number)

    except OverflowError:
        number = math.copysign(float('inf'), number)
        packed = struct.pack('>f', number)

    bits = ''.join(format(byte, '08b') for byte in packed)

    sign = bits[0]
    exponent = bits[1:9]
    mantissa = bits[9:]

    hexadecimal = packed.hex().upper()

    print("\n========== IEEE 754 REPRESENTATION ==========")

    print("Decimal Number:", number)

    print("\nSign Bit:", sign)
    print("Exponent:", exponent)
    print("Mantissa:", mantissa)

    print("\n32-bit Binary:", bits)
    print("Hexadecimal:", hexadecimal)

    check_special(bits)


# -----------------------------------
# 2. Special Value Detection
# -----------------------------------

def check_special(bits):

    sign = bits[0]
    exponent = bits[1:9]
    mantissa = bits[9:]

    if exponent == '00000000' and mantissa == '00000000000000000000000':

        if sign == '0':
            print("Special Value: Positive Zero (+0)")
        else:
            print("Special Value: Negative Zero (-0)")

    elif exponent == '11111111':

        if mantissa == '00000000000000000000000':

            if sign == '0':
                print("Special Value: Positive Infinity (+Infinity)")
            else:
                print("Special Value: Negative Infinity (-Infinity)")

        else:
            print("Special Value: NaN (Not a Number)")

    elif exponent == '00000000':

        print("Special Category: Subnormal Number")

    else:
        print("Special Value: Normal Number")


# -----------------------------------
# 3. IEEE 754 Binary to Decimal
# -----------------------------------

def binary_to_decimal(bits):

    if len(bits) != 32 or any(b not in '01' for b in bits):
        print("Error: Enter exactly 32 binary digits.")
        return

    data = int(bits, 2).to_bytes(4, byteorder='big')

    number = struct.unpack('>f', data)[0]

    print("\n========== BINARY TO DECIMAL ==========")

    print("Binary:", bits)

    print("Sign Bit:", bits[0])
    print("Exponent:", bits[1:9])
    print("Mantissa:", bits[9:])

    print("Decimal Value:", number)

    check_special(bits)


# -----------------------------------
# 4. Hexadecimal to Decimal
# -----------------------------------

def hexadecimal_to_decimal(hex_value):

    hex_value = hex_value.strip().replace("0x", "").replace("0X", "")

    if len(hex_value) != 8:
        print("Error: Enter exactly 8 hexadecimal digits.")
        return

    try:
        data = bytes.fromhex(hex_value)

        bits = ''.join(format(byte, '08b') for byte in data)

        number = struct.unpack('>f', data)[0]

        print("\n========== HEX TO DECIMAL ==========")

        print("Hexadecimal:", hex_value.upper())
        print("Binary:", bits)
        print("Decimal Value:", number)

        check_special(bits)

    except ValueError:
        print("Invalid hexadecimal input.")


# -----------------------------------
# 5. Main Menu
# -----------------------------------

while True:

    print("\n======================================")
    print("       IEEE 754 CONVERTER")
    print("       SINGLE PRECISION (32-BIT)")
    print("======================================")

    print("1. Decimal to IEEE 754")
    print("2. Binary to Decimal")
    print("3. Hexadecimal to Decimal")
    print("4. Exit")

    choice = input("\nEnter your choice: ")

    if choice == '1':

        try:
            value = float(input("Enter Decimal Number: "))

            decimal_to_ieee(value)

        except ValueError:
            print("Invalid decimal number.")

    elif choice == '2':

        bits = input("Enter 32-bit Binary Number: ").strip()

        binary_to_decimal(bits)

    elif choice == '3':

        hex_value = input("Enter 8-digit Hexadecimal Number: ")

        hexadecimal_to_decimal(hex_value)

    elif choice == '4':

        print("Program terminated.")
        break

    else:
        print("Invalid choice. Try again.")