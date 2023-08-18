# This is a brainchild of a fever dream. It is most likely useless.

import sys
from Usage import usage
from Encode import encode
from Decode import decode

if len(sys.argv) < 2:
    usage()
    sys.exit(1)
else:
    # sys.argv >= 2 so we should check and see if the [1] element is one of our editors.
    # Gets all arguments that aren't tt.py and the argument after tt.py
    args = []
    for index in range(len(sys.argv)):
        # Gets the arguments after tt.py
        if index > 1:
            args.append(sys.argv[index])

    # Checks which argument they invoked.
    if sys.argv[1] == "encode":
        encode(args=args)
    elif sys.argv[1] == "decode":
        decode(args=args)
    else:
        usage(error="The command you entered is not recognized.")
