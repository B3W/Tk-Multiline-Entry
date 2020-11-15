import tkinter as tk
from tkinter import ttk
from tkinter import font
import entryframe as ef


if __name__ == '__main__':
    root = tk.Tk()
    root.geometry('200x100')
    root.minsize(width=100, height=100)
    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=0, pad=10)
    root.configure(bg='green')

    MAX_LINES = 4
    custom_font = font.Font(family="Times New Roman", size=12)

    style = ttk.Style()

    style.configure('test.TFrame', background='red')

    frame = ef.EntryFrame(root, MAX_LINES, style='test.TFrame')
    frame.entry.configure(font=custom_font)
    frame.grid(column=0, row=0, sticky=tk.EW)

    root.mainloop()
