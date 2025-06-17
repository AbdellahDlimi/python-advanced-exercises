import tkinter as tk 

root = tk.Tk()
root.title("Hello Python")
root.geometry("700x300")

mylabel = tk.Label(root,text= "hello world",fg="#750404"
                   ,bg="#F0F0F0",font="Helvatica 20 bold",pady=30)
mylabel.pack()

mytext = tk.Entry(root,width=50)
mytext.insert(0,"clique sur un bouton")
mytext.pack(pady=6)

mylist = ["Python", "Java", "C++", "JavaScript", "Swift"]
def updat_entry(text):
    
    mytext.delete(0, tk.END)  
    mytext.insert(0, text) 

for lang in mylist:
    buttun = tk.Button(root,text=lang,fg="#349eeb",bg="#8c4e18"
        ,font="Helvatica 10 bold",width=10,height=1,pady=3
        ,command=lambda x =lang : updat_entry(x))
    buttun.pack()
    
root.mainloop()


