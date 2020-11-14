import tkinter as tk
from tkinter import font
import multilineentry as me


if __name__ == '__main__':
    root = tk.Tk()
    root.minsize(width=200, height=100)
    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=0)

    MAX_LINES = 4
    custom_font = font.Font(family="Courier", size=12)

    st = me.MultilineEntry(root,
                           MAX_LINES,
                           font=custom_font,
                           relief=tk.FLAT,
                           wrap='word',
                           highlightbackground="light grey",
                           highlightthickness=2,
                           height=1)

    st.grid(column=0, row=0, sticky=tk.EW)

    root.bind('<Configure>', st.on_configure)
    root.mainloop()
