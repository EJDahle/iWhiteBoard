import tkinter as tk


class Window:

    def __init__(self, root, width, height) -> None:
        self.width = width
        self.height = height
        self.transparent = False
        root.geometry(f"{self.width}x{self.height}")

    def menu_bar(self, root) -> None:
        self.my_menu = tk.Menu(root)
        self.file_menu = tk.Menu(self.my_menu, tearoff = 0)
        self.edit_menu = tk.Menu(self.my_menu, tearoff = 0)
        self.view_menu = tk.Menu(self.my_menu, tearoff = 0)
        self.about_menu = tk.Menu(self.my_menu, tearoff = 0)
        self.my_menu.add_cascade(label = "Fil", menu = self.file_menu)
        self.my_menu.add_cascade(label = "Rediger", menu = self.edit_menu)
        self.my_menu.add_cascade(label = "Vis", menu = self.view_menu)
        self.my_menu.add_cascade(label = "Om", menu = self.about_menu)
        self.file_menu.add_command(label="Text", compound = "left")
        root.config(menu = self.my_menu)

if __name__ == "__main__":
    root = tk.Tk()
    win = Window(root, 500, 500)
    win.menu_bar(root)
    root.mainloop()