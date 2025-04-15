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
}


# --- Fakty ---
class Item(Fact):
    name: str
    product: str
    used: bool = False


# --- Silnik regułowy ---
class RestaurantExpert(KnowledgeEngine):
    def __init__(self):
        super().__init__()
        self.total = 0.0
        self.promotions = []

    @Rule(Item(product=MATCH.product))
    def regular_price(self, product):
        self.total += PRODUCTS[product]

    @Rule(
        AS.a << Item(product="burger", used=False),
        AS.b << Item(product="fries", used=False),
    )
    def promo1(self, a, b):
        self.total -= 2.00
        self.promotions.append("Burger + frytki: -2.00 PLN")
        self.modify(a, used=True)
        self.modify(b, used=True)

    @Rule(
        AS.a << Item(product="burger", used=False),
        AS.b << Item(product="cola", used=False),
    )
    def promo2(self, a, b):
        self.total -= 1.00
        self.promotions.append("Burger + cola: -1.00 PLN")
        self.modify(a, used=True)
        self.modify(b, used=True)

    @Rule(
        AS.a << Item(product="ice_cream", used=False),
        AS.b << Item(product="cola", used=False),
    )
    def promo3(self, a, b):
        self.total -= 1.00
        self.promotions.append("Deser + cola: -1.00 PLN")
        self.modify(a, used=True)
        self.modify(b, used=True)

    @Rule(
        AS.a << Item(product="wrap", used=False),
        AS.b << Item(product="salad", used=False),
    )
    def promo4(self, a, b):
        self.total -= 2.00
        self.promotions.append("Wrap + sałatka: -2.00 PLN")
        self.modify(a, used=True)
        self.modify(b, used=True)

    @Rule(
        AS.a << Item(product="burger", used=False),
        AS.b << Item(product="apple_pie", used=False),
    )
    def promo5(self, a, b):
        self.total -= 1.00
        self.promotions.append("Burger + szarlotka: -1.00 PLN")
        self.modify(a, used=True)
        self.modify(b, used=True)

    @Rule(
        AS.a << Item(product="coffee", used=False),
        AS.b << Item(product="milkshake", used=False),
    )
    def promo6(self, a, b):
        self.total -= 1.00
        self.promotions.append("Kawa + shake: -1.00 PLN")
        self.modify(a, used=True)
        self.modify(b, used=True)

    @Rule(
        AS.a << Item(product="double_burger", used=False),
        AS.b << Item(product="cola", used=False),
    )
    def promo7(self, a, b):
        self.total -= 2.00
        self.promotions.append("Double + cola: -2.00 PLN")
        self.modify(a, used=True)
        self.modify(b, used=True)

    @Rule(
        AS.a << Item(product="nuggets", used=False),
        AS.b << Item(product="fries", used=False),
    )
    def promo8(self, a, b):
        self.total -= 1.00
        self.promotions.append("Nuggets + frytki: -1.00 PLN")
        self.modify(a, used=True)
        self.modify(b, used=True)

    @Rule(
        AS.a << Item(product="tea", used=False),
        AS.b << Item(product="apple_pie", used=False),
    )
    def promo9(self, a, b):
        self.total -= 1.00
        self.promotions.append("Herbata + szarlotka: -1.00 PLN")
        self.modify(a, used=True)
        self.modify(b, used=True)

    @Rule(
        AS.a << Item(product="cheeseburger", used=False),
        AS.b << Item(product="cola", used=False),
    )
    def promo10(self, a, b):
        self.total -= 1.00
        self.promotions.append("Cheeseburger + cola: -1.00 PLN")
        self.modify(a, used=True)
        self.modify(b, used=True)

    @Rule(
        AS.a << Item(product="onion_rings", used=False),
        AS.b << Item(product="wrap", used=False),
    )
    def promo11(self, a, b):
        self.total -= 1.00
        self.promotions.append("Cebulka + wrap: -1.00 PLN")
        self.modify(a, used=True)
        self.modify(b, used=True)

    @Rule(
        AS.a << Item(product="salad", used=False),
        AS.b << Item(product="water", used=False),
    )
    def promo12(self, a, b):
        self.total -= 1.00
        self.promotions.append("Sałatka + woda: -1.00 PLN")
        self.modify(a, used=True)
        self.modify(b, used=True)

    @Rule(
        AS.a << Item(product="coffee", used=False),
        AS.b << Item(product="onion_rings", used=False),
    )
    def promo13(self, a, b):
        self.total -= 1.00
        self.promotions.append("Kawa + cebulka: -1.00 PLN")
        self.modify(a, used=True)
        self.modify(b, used=True)

    @Rule(
        AS.a << Item(product="milkshake", used=False),
        AS.b << Item(product="ice_cream", used=False),
    )
    def promo14(self, a, b):
        self.total -= 1.00
        self.promotions.append("Shake + lody: -1.00 PLN")
        self.modify(a, used=True)
        self.modify(b, used=True)

    @Rule(
        AS.a << Item(product="cheeseburger", used=False),
        AS.b << Item(product="fries", used=False),
    )
    def promo15(self, a, b):
        self.total -= 1.00
        self.promotions.append("Cheeseburger + frytki: -1.00 PLN")
        self.modify(a, used=True)
        self.modify(b, used=True)


# --- GUI aplikacji ---
class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Restauracja - system regułowy")
        self.cart = []
        self.item_counter = 0  # <--- licznik pozycji

        # --- Górna część: produkty i koszyk ---
        top_frame = tk.Frame(root)
        top_frame.pack(padx=10, pady=10)

        # Lewa kolumna: produkty
        left_frame = tk.LabelFrame(top_frame, text="Produkty")
        left_frame.pack(side="left", padx=10)

        for name in PRODUCTS:
            price = PRODUCTS[name]
            btn = tk.Button(
                left_frame,
                text=f"{name} ({price:.2f} PLN)",
                command=lambda n=name: self.add_to_cart(n),
            )
            btn.pack(fill="x", pady=1)

        # Prawa kolumna: koszyk
        right_frame = tk.LabelFrame(top_frame, text="Koszyk")
        right_frame.pack(side="right", padx=10)

        self.cart_listbox = tk.Listbox(right_frame, width=30)
        self.cart_listbox.pack(padx=5, pady=5)

        # --- Dolna część: suma i promocje ---
        bottom_frame = tk.Frame(root)
        bottom_frame.pack(pady=10)

        self.total_label = tk.Label(
            bottom_frame, text="Suma: 0.00 PLN", font=("Arial", 14)
        )
        self.total_label.pack()

        self.promotions_label = tk.Label(
            bottom_frame, text="", fg="green", justify="left"
        )
        self.promotions_label.pack()

        calculate_btn = tk.Button(
            bottom_frame, text="Oblicz zamówienie", command=self.calculate_total
        )
        calculate_btn.pack(pady=5)

    def add_to_cart(self, product_name):
        self.cart.append(product_name)
        self.cart_listbox.insert(tk.END, product_name)

    def calculate_total(self):
        engine = RestaurantExpert()
        engine.reset()
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
