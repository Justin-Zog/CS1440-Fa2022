
from Usage import usage

# Turns the string into a mangled mess of numbers.
# I am pretty much making my own ASCII
def glitchify(string):
    # Loop through each character and convert it to its base12 number system value.
    for character in string:
        pass



def encode(args) -> []:
    '''Takes A File And Encodes It In a Glitchy Unpredictable Way'''
    encodedFile = []
    # Tell the user they need to put arguments in and the format in which they should do so.
    if len(args) == 0:
        # Lets the user know they need to put arguments and shows them how to use encode.
        usage(error="No arguments provided. Please enter a file to encode.", tool="encode")

    for file in args:
        f = file.open()
        for line in f:
            encodedFile.append(glitchify(line))

        f.close()
