# 🔐 Python Password Generator (Tkinter GUI)

A simple, stylish **desktop password generator** built with Python and Tkinter.  
It lets you generate strong random passwords with a clean dark UI and copy them with one click.

---

## ✨ Features

- 🎨 Modern dark-themed GUI using `ttk` styles  
- 📏 Selectable password length (8–32 characters)  
- 🔁 Generate **single** or **multiple** passwords
- 📋 One-click **copy to clipboard** button  
- 🧾 Scrollable text area to display 5 or 10 generated passwords  
- ✅ Simple status messages (e.g., “Copied to clipboard ✔”)

---

## 🧱 Technologies Used

- **Python 3.x**
- **Tkinter** (built-in GUI library)
- `ttk` for themed widgets
- `random` and `string` modules for password generation

---

## 📁 File Structure

You only need one main Python file, for example:

```text
.
├── password_generator.py   
└── README.md               


## How It Works 
The GUI is built using Tkinter and ttk widgets.

You select a password length using a Combobox.

When you click Generate, it:

Uses letters (a-z, A-Z), digits (0–9), and symbols (!@#$%^&*)

Builds a random password of the selected length

Displays it in a read-only text field

Copy button:

Copies the generated password into your system clipboard

Shows a small status message under the field

Multiple Passwords:

Buttons to quickly generate 5 or 10 passwords

They are displayed in a scrollable


Common Issues & Fixes
1. No window appears

Make sure you’re not using an online IDE (many don’t support GUIs).

Run the script locally on your PC using a normal terminal or an editor like:

VS Code

IDLE (comes with Python)

PyCharm

ModuleNotFoundError: No module named 'tkinter'

On Linux, install Tkinter:

sudo apt install python3-tk


On Windows/macOS:

Reinstall Python from python.org making sure to install the standard library.

3. Script runs but crashes immediately

Open a terminal and run the script from there to see the error message.

Check that your file is not named tkinter.py, random.py, or string.py.


Future Ideas

If you want to upgrade this project later, here are some ideas:

Add checkboxes for:

Include / exclude symbols

Include / exclude numbers

Include / exclude uppercase letters

Add a strength meter (Weak / Medium / Strong)

Option to save generated passwords to a file

Add a light/dark mode toggle

