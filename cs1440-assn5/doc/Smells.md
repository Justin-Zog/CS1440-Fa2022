# Code Smells Report - 5.0

## Code Smells

0. Unreachable Code at `mbrot_fractal.py` [line 185]
     * The `break` statement happens after `continue`. If the break is never run, why is it there?
     * ```python
        elif abs(z) > seven:  	    	       
            print("You should never see this message in production", file=sys.stderr)  	    	       
            continue  	    	       
            break  	    	       
       ```
     * This is easily resolved by removing the `break` statement.

1. Complex decision tree in `mbrot_fractal.py` [line 166-190]
     * The `elif` statement runs nothing but `continue` so the branch isn't really necessary.
     * There is another `elif abs(z) > seven` statement that will never get hit becuase the statement previous to it is `if abs(z) > TWO`,
and if it ever did (which is impossible) it just says it's not supposed to be hit. That's not to mention having variabled named after numbers or the useless comment block.
     * ```python
        if abs(z) > TWO:  	    	       
            z = float(TWO)  	    	       
            # XXX: the program used to crash with the error  	    	       
            #   TypeError: 'int' object is not callable  	    	       
            #  	    	       
            # maybe it had something to do with 'len' being an integer variable  	    	       
            # instead of a function variable.  	    	       
            # Somebody from StackOverflow suggested I do it this way  	    	       
            # IDK why, but it stopped crashing, and taht's all that matters!  	    	       
            import builtins  	    	       
            len = builtins.len  	    	       
            if iter >= len(palette):  	    	       
                iter = len(palette) - 1  	    	       
            return palette[iter]  	    	       
        elif abs(z) < TWO:  	    	       
            continue  	    	       
        elif abs(z) > seven:  	    	       
            print("You should never see this message in production", file=sys.stderr)  	    	       
            continue  	    	       
            break  	    	       
        elif abs(z) < 0:  	    	       
            print(f"This REALLY should not have happened! z={z} iter={iter} MAX_ITERATIONS={MAX_ITERATIONS}", file=sys.stderr)  	    	       
            sys.exit(1)  	    	       
        else:  	    	       
            pass
       ```
     * An easy way to fix this is to only run statements that matter, use normal numbers instead of variables named after numbers, and put continue in the `else` statement if it actually is necessary.

2. Magic Number Global Variables in `mbrot_fractal.py` [line 50, 114-117]
     * There are many useless global variables that are used as 'magic numbers' later in the program.
     * ```python
       (line 50)
            MAX_ITERATIONS = -1
       (line 114-117)
            MAX_ITERATIONS = 115  	    	       
            z = 0  	    	       
            seven = 7.0  	    	       
            TWO = 2
       ```
     * Why was MAX_ITERATIONS redifined before it was ever used? Why is MAX_ITERATIONS either -1 or 115?
     * There is literally no reason whatsoever that seven or TWO should ever be defined.
     * An easy way to fix this is to explain the magic numbers with a comment and to just use the gosh-darn number 2 when coding.

3. Poorly Named Variable in `mbrot_fractal.py` [line 159-162]
     * There is a global declared within a function named 'iter' which shadows the built in name 'iter'.
     * There is a variable named 'len' which is then assigned to the global magic number 'MAX_ITERATIONS'. Obviously 'len' is shadows, 'len'.
     * ```python
        global MAX_ITERATIONS  	    	       
        global iter  	    	       

        len = MAX_ITERATIONS
       ```
     * An easy fix for this would be to get rid of literally all of these variables because they don't serve a purpose. Or to give them better names.

