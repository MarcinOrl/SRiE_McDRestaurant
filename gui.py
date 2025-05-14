import tkinter as tk
from rules import Item, VIPStatus, PaperBag, RestaurantExpert
from products import PRODUCTS


# --- GUI aplikacji ---
class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Restauracja - system regułowy")
        self.cart = []
        self.item_counter = 0

        # --- Górna część: produkty i koszyk ---
        top_frame = tk.Frame(root, bg="#f8f9fa")
        top_frame.grid(row=0, column=0, padx=20, pady=20)

        # Lewa kolumna: produkty
        left_frame = tk.LabelFrame(
            top_frame, text="Produkty", bg="#f8f9fa", font=("Arial", 12, "bold")
        )
        left_frame.grid(row=0, column=0, padx=10, pady=10)

        # Canvas i pasek przewijania dla produktów
        canvas = tk.Canvas(left_frame)
        scroll_y = tk.Scrollbar(left_frame, orient="vertical", command=canvas.yview)
        canvas.configure(yscrollcommand=scroll_y.set)

        product_frame = tk.Frame(canvas)
        canvas.create_window((0, 0), window=product_frame, anchor="nw")
        scroll_y.pack(side="right", fill="y")
        canvas.pack(side="left", fill="both", expand=True)

        # Dodawanie przycisków produktów do przewijalnego widżetu w dwóch kolumnach
        row = 0
        col = 0
        for i, name in enumerate(PRODUCTS):
            price = PRODUCTS[name]
            btn = tk.Button(
                product_frame,
                text=f"{name} ({price:.2f} PLN)",
                command=lambda n=name: self.add_to_cart(n),
                width=20,
                height=2,
                bg="#e3e4e8",
                relief="solid",
                font=("Arial", 10),
                borderwidth=1,
            )
            btn.grid(row=row, column=col, padx=5, pady=5)

            col += 1
            if col == 2:
                col = 0
                row += 1

        product_frame.update_idletasks()
        canvas.config(scrollregion=canvas.bbox("all"))

        # Prawa kolumna: koszyk
        right_frame = tk.LabelFrame(
            top_frame, text="Koszyk", bg="#f8f9fa", font=("Arial", 12, "bold")
        )
        right_frame.grid(row=0, column=1, padx=10, pady=10)

        # Canvas i pasek przewijania dla koszyka
        self.cart_canvas = tk.Canvas(right_frame)
        cart_scroll_y = tk.Scrollbar(
            right_frame, orient="vertical", command=self.cart_canvas.yview
        )
        self.cart_canvas.configure(yscrollcommand=cart_scroll_y.set)

        cart_frame = tk.Frame(self.cart_canvas)
        self.cart_canvas.create_window((0, 0), window=cart_frame, anchor="nw")
        cart_scroll_y.pack(side="right", fill="y")
        self.cart_canvas.pack(side="left", fill="both", expand=True)

        self.cart_frame = cart_frame

        # --- Dolna część: suma i promocje ---
        bottom_frame = tk.Frame(root, bg="#f8f9fa")
        bottom_frame.grid(row=1, column=0, padx=20, pady=10)

        # Lewa kolumna: opcje (checkboxy)
        left_options_frame = tk.Frame(bottom_frame, bg="#f8f9fa")
        left_options_frame.grid(row=0, column=0, sticky="nw", padx=10)

        self.vip_var = tk.BooleanVar()
        vip_checkbox = tk.Checkbutton(
            left_options_frame,
            text="Klient VIP: -20% na całe zamówienie",
            variable=self.vip_var,
            bg="#f8f9fa",
            font=("Arial", 10),
        )
        vip_checkbox.pack(anchor="w", pady=5)

        self.bag_var = tk.BooleanVar()
        bag_checkbox = tk.Checkbutton(
            left_options_frame,
            text="Torba papierowa (+0.50 zł)",
            variable=self.bag_var,
            bg="#f8f9fa",
            font=("Arial", 10),
        )
        bag_checkbox.pack(anchor="w", pady=5)

        # Prawa kolumna: suma, promocje, przycisk
        right_summary_frame = tk.Frame(bottom_frame, bg="#f8f9fa")
        right_summary_frame.grid(row=0, column=1, sticky="ne", padx=40)

        self.total_label = tk.Label(
            right_summary_frame,
            text="Suma: 0.00 PLN",
            font=("Arial", 14, "bold"),
            bg="#f8f9fa",
        )
        self.total_label.grid(row=0, column=0, pady=10)

        self.promotions_label = tk.Label(
            right_summary_frame,
            text="",
            fg="green",
            justify="left",
            bg="#f8f9fa",
            font=("Arial", 10),
        )
        self.promotions_label.grid(row=1, column=0, pady=5)

        calculate_btn = tk.Button(
            right_summary_frame,
            text="Oblicz zamówienie",
            command=self.calculate_total,
            bg="#5cb85c",
            fg="white",
            font=("Arial", 12),
            relief="flat",
            height=2,
            width=20,
        )
        calculate_btn.grid(row=2, column=0, pady=10)

    def add_to_cart(self, product_name):
        self.cart.append(product_name)
        self.update_cart()

    def remove_from_cart(self, product_name):
        self.cart.remove(product_name)
        self.update_cart()

    def update_cart(self):
        for widget in self.cart_frame.winfo_children():
            widget.destroy()

        row = 0
        col = 0
        for name in self.cart:
            btn = tk.Button(
                self.cart_frame,
                text=f"{name} (Usuń)",
                command=lambda n=name: self.remove_from_cart(n),
                width=20,
                height=2,
                bg="#f8f9fa",
                relief="solid",
                font=("Arial", 10),
                borderwidth=1,
            )
            btn.grid(row=row, column=col, padx=5, pady=5)

            col += 1
            if col == 2:
                col = 0
                row += 1

        self.cart_frame.update_idletasks()
        # Dostosowanie regionu przewijania koszyka
        self.cart_canvas.config(scrollregion=self.cart_canvas.bbox("all"))

    def calculate_total(self):
        engine = RestaurantExpert()
        engine.reset()

        if self.vip_var.get():
            engine.declare(VIPStatus(status=True))

        if self.bag_var.get():
            engine.declare(PaperBag(status=True))

        for i, product_name in enumerate(self.cart):
            engine.declare(
                Item(name=f"{product_name}_{i}", product=product_name, used=False)
            )
        engine.run()

        self.total_label.config(text=f"Suma: {engine.total:.2f} PLN")
        self.promotions_label.config(
            text="\n".join(engine.promotions) or "Brak promocji"
        )
