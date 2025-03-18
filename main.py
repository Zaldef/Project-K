import tkinter as tk
from tkinter import messagebox

class app:
    def __init__(self, root):
        self.root = root
        self.root.title("Project-K")
        self.root.geometry("1336x768")


if __name__ == "__main__":
    root = tk.Tk()
    app = app(root)
    root.mainloop()