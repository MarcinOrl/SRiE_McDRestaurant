from experta import *
from experta import Fact
from products import PRODUCTS


# --- Fakty ---
class Item(Fact):
    name: str
    product: str
    used: bool = False


class VIPStatus(Fact):
    status: bool = False


class PaperBag(Fact):
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

    @Rule(
        AS.a << Item(product="burger", used=False, name=MATCH.na),
        AS.b << Item(product="burger", used=False, name=MATCH.nb),
        AS.c << Item(product="burger", used=False, name=MATCH.nc),
        TEST(lambda na, nb, nc: na < nb < nc),
        salience=10,
    )
    def three_burgers_in_two(self, a, b, c):
        self.total -= PRODUCTS["burger"]
        self.promotions.append("3 burgery w cenie 2: -10.99 PLN")
        self.modify(a, used=True)
        self.modify(b, used=True)
        self.modify(c, used=True)

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
        self.promotions.append("Lody + cola: -1.00 PLN")
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
        self.promotions.append("Podwójny burger + cola: -2.00 PLN")
        self.modify(a, used=True)
        self.modify(b, used=True)

    @Rule(
        AS.a << Item(product="nuggets", used=False),
        AS.b << Item(product="fries", used=False),
        salience=0,
    )
    def promo8(self, a, b):
        self.total -= 1.00
        self.promotions.append("Nuggety + frytki: -1.00 PLN")
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
        self.promotions.append("Wegański burger + smoothie: -2.50 PLN")
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

    @Rule(PaperBag(status=True), salience=-30)
    def add_bag_price(self):
        self.total += 0.50
        self.promotions.append("Torba papierowa: +0.50 PLN")