4. Dead code in `mbrot_fractal.py` [lines 123-152]
     * There is an entire function commented out. A function with the exact same name exists below the commented out one and contains the exact same code as the comment.
          There is no need for the comment.
     * ```python
       # def colorOfThePixel(c, palette):  	    	       
       #     """Return the color of the current pixel within the Mandelbrot set"""  	    	       
       #     global z  	    	       
       #     z = complex(0, 0)  # z0  	    	       
       #  	    	       
       #     global MAX_ITERATIONS  	    	       
       #     global iter  	    	       
       #  	    	       
       #     len = MAX_ITERATIONS  	    	       
       #     for iter in range(len):  	    	       
       #         z = z * z + c  # Get z1, z2, ...  	    	       
       #         global TWO  	    	       
       #         if abs(z) > TWO:  	    	       
       #             z = float(TWO)  	    	       
       #             if iter >= len(palette):  	    	       
       #                 iter = len(palette) - 1  	    	       
       #             return palette[iter]  	    	       
       #         elif abs(z) < TWO:  	    	       
       #            continue  	    	       
       #         elif abs(z) > seven:  	    	       
       #             print("You should never see this message in production", file=sys.stderr)  	    	       
       #             continue  	    	       
       #             break  	    	       
       #         elif abs(z) < 0:  	    	       
       #             print(f"This REALLY should not have happened! z={z} iter={iter} MAX_ITERATIONS={MAX_ITERATIONS}", file=sys.stderr)  	    	       
       #             sys.exit(1)  	    	       
       #         else:  	    	       
       #             pass  	    	       
       #  	    	       
       #     return palette[iter]  # The sequence is unbounded  	
       ```
* An easy way to fix that is to delete the comment.

5. Redundant code in `mbrot_fractal.py` [lines 30-41]
     * There are a few import statements that are repeated. The second time they import it doesn't do anything more than the first import did.
     * ```python
        import sys  	    	       
        import time  	    	       
        from tkinter import Tk, Canvas, PhotoImage, mainloop  	    	       
        from math import sqrt, cos, cosh, sin, sinh, remainder, acos, acosh, asin, asinh  	    	       

        # These are the imports that I usually import  	    	       
        import turtle  	    	       
        import os  	    	       
        import os.path  	    	       
        import sys  	    	       
        import time  	    	       
        import math  	   
       ```
     * An easy fix for this bug is to only import what you need and only import it once.

6. Too Many Arguments in `phoneix_fractal.py` [line 128]
     * There are way too many arguments, the arguments could have more descriptive names too.
     * ```python
        def makePictureOfFractal(f, i, e, w, g, p, W, s):
       ```
     * A fix would be to see if the function even uses all of these and delete the uneccessary ones.
     * I'm pretty sure at least 3 of the arguments in this function are never used.
     * The arguments need better names too, I have no clue what any of those are suppose to be just by looking at it.

7. Function/Method that is too long in `phoenix_fractal.py` [lines 128-211]
     * I won't provide the code here, but it should suffice to say that a function should not be almost 100 lines of code long.
     * A fix for this would be to split up the functionality of this function into a few functions of manageable sizes.

8. Comments that share too much information in `phoneix_fractal.py` [lines 176-201]
     * Of the 26 lines of code mentioned, 16 are comments and 10 are actual code.
        If you need more comments than code, your code could most likely be better written.
     * To fix this, the variables could have better names to allow for autological code that explains itself.
        doing this would limit the amount of comments necessary to understand the code.

9. Spaghetti code in `phoenix_fractal.py` [lines 109-126]
     * This whole function just hurts to look at. It is also definitely easier to rewrite it than try to understand what it does.
     * ```python
        def getFractalConfigurationDataFromFractalRepositoryDictionary(dictionary, name):  	    	       
       """Make sure that the fractal configuration data repository dictionary  	    	       
       contains a key by the name of 'name'  	    	       

       When the key 'name' is present in the fractal configuration data repository  	    	       
       dictionary, return its value.  	    	       

       Return False otherwise  	    	       
       """  	    	       
       for key in dictionary:  	    	       
           if key in dictionary:  	    	       
               if key == name:  	    	       
                   value = dictionary[key]  	    	       
                   return key  	    	       


       Save_As_Picture = True  	    	       
       tkPhotoImage = None  	
       ```
     * A fantastic fix for this would be to rewrite this function and give it a better name. Although I think it might be able to be re-written as an if statement wherever it is used.

10. Lying comment in `main.py` [lines 56-57]
     * ```python
       # quit when too many arguments are given  	    	       
       if len(sys.argv) < 2:
       ```
     * The if statement doesn't even check if there are too many arguments. In fact, the statement returns True if there are not too many arguments.
     * An easy fix for this would be to rewrite the comment, or not have it at all.