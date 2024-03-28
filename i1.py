from tkinter import *
from tkinter import messagebox

def entertask():
    task = entry.get()
    if task:
        listbox.insert(END, task)
        entry.delete(0, END)
    else:
        messagebox.showerror("Error", "Enter a task according to u are requirment!")

def deletetask():
    try:
        selected_task = listbox.curselection()[0]
        listbox.delete(selected_task)
    except IndexError:
        messagebox.showerror("Error", " Task selected!")
ws = Tk()
ws.geometry("400x400")
ws.title("To-Do List App")
ws.config(bg='purple')

frame = Frame(ws)
frame.pack(pady=15)
listbox = Listbox(frame, width=35, height=10)
listbox.pack(side=LEFT)
scrollbar = Scrollbar(frame, orient=VERTICAL)
scrollbar.pack(side=RIGHT, fill=Y)

listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)

entry = Entry(ws, font=("Helvetica", 16))
entry.pack(pady=20)

add_btn = Button(ws, text="Add The Task", command=entertask)
add_btn.pack()

delete_btn = Button(ws, text="Delete The Task", command=deletetask)
delete_btn.pack()

ws.mainloop()
