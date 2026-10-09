import tkinter as tk

def ajouter_caractere(caractere):
    entry.insert(tk.END, caractere)

def calculer():
    try:
        expression = entry.get()
        result = eval(expression)
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except :
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

def effacer():
    entry.delete(0, tk.END)

root = tk.Tk()
root.title("Calculatrice")
root.geometry("300x400")
entry = tk.Entry(root, width=16, font=("Arial", 24), borderwidth=2, relief="ridge", justify="left")
entry.grid(row=0, column=0, columnspan=4, padx=13, pady=13)
buttons = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
    ("0", 4, 0), (".", 4, 1), ("=", 4, 2), ("+", 4, 3)
]
for (text, row, col) in buttons:
    if text == "=":
        button = tk.Button(root, text=text, font=("Arial", 18), command=calculer)
        button.grid(row=row, column=col, padx=5, pady=5, sticky="nsew")
    else:
        button = tk.Button(root, text=text, font=("Arial", 18), command=lambda t=text: ajouter_caractere(t))
        button.grid(row=row, column=col, padx=5, pady=5, sticky="nsew")

button_effacer = tk.Button(root, text="C", font=("Arial", 18), command=effacer)
button_effacer.grid(row=5, column=0, columnspan=4, padx=5, pady=5, sticky="nsew")
for row in range(6):
    root.grid_rowconfigure(row, weight=1)
for col in range(4):
    root.grid_columnconfigure(col, weight=1)
root.mainloop()
