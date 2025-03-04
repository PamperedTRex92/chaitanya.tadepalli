# CNC Design App

CNC Design App is a Python application that allows users to create a simple design by clicking points on a canvas. The application generates CNC G-code and M-code from the design, which can be directly fed to a CNC machine.

## Features

- **Simple GUI**: Easy-to-use graphical user interface using `customtkinter`.
- **Design Area**: Click to add points and create a design.
- **G-code Generation**: Generates CNC G-code and M-code from the design.
- **Output Notification**: Notifies the user when the G-code has been successfully generated and saved.

## Requirements

- Python 3.x
- `customtkinter` library
- `tkinter` library (usually included with Python)

## Installation

1. Make sure you have Python 3 installed. You can download it from [python.org](https://www.python.org/).
2. Install the `customtkinter` library if you haven't already:

   ```bash
   pip install customtkinter
   
## Usage
1. Clone this repository or download the source code.
2. Run the cnc_design_app.py file:

python cnc_design_app.py

3. The application window will open. Click on the canvas to add points and create your design.

4. Click the "Generate G-code" button to generate and save the CNC G-code and M-code to the output.nc file in your home directory. A message box will notify you when the G-code has been successfully generated.

## Code Overview

CNCDesignApp: The main application class.
__init__(self, root): Initializes the application, sets up the canvas, and binds the mouse click event.

add_point(self, event): Adds a point to the design when the canvas is clicked.

generate_gcode(self): Generates the CNC G-code and M-code from the design and saves it to the output.nc file.

## Acknowledgments

Thanks to the developers of customtkinter for providing the library used in this project.
