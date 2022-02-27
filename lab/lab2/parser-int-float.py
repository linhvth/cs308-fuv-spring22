"""
Author: Linh Vu (linh.vu.200043@student.fulbright.edu.vn)
"""

import re


def main(num):
    print("Input: {}".format(num))

    intPattern = "^[+-]?[0-9]+$"
    floatPattern = "^[+-]?[0-9]*\.[0-9]+$"
    # [+-]? matches an optional "+", "-", or an empty string
    # ^, $: start-of-line and end-of-line respectively
    # \. matches "."

    if re.search(intPattern, num):
        print("This is an integer")
        print(re.sub(intPattern, "I", num))
        print()

    elif re.search(floatPattern, num):
        print("This is a float")
        print(re.sub(floatPattern, "F", num))
        print()
    else:
        print("This input is neither an integer nor a float\n")


if __name__ == "__main__":
    #num = input("Enter string to test if integer or float: ")
    num1 = "12"
    main(num1)

    num2 = "-12"
    main(num2)

    num3 = "1.2"
    main(num3)

    num4 = ".12"
    main(num4)

    num5 = "-.12"
    main(num5)

    num6 = "12.4abc"
    main(num6)
