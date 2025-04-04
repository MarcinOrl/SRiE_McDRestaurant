import tkinter as tk


class SummaryPanel(tk.Frame):
    def __init__(self, parent, cart):
        super().__init__(parent)
        self.cart = cart
        self.label = tk.Label(self, text="Podsumowanie:\nCena całkowita: 0.00 zł")
        self.label.pack()

        self.checkout_btn = tk.Button(
            self, text="Checkout", command=self.update_summary
        )
        self.checkout_btn.pack()

    def update_summary(self):
        total = self.cart.total_price()
        self.label.config(text=f"Podsumowanie:\nCena całkowita: {total:.2f} zł")
