# Justin Herzog A02306067
import os
import sys
from ex1 import getFileSafely
# If the above import is used, be sure *no additional output is printed* by
#   getFileSafely, otherwise the tests will fail.

def printContents1(file):
    print(file.read(), end="")


def printContents2(file):
    fileLines = file.readlines()
    stringToPrint = ""
    for i in fileLines:
        stringToPrint = (stringToPrint + i)

    print(stringToPrint, end="")

def printTwice(filename):
    safeFile = getFileSafely(filename)
    printContents1(safeFile)
    safeFile.seek(0)
    printContents2(safeFile)
    safeFile.close()


if __name__ == '__main__':
    cwd = os.getcwd()
    print(f"Please enter a file path relative to {cwd}")
    filename = input("File Path: ")
    printTwice(filename)
