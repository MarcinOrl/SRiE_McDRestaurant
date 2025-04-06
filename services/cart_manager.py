from rules.pricing_rules import PricingRules, Product, Total, DiscountedTotal
from experta import Fact


class CartManager:
    def __init__(self):
        self.selected_products = []

    def add_product(self, product):
        """Dodaj produkt do listy"""
        self.selected_products.append(product)

    def clear(self):
        """Wyczyść koszyk"""
        self.selected_products.clear()

    def calculate_summary(self):
        """Oblicz podsumowanie koszyka i zastosuj zniżkę"""
        engine = PricingRules()
        engine.reset()
        engine.discounts = []  # Resetowanie listy zniżek

        for i, p in enumerate(self.selected_products):
            engine.declare(Product(id=i, name=p.name, price=p.price))

        engine.run()

        # Zwróć aktualną sumę z faktu Total oraz zastosowane zniżki
        total_fact = next(
            (
                fact
                for fact in engine.facts.values()
                if isinstance(fact, DiscountedTotal)
            ),
            None,
        )
        return total_fact["value"], engine.discounts
