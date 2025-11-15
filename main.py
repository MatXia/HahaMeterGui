import darkdetect, sv_ttk
from tkinter import *
from tkinter import ttk, messagebox
from hahameter import get_score

root = Tk()
root.title("HahaMeterGUI")
root.geometry("400x200")
root.resizable(False, False)
root.iconbitmap(bitmap="smile.ico")

def processing(event):
    score = round(get_score(smeh_var.get()) * 100)
    result_text.configure(text=f"{score}%")

smeh_var = StringVar()

smeh_text = ttk.Label(root, text="Введите смех друга:", font=({"", 15}))
result_text = ttk.Label(root, text="", font=({"", 15}))
smeh = ttk.Entry(root, textvariable=smeh_var)
processing_btn = ttk.Button(root, text="Обработать")
about_btn = ttk.Button(root, text="О программе")

smeh_text.pack(anchor=CENTER, pady=5)
smeh.pack(anchor=CENTER, pady=5)
processing_btn.pack(anchor=CENTER, pady=5)
result_text.pack(anchor=CENTER, pady=5)
about_btn.pack(anchor=S, pady=10)

processing_btn.bind('<Button-1>', processing)
about_btn.bind('<Button-1>', lambda event: messagebox.showinfo("О программе", "Разработал MatXia зачем-то."))
smeh.bind('<Return>', processing)

sv_ttk.set_theme(darkdetect.theme())

root.mainloop()