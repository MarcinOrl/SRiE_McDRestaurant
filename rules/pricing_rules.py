from experta import *


class Product(Fact):
    """Fakt reprezentujący produkt w koszyku"""

    id: int
    name: str
    price: float


class Total(Fact):
    """Fakt z aktualną sumą zamówienia bez zniżki"""

    value: float


class DiscountedTotal(Fact):
    """Fakt z sumą zamówienia po uwzględnieniu zniżki"""

    value: float


class PricingRules(KnowledgeEngine):
    def __init__(self):
        super().__init__()
        self.discounts = []

    @DefFacts()
    def _initial_facts(self):
        yield Total(value=0)
        yield DiscountedTotal(value=0)

    @Rule(AS.product << Product())
    def accumulate_total(self, product):
        """Sumowanie wszystkich produktów do zwykłej sumy"""
        total_fact = next(
            (fact for fact in self.facts.values() if isinstance(fact, Total)), None
        )
        if total_fact:
            new_total = total_fact["value"] + product["price"]
            self.retract(total_fact)
            self.declare(Total(value=new_total))
            print(f"Updated total: {new_total}")

            discounted_total_fact = next(
                (
                    fact
                    for fact in self.facts.values()
                    if isinstance(fact, DiscountedTotal)
                ),
                None,
            )
            if discounted_total_fact:
                self.retract(discounted_total_fact)
                self.declare(DiscountedTotal(value=new_total))

    @Rule(AS.total << Total(value=P(lambda total: total >= 20)))
    def apply_discount(self, total):
        """Stosowanie zniżki dla zamówienia >= 20"""
        total_value = total["value"]
        discount = total_value * 0.1
        print(f"Applied discount: {discount}")
        discounted_total_value = total_value - discount
        discounted_total_fact = next(
            (fact for fact in self.facts.values() if isinstance(fact, DiscountedTotal)),
            None,
        )
        if discounted_total_fact:
            self.retract(discounted_total_fact)
            self.declare(DiscountedTotal(value=discounted_total_value))
        print(f"Total after discount: {discounted_total_value}")

        discount_message = f"Applied 10% discount. Saved {discount:.2f} zł"
        existing_discount = next(
            (d for d in self.discounts if "Applied 10% discount." in d), None
        )

        if existing_discount:
            self.discounts[self.discounts.index(existing_discount)] = discount_message
        else:
            self.discounts.append(discount_message)
