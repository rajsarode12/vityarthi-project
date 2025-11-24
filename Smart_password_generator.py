import tkinter as tk
from tkinter import ttk
import random
import string

class SimpleStylishPasswordGenerator:
    def __init__(self, root):
        self.root = root
        self.root.title("🔐 Password Generator")
        self.root.geometry("500x400")
        self.root.minsize(450, 350)

        self.setup_styles()
        self.create_widgets()

    def setup_styles(self):
        style = ttk.Style()
        # Use a safe theme
        try:
            style.theme_use("clam")
        except tk.TclError:
            style.theme_use(style.theme_names()[0])

        self.root.configure(bg="#0f172a")  # dark blue background

        style.configure("TFrame", background="#0f172a")
        style.configure("Card.TFrame", background="#111827")
        style.configure("Title.TLabel",
                        background="#0f172a",
                        foreground="#e5e7eb",
                        font=("Segoe UI", 16, "bold"))
        style.configure("TLabel",
                        background="#111827",
                        foreground="#e5e7eb",
                        font=("Segoe UI", 10))
        style.configure("Sub.TLabel",
                        background="#111827",
                        foreground="#9ca3af",
                        font=("Segoe UI", 9))

        style.configure("Accent.TButton",
                        font=("Segoe UI", 10, "bold"),
                        padding=(10, 5))
        style.map("Accent.TButton",
                  background=[("!disabled", "#2563eb"), ("active", "#1d4ed8")],
                  foreground=[("!disabled", "#f9fafb")])

        style.configure("Ghost.TButton",
                        font=("Segoe UI", 9),
                        padding=(8, 4))
        style.map("Ghost.TButton",
                  background=[("!disabled", "#111827"), ("active", "#1f2937")],
                  foreground=[("!disabled", "#e5e7eb")])

    def create_widgets(self):
        outer = ttk.Frame(self.root, padding=15)
        outer.pack(fill=tk.BOTH, expand=True)

        card = ttk.Frame(outer, style="Card.TFrame", padding=15)
        card.pack(fill=tk.BOTH, expand=True)

        # Title
        title = ttk.Label(card, text="🔐 Password Generator", style="Title.TLabel")
        title.pack(anchor="w", pady=(0, 5))

        subtitle = ttk.Label(card,
                             text="Generate secure random passwords instantly.",
                             style="Sub.TLabel")
        subtitle.pack(anchor="w", pady=(0, 10))

        ttk.Separator(card).pack(fill=tk.X, pady=8)

        # Length row
        length_frame = ttk.Frame(card, style="Card.TFrame")
        length_frame.pack(fill=tk.X, pady=8)

        ttk.Label(length_frame, text="Password length:").pack(side=tk.LEFT)

        self.length_var = tk.IntVar(value=12)
        length_combo = ttk.Combobox(
            length_frame,
            textvariable=self.length_var,
            values=[8, 10, 12, 14, 16, 20, 24, 32],
            width=5,
            state="readonly"
        )
        length_combo.pack(side=tk.LEFT, padx=10)

        # Generate + copy buttons
        btn_frame = ttk.Frame(card, style="Card.TFrame")
        btn_frame.pack(fill=tk.X, pady=8)

        generate_btn = ttk.Button(
            btn_frame,
            text="Generate",
            style="Accent.TButton",
            command=self.generate_password
        )
        generate_btn.pack(side=tk.LEFT)

        copy_btn = ttk.Button(
            btn_frame,
            text="Copy",
            style="Ghost.TButton",
            command=self.copy_password
        )
        copy_btn.pack(side=tk.LEFT, padx=8)

        # Password display
        display_frame = ttk.Frame(card, style="Card.TFrame")
        display_frame.pack(fill=tk.X, pady=8)

        ttk.Label(display_frame, text="Password:").pack(anchor="w")

        self.password_var = tk.StringVar()
        self.password_entry = ttk.Entry(
            display_frame,
            textvariable=self.password_var,
            font=("Consolas", 13),
            state="readonly"
        )
        self.password_entry.pack(fill=tk.X, pady=(3, 0))

        self.status_var = tk.StringVar(value="")
        status_label = ttk.Label(display_frame, textvariable=self.status_var, style="Sub.TLabel")
        status_label.pack(anchor="w", pady=(3, 0))

        ttk.Separator(card).pack(fill=tk.X, pady=10)

        # Multiple passwords section
        multi_top = ttk.Frame(card, style="Card.TFrame")
        multi_top.pack(fill=tk.X)

        ttk.Label(multi_top, text="Generate multiple passwords:").pack(side=tk.LEFT)

        ttk.Button(
            multi_top,
            text="5",
            style="Ghost.TButton",
            command=lambda: self.generate_multiple(5)
        ).pack(side=tk.RIGHT)

        ttk.Button(
            multi_top,
            text="10",
            style="Ghost.TButton",
            command=lambda: self.generate_multiple(10)
        ).pack(side=tk.RIGHT, padx=5)

        # Text box
        self.results_text = tk.Text(
            card,
            height=7,
            font=("Consolas", 10),
            bg="#020617",
            fg="#e5e7eb",
            bd=0,
            relief="flat",
            insertbackground="#f9fafb"
        )
        self.results_text.pack(fill=tk.BOTH, expand=True, pady=(8, 0))

    def generate_password(self, length=None):
        if length is None:
            length = self.length_var.get()

        chars = string.ascii_letters + string.digits + "!@#$%^&*"
        password = "".join(random.choice(chars) for _ in range(length))
        self.password_var.set(password)
        self.status_var.set("")
        return password

    def generate_multiple(self, count):
        self.results_text.delete("1.0", tk.END)
        for i in range(count):
            pwd = self.generate_password()
            self.results_text.insert(tk.END, f"{i+1:2d}. {pwd}\n")

    def copy_password(self):
        pwd = self.password_var.get()
        if not pwd:
            self.status_var.set("Generate a password first.")
            return
        self.root.clipboard_clear()
        self.root.clipboard_append(pwd)
        self.status_var.set("Copied to clipboard ✔")
        self.root.after(2500, lambda: self.status_var.set(""))

if __name__ == "__main__":
    print("Starting GUI...")  
    root = tk.Tk()
    app = SimpleStylishPasswordGenerator(root)
    root.mainloop()
