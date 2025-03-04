import customtkinter as ctk
import tkinter as tk
from tkinter import messagebox
import os

class CNCDesignApp:
    def __init__(self, root):
        self.root = root
        self.root.title("CNC Design App")
        self.canvas = ctk.CTkCanvas(root, width=500, height=500, bg="white")
        self.canvas.pack()
        self.points = []
        self.canvas.bind("<Button-1>", self.add_point)
        self.output_path = os.path.join(os.path.expanduser("~"), "output.nc")

    def add_point(self, event):
        x, y = event.x, event.y
        self.points.append((x, y))
        self.canvas.create_oval(x-2, y-2, x+2, y+2, fill="blue")
        if len(self.points) > 1:
            self.canvas.create_line(self.points[-2], self.points[-1], fill="blue")

    def generate_gcode(self):
        gcode = "G21 ; Set units to mm\nG90 ; Absolute positioning\n"
        for point in self.points:
            gcode += f"G01 X{point[0]} Y{point[1]} ; Move to point\n"
        gcode += "M02 ; End of program\n"
        with open(self.output_path, "w") as file:
            file.write(gcode)
        messagebox.showinfo("G-code Generated", f"G-code has been successfully generated and saved to {self.output_path}")

if __name__ == "__main__":
    root = ctk.CTk()
    app = CNCDesignApp(root)
    ctk.CTkButton(root, text="Generate G-code", command=app.generate_gcode).pack()
    root.mainloop()
