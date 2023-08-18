# Gives errors and jaunt

ENCODE = """tt.py encode FILENAME...
     encodes and prints files in order"""

DECODE = """tt.py decode FILENAME
     decodes and prints files in order"""


def usage(error=None, tool=None):
    # Print a specific error message, if requested
    if error is not None:
        print(f"Error: {error}\n")

    if tool == "encode":
        print(f"\t{ENCODE}")
    elif tool == "decode":
        print(f"\t{DECODE}")
    else:
        print(f"""Python Tools Usage
====================================

{ENCODE}

{DECODE}

""")

    # exit the program
    exit(1)
