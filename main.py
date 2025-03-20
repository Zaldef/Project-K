import tkinter as tk
from src.controllers.home_controller import HomeController

class app:
    def __init__(self, root):
        self.root = root
        self.root.title("Project-K")
        self.root.geometry("1336x768")


if __name__ == "__main__":
    root = tk.Tk()
    app = HomeController(root)
    root.mainloop()