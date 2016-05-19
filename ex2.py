"""
    Example 2
    Box drawing application

"""

import tkinter as tk
import random

class Box(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

        # Set the height and width offsets
        self.height_offset = 20
        self.height = self.y + self.height_offset
        self.width_offset = 20
        self.width = self.x + self.width_offset

    def get_coords(self):
        # Return the coords of the box
        return (self.x, self.y, self.width, self.height)

    def set_coords(self, x, y):
        """Sets the coords of the box"""
        self.x = x
        self.y = y
        self.width = self.x + self.width_offset
        self.height = self.y + self.height_offset

    def set_box_size(self, size):
        """Sets the size of the box"""
        self.height_offset = size
        self.height = self.y + self.height_offset
        self.width_offset = size
        self.width = self.x + self.width_offset

class TodoApp(object):
    """A todo list app"""

    def __init__(self, master):
        self.master = master
        self.master.title("Box drawer app")

        self.topFrame = tk.Frame(master)

        # Create the canvas
        self.canvas = tk.Canvas(self.topFrame)
        self.canvas.pack(expand=True, fill=tk.BOTH)

        # Create the box model
        self.box = Box(40, 60)

        # Create the box to draww onto the canvas
        self.canvas_box = self.canvas.create_rectangle(self.box.x, self.box.y, 100, 100, fill="blue")

        self.topFrame.pack(side=tk.TOP, expand=True, fill=tk.BOTH)


        # Bind events to the canvas
        self.canvas.bind('<Motion>', self.move_box)
        self.canvas.bind('<Button-1>', self.box_click)

    def move_box(self, event):
        """Moves the box"""

        # Get the canvas coords
        x = event.x - self.box.width_offset * 0.5
        y = event.y - self.box.height_offset * 0.5
        self.box.set_coords(x, y)
        
        self.canvas.coords(self.canvas_box, self.box.get_coords())

    def box_click(self, event):
        """Sets the size of the box on click"""
        size = random.randint(10, 40)

        # Set the box size
        self.box.set_box_size(size)

        # Redraw the box
        self.canvas.coords(self.canvas_box, self.box.get_coords())
        


root = tk.Tk()
app = TodoApp(root)
root.mainloop()
