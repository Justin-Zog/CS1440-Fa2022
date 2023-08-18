import tkinter as tk
from sys import stderr
from time import time


class ImagePainter:

    def __init__(self, fractal, palette, fractal_info):
        self.fractal = fractal
        self.palette = palette
        self.fractal_info = fractal_info

    def create_image(self):
        print(f"Rendering {self.fractal_info['imagename']} fractal", file=stderr)
        image_size = self.fractal_info['pixels']
        start_time = time()

        window = tk.Tk()
        photo_image = tk.PhotoImage(width=image_size, height=image_size)
        canvas = tk.Canvas(window, width=image_size, height=image_size)
        canvas.pack()

        canvas.create_image((image_size / 2, image_size / 2), image=photo_image, state="normal")

        for row in range(image_size + 1):
            pixel_row = []
            for column in range(image_size + 1):
                x = self.fractal_info['min']['x'] + column * self.fractal_info['pixelsize']
                y = self.fractal_info['min']['y'] + row * self.fractal_info['pixelsize']
                iteration = self.fractal.count(complex(x, y))
                pixel_row.append(self.palette.getColor(iteration))

            photo_image.put('{' + ' '.join(pixel_row) + '}', to=(0, image_size - row))
            window.update()

            # Makes the Status Bar
            percent_drawn = row / image_size
            print(f"[{percent_drawn:>4.0%} + {'=' * int(34 * percent_drawn):<33}]", end='\r', file=stderr)

        print(f"\nDone in {time() - start_time:.3f} seconds!", file=stderr)
        photo_image.write(f"{self.fractal_info['imagename']}.png")
        print("Wrote picture " + self.fractal_info['imagename'] + ".png", file=stderr)

        print("Close the image window to exit the program", file=stderr)

        tk.mainloop()
