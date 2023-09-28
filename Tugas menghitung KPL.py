import tkinter as tk
from tkinter import ttk
import math

class Window(tk.Tk):
    def __init__(self):
        super(Window, self).__init__()
        
        self.title("Menghitung KPL - TextBox")
        self.minsize(480, 320)
        
        tk.Grid.rowconfigure(self, 0, weight=1)
        tk.Grid.rowconfigure(self, 1, weight=1)
        tk.Grid.rowconfigure(self, 2, weight=1)
        tk.Grid.rowconfigure(self, 3, weight=1)
        tk.Grid.rowconfigure(self, 4, weight=1)
        tk.Grid.rowconfigure(self, 5, weight=999)
        
        tk.Grid.columnconfigure(self, 0, weight=1)
        tk.Grid.columnconfigure(self, 1, weight=1)
        tk.Grid.columnconfigure(self, 2, weight=1)
        tk.Grid.columnconfigure(self, 3, weight=1)
        tk.Grid.columnconfigure(self, 4, weight=1)
        tk.Grid.columnconfigure(self, 5, weight=999)
                
        self.text_entry()
    
    def hasil(self):
        
        kpl_sebelumnya = float(self.kpl_sebelumnya_entry.get())
        jarak_sebelumnya = float(self.jarak_sebelumnya_entry.get())
        kpl_sekarang = float(self.kpl_sekarang_entry.get())
        jarak_sekarang = float(self.jarak_sekarang_entry.get())
        
        liter_sebelumnya = jarak_sebelumnya / kpl_sebelumnya
        liter_sekarang = jarak_sekarang / kpl_sekarang
        liter = liter_sebelumnya + liter_sekarang
        jarak_terakhir = jarak_sekarang - jarak_sebelumnya
        kpl_terakhir = jarak_terakhir / liter
        
        self.kpl_terakhir_label.configure(text="{:.2f}".format(kpl_terakhir))
        
    def text_entry(self):
        kpl_sebelumnya_label = ttk.Label(self, text="Kpl Sebelumnya:")
        kpl_sebelumnya_label.grid(column=0, row=0, padx=7, pady=7)
    
        kpl_sekarang_label = ttk.Label(self, text="Kpl Sekarang:")
        kpl_sekarang_label.grid(column=0, row=1, padx=7, pady=7)
        
        jarak_sebelumnya_label = ttk.Label(self, text="Jarak Sebelumnya:")
        jarak_sebelumnya_label.grid(column=2, row=0, padx=7, pady=7)
        
        jarak_sekarang_label = ttk.Label(self, text="Jarak Sekarang:")
        jarak_sekarang_label.grid(column=2, row=1, padx=7, pady=7)

        self.kpl_sebelumnya_entry = ttk.Entry(self)
        self.kpl_sebelumnya_entry.grid(column=1, row=0, padx=7, pady=7)
        
        self.kpl_sekarang_entry = ttk.Entry(self)
        self.kpl_sekarang_entry.grid(column=1, row=1, padx=7, pady=7)
        
        self.jarak_sebelumnya_entry = ttk.Entry(self)
        self.jarak_sebelumnya_entry.grid(column=3, row=0, padx=7, pady=7)
        
        self.jarak_sekarang_entry = ttk.Entry(self)
        self.jarak_sekarang_entry.grid(column=3, row=1, padx=7, pady=7)
        
        hitung_button = ttk.Button(self, text="Hitung KPL", command=self.hasil)
        hitung_button.grid(column=1, row=3, padx=7, pady=7, columnspan=2, sticky=tk.EW)
        
        kpl_terakhir_label = ttk.Label(self, text="Kpl Terakhir:")
        kpl_terakhir_label.grid(column=2, row=4, padx=7, pady=7, sticky=tk.W)
        
        self.kpl_terakhir_label = ttk.Label(self, text="")
        self.kpl_terakhir_label.grid(column=3, row=4, padx=7, pady=7)
        

window = Window()
window.mainloop()