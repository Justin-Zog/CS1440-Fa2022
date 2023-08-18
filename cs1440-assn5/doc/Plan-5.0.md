# Software Development Plan

## Phase 0: Requirements Specification *(10%)*

**Deliver:**

All we are doing is refactoring the code that this mathematician wrote and making it cleaner.
* This will require a careful study of what his code is doing and lots of small changes until the program looks beautiful.

This purpose of the program the mathematician made is to graph different parts of the Mandelbrot function.
* A good solution would graph different parts of the Mandelbrot correctly.
* I already know how to code, I just have to decipher this guys code and make it clean and readable.
* The challenges that I can see are trying to understand what his code is saying and getting rid of the putrid pure ugliness of it.
* Using unit tests to ensure our output remains the same will be a key ingredient of doing this effectively.


## Phase 1: System Analysis *(10%)*

**Deliver:**

This program will take some input from the user then use the tkinter module to graph a pattern in the Mandelbrot set.
* The output will take the form of a picture of the pattern the user requested.
* The data we need to graph theses patterns has been provided by the mathematician, we just have to clean up the code he wrote.

### Un-refactored Code
After looking at the code provided by the mathematician I have formed a hypothesis of what functions the program needs.


#### Classes
I think the program could greatly benefit from the creation of an 'Fractal' class
that makes fractals. It could get the data for these fractals from an 'Images' class. These images are contained in a 
dictionary of dictionaries at the bottom of mbrot_fractal.py.

The mathematicians main.py file seems like it does what's expected. Ask the user for input then prints the fractal they asked for.

A palette class that contains color palettes would be useful in cleaning up mbrot_fractal.py

Hopefully this makes the code a lot more readable and understandable.

All other formulae have been provided by the mathematician in his source code... Albeit in a cancerous way.


## Phase 2: Design *(30%)*

#### Functions
Makes sure the user gave valid input and raises an error if they did not.
```
def main():
    Gets the arguments from the user and throws an error if they are invalid.
```
Draws the fractal.
```
def draw_fractal(fractal_name):
    Takes the fractal the user input as an argument.
    Find that fractal in the dictionary of fractals
    Graphs it using tkinter.
```
Gets the color a pixel is supposed to be at some coordinate.
```
def set_pixel_color(coord):
    Takes in a complex number and returns the pixel color for the coordinate.
```
This is in both phoenix_fractal.py and mbrot_fractal.py under different names.
I don't know if it is necessary though.
```
def draw_row():
    draws a row of pixels.
```

## Phase 3: Implementation *(15%)*

**Deliver:**

The only noteable thing is that about halfway through implementation I got a 'weird' error. It turns out my import statement was running the code, which we talked about 
in class. That code was creating a useless tkwindow because I hadn't implemented that yet.

## Phase 4: Testing & Debugging *(30%)*

**Deliver:**

No input error. It is caught and handled by letting the user know their options.

'''
python3 src/main.py 
Please provide the name of a fractal as an argument
phoenix
peacock
monkey-knife-fight
shrimp-cocktail
mandelbrot
mandelbrot-zoomed
spiral0
spiral1
seahorse
elephants
leaf
starfish

'''

Invalid input error. It is caught and handled by letting the user know what options they have to choose from.

'''
python3 src/main.py Blarg_Jaunt 
ERROR: Blarg_Jaunt is not a valid fractal
Please choose one of the following:
phoenix
peacock
monkey-knife-fight
shrimp-cocktail
mandelbrot
mandelbrot-zoomed
spiral0
spiral1
seahorse
elephants
leaf
starfish

'''

## Phase 5: Deployment *(5%)*



## Phase 6: Maintenance

**Deliver:**

The only sloppily written parts of this program is the palette. Specifically the mandelbrot_palette. That thing is just ugly and doesn't make much sense to me.
If a bug was reported in a few months I do not think it would take long to find the cause because of how modularized the program is.

I think the documentation will make sense to other people other than myself. It will definitely make sense to me in 6 months time.

I think it would be relatively easy to add a new feature in a few months. It would be easier if the functions were contained in some sort of class (foresight, that's 
next assignment.).

The program should keep working after upgrading the computer's hardware, operating system. Hopefully python as well, although I hope they improve how tkinter works.

