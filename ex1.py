"""
    Example 1
    Todo list application

"""

import tkinter as tk

class TodoApp(object):
    """A todo list app"""

    def __init__(self, master):
        self.master = master
        self.master.title("Todo list app")

        self.items = []

        # Top frame
        self.topFrame = tk.Frame(master)

        self.toplab = tk.Label(self.topFrame, text="TodoList")
        self.toplab.pack(side=tk.TOP, fill=tk.X)

        self.listbox = tk.Listbox(self.topFrame)
        self.listbox.pack(side=tk.BOTTOM, expand=True, fill=tk.BOTH)

        self.topFrame.pack(side=tk.TOP, expand=True, fill=tk.BOTH)

    
        # Bottom frame
        self.bottomFrame = tk.Frame(master)

        self.todoText = tk.Entry(self.bottomFrame)
        self.todoText.pack(side=tk.LEFT, fill=tk.X, expand=True)

        self.addButton = tk.Button(self.bottomFrame, text="ADD", command=self.addItem)
        self.addButton.pack(side=tk.RIGHT)

        self.bottomFrame.pack(side=tk.BOTTOM, fill=tk.X)


    def addItem(self):
        todo = self.todoText.get()
        self.listbox.insert(tk.END, todo)
        self.todoText.delete(0, "end")


root = tk.Tk()
app = TodoApp(root)
root.mainloop()
