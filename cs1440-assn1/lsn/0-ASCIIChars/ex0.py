# Justin Herzog A02306067
def displayASCII():
    # I think making an array and printing each item would be the easiest way to code this
    printableASCIIs = []
    # Puts all printable ASCII character codes in the array
    for i in range(32, 127):
        printableASCIIs.append(i)

    # Put a print statement in here.
    for i in printableASCIIs:
        print(f"chr({i}) = " + chr(i))


if __name__ == '__main__':
    displayASCII()
