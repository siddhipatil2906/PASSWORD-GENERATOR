from tkinter import *
import random
import string

def generate():
    length = int(entry.get())

    chars = ""

    if var1.get() == 1:
        chars += string.ascii_letters

    if var2.get() == 1:
        chars += string.digits

    if var3.get() == 1:
        chars += "!@#$%&*?"

    password = "".join(random.choice(chars) for i in range(length))

    output.config(text=password)

    # Strength Meter
    if length <= 6:
        strength.config(text="Weak", fg="red")
    elif length <= 10:
        strength.config(text="Medium", fg="orange")
    else:
        strength.config(text="Strong", fg="green")

def copy():
    root.clipboard_clear()
    root.clipboard_append(output.cget("text"))

root = Tk()
root.title("Premium Password Generator")
root.geometry("450x500")
root.config(bg="#121212")

Label(root, text="🔐 Premium Password Generator",
font=("Arial",18,"bold"),
bg="#121212", fg="white").pack(pady=15)

Label(root, text="Enter Password Length",
font=("Arial",12),
bg="#121212", fg="white").pack()

entry = Entry(root, font=("Arial",14), justify="center")
entry.pack(pady=10)

# Checkboxes
var1 = IntVar(value=1)
var2 = IntVar(value=1)
var3 = IntVar(value=1)

Checkbutton(root, text="Letters (A-z)",
variable=var1,
bg="#121212", fg="white",
selectcolor="#121212").pack()

Checkbutton(root, text="Numbers (0-9)",
variable=var2,
bg="#121212", fg="white",
selectcolor="#121212").pack()

Checkbutton(root, text="Symbols (!@#$)",
variable=var3,
bg="#121212", fg="white",
selectcolor="#121212").pack()

Button(root, text="Generate Password",
font=("Arial",12,"bold"),
bg="#25D366", fg="white",
command=generate).pack(pady=15)

output = Label(root, text="",
font=("Courier",16,"bold"),
bg="#121212", fg="yellow")
output.pack(pady=15)

strength = Label(root, text="",
font=("Arial",14,"bold"),
bg="#121212")
strength.pack()

Button(root, text="Copy Password",
font=("Arial",12),
bg="#075E54", fg="white",
command=copy).pack(pady=15)

root.mainloop()
