import tkinter as tk


class SelectedList(tk.Frame):
    def __init__(self, parent, cart):
        super().__init__(parent)
        self.cart = cart

        self.label = tk.Label(self, text="Wybrane produkty:")
        self.label.pack()

        self.listbox = tk.Listbox(self)
        self.listbox.pack(fill=tk.BOTH, expand=True)
        self.listbox.bind("<Double-Button-1>", self.on_double_click)

        remove_btn = tk.Button(
            self, text="Usuń z koszyka", command=self.remove_selected
        )
        remove_btn.pack()

    def update_list(self):
        self.listbox.delete(0, tk.END)
        for product in self.cart.selected_products:
            self.listbox.insert(tk.END, str(product))

    def remove_selected(self):
        selection = self.listbox.curselection()
        if selection:
            index = selection[0]
            del self.cart.selected_products[index]
            self.update_list()

    def on_double_click(self, event):
        self.remove_selected()
