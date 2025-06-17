import tkinter as tk
def ajouter_a_litbox():
    if mytext.get() == "":
        mytext.delete(0,tk.END)
        mytext.insert(tk.END,"Veuillez entrer une tache")
    else:
        litbox.insert(tk.END,mytext.get())
        mytext.delete(0,tk.END)

def supprimer_from_litbox():
    index = litbox.curselection()
    if index == None:
        mytext.insert(tk.END,"Sélectionne une tâche à supprimer.")
    else:
        try:
            litbox.delete(index)
            mytext.insert(0,"La tâche a été supprimée.")
        except Exception as e:
            mytext.insert(0,e)

root = tk.Tk()
root.title("To-Do List")
root.geometry("700x300")
root.configure(bg="#ffe4f2")  

mytext = tk.Entry(root, width=50)
mytext.pack(pady=6)


button_ajouter= tk.Button(root ,text="ajouter",pady=3,fg="#fcfbfa"
                    ,bg="#f0823e",font="Helvatica 10 bold"
                    ,command= ajouter_a_litbox)
button_ajouter.pack()

litbox =tk.Listbox(root,width=20)
litbox.pack(pady=4)

button_suprimer= tk.Button(root ,text="supprimer",pady=3
            ,fg="#fcfbfa",bg="#92e8f0",font="Helvatica 10 bold"
            ,command=supprimer_from_litbox)
button_suprimer.pack()

root.mainloop()