import tkinter as tk
from tkinter import ttk


class ProductList(ttk.Frame):
    def __init__(self, parent, products, cart):
        super().__init__(parent)
        self.cart = cart
        self.products = products
        self.selected_list = None

        self.label = tk.Label(self, text="Lista produktów:")
        self.label.pack()

        self.listbox = tk.Listbox(self)
        for p in products:
            self.listbox.insert(tk.END, str(p))
        self.listbox.pack(fill=tk.BOTH, expand=True)
        self.listbox.bind("<Double-Button-1>", self.on_double_click)

        btn = tk.Button(self, text="Dodaj do koszyka", command=self.add_selected)
        btn.pack()

    def set_selected_list(self, selected_list):
        self.selected_list = selected_list

    def add_selected(self):
        selection = self.listbox.curselection()
        if selection:
            index = selection[0]
            self.cart.add_product(self.products[index])
            if self.selected_list:
                self.selected_list.update_list()

    def on_double_click(self, event):
        self.add_selected()
