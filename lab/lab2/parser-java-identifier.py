"""
The program check whether the input is legitimate and customary 
Java variable identifier.

Author: Linh Vu (linh.vu.200043@student.fulbright.edu.vn)
"""
import re


def main(javaIdentifier):
    pattern = "^[a-z][a-zA-Z0-9_]+$"

    # certify whether the input is a valid identifier name or not
    check = re.search(pattern, javaIdentifier)

    if check:
        print("This is a valid name for Java identifier")

        # replace each identifier with an X
        sub_pattern = "[a-zA-Z0-9_]+"
        newName = re.sub(sub_pattern, "X", javaIdentifier)
        print(newName)
    else:
        print("This is not a valid name for Java identifier")


if __name__ == "__main__":
    javaIdentifier = input("Input the Java identifier name here: ")
    main(javaIdentifier)
