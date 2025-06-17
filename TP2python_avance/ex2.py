from tkinter import *
def Celsius_Fahrenheit(nbr):
    F = nbr * 9/5 + 32
    return F
def Fahrenheit_Celsius(nbr):
    C = (nbr - 32) * 5/9
    return C
def convert():
    try:
        valeur = mytext.get().strip()
        if valeur == "":
            text.delete(0, END)
            text.insert(0, "Champ vide")
            return
        if choix.get() == 1:
            text.delete(0, END)
            text.insert(0, Celsius_Fahrenheit(float(valeur)))
        elif choix.get() == 2:
            text.delete(0, END)
            text.insert(0, Fahrenheit_Celsius(float(valeur)))
        else:
            text.delete(0, END)
            text.insert(0, "Choisis une option")
    except ValueError:
        text.delete(0, END)
        text.insert(0, "Entrée invalide")

root = Tk()
root.title("Convertisseur de température")
root.geometry("700x300")

label1 = Label(root, text="Enter votre nombre: ")
label1.pack()
choix = IntVar()

mytext = Entry(root, width=50)
mytext.pack()

butt1 = Radiobutton(root, text="Celsius vers Fahrenheit", variable=choix, value=1)
butt1.pack()

butt2 = Radiobutton(root, text="Fahrenheit vers Celsius", variable=choix, value=2)
butt2.pack()

button = Button(root, text="Convertir", command=convert,padx=1
                ,pady=6,fg="white",bg="#8c4e18",font="Helvatica 10 bold")
button.pack()

text = Entry(root, width=13,fg="white",bg="black",font="Helvatica 20 bold")
text.pack(pady=10)

root.mainloop()
