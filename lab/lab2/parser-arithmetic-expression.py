"""
Author: Linh Vu
"""

import re


def main(input):
    input = "+" + input
    input = re.sub("\s", "", input)

    var_pattern = "(?<=[*+/-])[+-]?[a-z][a-zA-Z0-9_]*?(?=[*+/-]|$)"
    int_pattern = "(?<=[*+/-])[+-]?[0-9]+?(?=[*+/-]|$)"
    float_pattern = "(?<=[*+/-])[+-]?[0-9]*\.[0-9]+?(?=[*+/-]|$)"

    all_vars = re.findall(var_pattern, input)
    for i in range(len(all_vars)):
        input = re.sub(all_vars[i], i*"$" + "X", input)

    input = re.sub(float_pattern, "F", input)
    input = re.sub(int_pattern, "I", input)

    print(input + "\n")


if __name__ == "__main__":
    print("Example 1: num1 + 4.2 - 9")
    input1 = "num1 + 4.2 - 9"
    main(input1)

    print("Example 2: num1 + w * -2")
    input2 = "num1 + w * -2"
    main(input2)

    print("Example 3: num1 * num2 - num3")
    input3 = "num1 * num2 - num3"
    main(input3)

    print("Example 4: num1+4.2-9")
    input4 = "num1+4.2-9"
    main(input4)
