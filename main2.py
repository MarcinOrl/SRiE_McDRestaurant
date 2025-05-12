import tkinter as tk
from experta import *

# --- Produkty i ceny ---
PRODUCTS = {
    "burger": 10.99,
    "fries": 5.49,
    "cola": 3.99,
    "ice_cream": 6.29,
    "nuggets": 8.79,
    "coffee": 5.19,
    "salad": 7.49,
    "wrap": 9.99,
    "water": 2.99,
    "tea": 3.49,
    "milkshake": 6.59,
    "apple_pie": 4.99,
    "cheeseburger": 11.49,
    "double_burger": 13.99,
    "onion_rings": 4.79,
    "vegan_burger": 12.99,
    "smoothie": 7.99,
    "hot_dog": 9.49,
    "latte": 6.29,
    "mozzarella_sticks": 6.99,
    "brownie": 5.49,
}


# --- Fakty ---
class Item(Fact):
    name: str
    product: str
    used: bool = False


class VIPStatus(Fact):
    status: bool = False


# --- Silnik regułowy ---
class RestaurantExpert(KnowledgeEngine):
    def __init__(self):
        super().__init__()
        self.total = 0.0
        self.promotions = []

    @Rule(Item(product=MATCH.product))
    def regular_price(self, product):
        self.total += PRODUCTS[product]

    # @Rule(
    #     AS.a << Item(product="burger", used=False, name=MATCH.na),
    #     AS.b << Item(product="burger", used=False, name=MATCH.nb),
    #     AS.c << Item(product="burger", used=False, name=MATCH.nc),
    #     TEST(lambda na, nb, nc: na < nb < nc),
    #     salience=10,
    # )
    # def three_burgers_in_two(self, a, b, c):
    #     self.total -= PRODUCTS["burger"]
    #     self.promotions.append("3 burgery w cenie 2: -10.99 PLN")
    #     self.modify(a, used=True)
    #     self.modify(b, used=True)
    #     self.modify(c, used=True)

    @Rule(
        AS.a << Item(product="burger", used=False),
        AS.b << Item(product="fries", used=False),
        salience=0,
    )
    def promo1(self, a, b):
        self.total -= 2.00
        self.promotions.append("Burger + frytki: -2.00 PLN")
        self.modify(a, used=True)
        self.modify(b, used=True)

    @Rule(
        AS.a << Item(product="burger", used=False),
        AS.b << Item(product="cola", used=False),
        salience=0,
    )
    def promo2(self, a, b):
        self.total -= 1.00
        self.promotions.append("Burger + cola: -1.00 PLN")
        self.modify(a, used=True)
        self.modify(b, used=True)

    @Rule(
        AS.a << Item(product="ice_cream", used=False),
        AS.b << Item(product="cola", used=False),
        salience=0,
    )
    def promo3(self, a, b):
        self.total -= 1.00
        self.promotions.append("Deser + cola: -1.00 PLN")
        self.modify(a, used=True)
        self.modify(b, used=True)

    @Rule(
        AS.a << Item(product="wrap", used=False),
        AS.b << Item(product="salad", used=False),
        salience=0,
    )
    def promo4(self, a, b):
        self.total -= 2.00
        self.promotions.append("Wrap + sałatka: -2.00 PLN")
        self.modify(a, used=True)
        self.modify(b, used=True)

    @Rule(
        AS.a << Item(product="burger", used=False),
        AS.b << Item(product="apple_pie", used=False),
        salience=0,
    )
    def promo5(self, a, b):
        self.total -= 1.00
        self.promotions.append("Burger + szarlotka: -1.00 PLN")
        self.modify(a, used=True)
        self.modify(b, used=True)

    @Rule(
        AS.a << Item(product="coffee", used=False),
        AS.b << Item(product="milkshake", used=False),
        salience=0,
    )
    def promo6(self, a, b):
        self.total -= 1.00
        self.promotions.append("Kawa + shake: -1.00 PLN")
        self.modify(a, used=True)
        self.modify(b, used=True)

    @Rule(
        AS.a << Item(product="double_burger", used=False),
        AS.b << Item(product="cola", used=False),
        salience=0,
    )
    def promo7(self, a, b):
        self.total -= 2.00
        self.promotions.append("Double + cola: -2.00 PLN")
        self.modify(a, used=True)
        self.modify(b, used=True)

    @Rule(
        AS.a << Item(product="nuggets", used=False),
        AS.b << Item(product="fries", used=False),
        salience=0,
    )
    def promo8(self, a, b):
        self.total -= 1.00
        self.promotions.append("Nuggets + frytki: -1.00 PLN")
        self.modify(a, used=True)
        self.modify(b, used=True)

    @Rule(
        AS.a << Item(product="tea", used=False),
        AS.b << Item(product="apple_pie", used=False),
        salience=0,
    )
    def promo9(self, a, b):
        self.total -= 1.00
        self.promotions.append("Herbata + szarlotka: -1.00 PLN")
        self.modify(a, used=True)
        self.modify(b, used=True)

    @Rule(
        AS.a << Item(product="cheeseburger", used=False),
        AS.b << Item(product="cola", used=False),
        salience=0,
    )
    def promo10(self, a, b):
        self.total -= 1.00
        self.promotions.append("Cheeseburger + cola: -1.00 PLN")
        self.modify(a, used=True)
        self.modify(b, used=True)

    @Rule(
        AS.a << Item(product="onion_rings", used=False),
        AS.b << Item(product="wrap", used=False),
        salience=0,
    )
    def promo11(self, a, b):
        self.total -= 1.00
        self.promotions.append("Cebulka + wrap: -1.00 PLN")
        self.modify(a, used=True)
        self.modify(b, used=True)

    @Rule(
        AS.a << Item(product="salad", used=False),
        AS.b << Item(product="water", used=False),
        salience=0,
    )
    def promo12(self, a, b):
        self.total -= 1.00
        self.promotions.append("Sałatka + woda: -1.00 PLN")
        self.modify(a, used=True)
        self.modify(b, used=True)

    @Rule(
        AS.a << Item(product="coffee", used=False),
        AS.b << Item(product="onion_rings", used=False),
        salience=0,
    )
    def promo13(self, a, b):
        self.total -= 1.00
        self.promotions.append("Kawa + cebulka: -1.00 PLN")
        self.modify(a, used=True)
        self.modify(b, used=True)

    @Rule(
        AS.a << Item(product="milkshake", used=False),
        AS.b << Item(product="ice_cream", used=False),
        salience=0,
    )
    def promo14(self, a, b):
        self.total -= 1.00
        self.promotions.append("Shake + lody: -1.00 PLN")
        self.modify(a, used=True)
        self.modify(b, used=True)

    @Rule(
        AS.a << Item(product="cheeseburger", used=False),
        AS.b << Item(product="fries", used=False),
        salience=0,
    )
    def promo15(self, a, b):
        self.total -= 1.00
        self.promotions.append("Cheeseburger + frytki: -1.00 PLN")
        self.modify(a, used=True)
        self.modify(b, used=True)

    @Rule(
        AS.a << Item(product="vegan_burger", used=False),
        AS.b << Item(product="smoothie", used=False),
        salience=0,
    )
    def promo16(self, a, b):
        self.total -= 2.50
        self.promotions.append("Vegan burger + smoothie: -2.50 PLN")
        self.modify(a, used=True)
        self.modify(b, used=True)

    @Rule(
        AS.a << Item(product="hot_dog", used=False),
        AS.b << Item(product="cola", used=False),
        salience=0,
    )
    def promo17(self, a, b):
        self.total -= 1.00
        self.promotions.append("Hot dog + cola: -1.00 PLN")
        self.modify(a, used=True)
        self.modify(b, used=True)

    @Rule(
        AS.a << Item(product="latte", used=False),
        AS.b << Item(product="brownie", used=False),
        salience=0,
    )
    def promo18(self, a, b):
        self.total -= 1.50
        self.promotions.append("Latte + brownie: -1.50 PLN")
        self.modify(a, used=True)
        self.modify(b, used=True)

    @Rule(
        AS.a << Item(product="mozzarella_sticks", used=False),
        AS.b << Item(product="fries", used=False),
        salience=0,
    )
    def promo19(self, a, b):
        self.total -= 1.00
        self.promotions.append("Mozzarella sticks + frytki: -1.00 PLN")
        self.modify(a, used=True)
        self.modify(b, used=True)

    @Rule(salience=-10)
    def discount_over_50(self):
        if self.total > 50:
            discount = self.total * 0.10
            self.total -= discount
            self.promotions.append(
                f"Zniżka 10% na zamówienie powyżej 50 PLN: -{discount:.2f} PLN"
            )

    @Rule(VIPStatus(status=True), salience=-20)
    def vip_discount(self):
        discount = self.total * 0.20
        self.total -= discount
        self.promotions.append(f"Klient VIP: -{discount:.2f} PLN")


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

        for i, product_name in enumerate(self.cart):
            engine.declare(
                Item(name=f"{product_name}_{i}", product=product_name, used=False)
            )
        engine.run()

        self.total_label.config(text=f"Suma: {engine.total:.2f} PLN")
        self.promotions_label.config(
            text="\n".join(engine.promotions) or "Brak promocji"
        )


# --- Start aplikacji ---
if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
