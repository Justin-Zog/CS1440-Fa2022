# Fractal Visualizer User Manual

Go to the command line and run the file named main.py. You can add the optional arguments: FRACTAL_FILE and PALETTE_NAME if wanted.

## Commands

python src/main.py `[FRACTAL_FILE [PALETTE_NAME]]`

When only one argument is given, it is treated as the fractal file. Because of this you can not paint the default fractal with a different palette.

If no FRACTAL_NAME or PALETTE_NAME is given the program will draw the Octopus fractal with the `Ocean` palette.

The available palettes to use are:
* Ocean
* Forest
* Sunset

## Output

Once a valid fractal file is given, the program will open up a separate window and draw a PNG image of a fractal.
After the picture is drawn, the program will save the fractal as a PNG file to your device in the current working directory.

## Common Errors

If you enter an invalid file, the program will let you know and display an error message.

When this happens you can expect the output to look like so:
`File "/Users/justinherzog/Desktop/CS1440-Fa2022/cs1440-assn5/src/main.py", line 97, in \<module\>
    file = open(sys.argv[1])
           ^^^^^^^^^^^^^^^^^
FileNotFoundError: [Errno 2] No such file or directory: *********`

