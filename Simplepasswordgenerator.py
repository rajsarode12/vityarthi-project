import tkinter as tk
from tkinter import ttk
import random
import string

class SimplePasswordGenerator:
    def __init__(self, root):
        self.root = root
        self.root.title("🔐 Password Generator")
        self.root.geometry("500x400")
        self.create_widgets()
    
    def create_widgets(self):
        # Main container
        main_frame = ttk.Frame(self.root, padding="20")
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Title
        title_label = ttk.Label(main_frame, text="🔐 Password Generator", 
                               font=("Arial", 16, "bold"))
        title_label.pack(pady=10)
        
        # Length selection
        length_frame = ttk.Frame(main_frame)
        length_frame.pack(fill=tk.X, pady=10)
        
        ttk.Label(length_frame, text="Password Length:").pack(side=tk.LEFT)
        self.length_var = tk.IntVar(value=12)
        length_combo = ttk.Combobox(length_frame, textvariable=self.length_var, 
                                   values=[8, 10, 12, 14, 16, 20], width=10)
        length_combo.pack(side=tk.LEFT, padx=10)
        
        # Generate button
        ttk.Button(main_frame, text="Generate Password", 
                  command=self.generate_password).pack(pady=10)
        
        # Password display
        self.password_var = tk.StringVar()
        password_entry = ttk.Entry(main_frame, textvariable=self.password_var, 
                                 font=("Courier", 14), width=30, state="readonly")
        password_entry.pack(pady=10)
        
        
        # Generate multiple
        multi_frame = ttk.Frame(main_frame)
        multi_frame.pack(fill=tk.X, pady=20)
        
        ttk.Label(multi_frame, text="Generate Multiple:").pack()
        ttk.Button(multi_frame, text="5 Passwords", 
                  command=lambda: self.generate_multiple(5)).pack(pady=5)
        ttk.Button(multi_frame, text="10 Passwords", 
                  command=lambda: self.generate_multiple(10)).pack(pady=5)
        
        # Results area
        self.results_text = tk.Text(main_frame, height=8, width=50, font=("Courier", 10))
        self.results_text.pack(fill=tk.BOTH, expand=True)
    
    def generate_password(self, length=None):
        if length is None:
            length = self.length_var.get()
        
        characters = string.ascii_letters + string.digits + "!@#$%^&*"
        password = ''.join(random.choice(characters) for _ in range(length))
        
        self.password_var.set(password)
        return password
    
    def generate_multiple(self, count):
        self.results_text.delete(1.0, tk.END)
        
        for i in range(count):
            password = self.generate_password()
            self.results_text.insert(tk.END, f"{i+1:2d}. {password}\n")

if __name__ == "__main__":
    root = tk.Tk()
    app = SimplePasswordGenerator(root)
    root.mainloop()