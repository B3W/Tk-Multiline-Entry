import autoscrollbar as asb
import multilineentry as me
import tkinter as tk
from tkinter import ttk


class EntryFrame(ttk.Frame):
    '''UI element containing widgets for message compilation.'''
    def __init__(self, master, max_lines, *args, **kwargs):
        '''Override of ttk.Frame's initialization function'''
        # Initialize root frame
        ttk.Frame.__init__(self, master, *args, **kwargs)

        self.columnconfigure(0, weight=1)  # Entry widget
        self.columnconfigure(1, weight=0)  # AutoScrollbar
        self.rowconfigure(0, weight=1)

        self.MAX_LINES = max_lines  # Max number of lines entry will resize to

        # Initialize multiline entry widget
        self.entry = me.MultilineEntry(self,
                                       self.MAX_LINES,
                                       relief=tk.FLAT,
                                       wrap='word',
                                       highlightbackground="light grey",
                                       highlightthickness=2,
                                       height=1)
        self.entry.grid(column=0, row=0, sticky=tk.EW)

        # Initialize scrollbar
        self.vsb = asb.AutoScrollbar(self, 1, 0, orient=tk.VERTICAL)
        self.entry.configure(yscrollcommand=self.vsb.set)

        self.bind('<Configure>', self.entry.on_configure)
