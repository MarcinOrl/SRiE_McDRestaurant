import tkinter as tk


class SummaryPanel(tk.Frame):
    def __init__(self, parent, cart):
        super().__init__(parent)
        self.cart = cart

        self.text = tk.Text(self, height=10, width=50)
        self.text.pack()

        self.checkout_btn = tk.Button(
            self, text="Checkout", command=self.update_summary
        )
        self.checkout_btn.pack()

    def update_summary(self):
        total, discounts = self.cart.calculate_summary()
        self.text.delete("1.0", "end")
        self.text.insert("end", f"Podsumowanie:\nCena całkowita: {total:.2f} zł\n")
        if discounts:
            self.text.insert("end", "Zastosowane promocje:\n")
            for d in discounts:
                self.text.insert("end", f"- {d}\n")
        else:
            self.text.insert("end", "Brak promocji.\n")
