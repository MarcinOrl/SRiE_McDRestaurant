from experta import *


class PricingRules(KnowledgeEngine):
    @DefFacts()
    def _initial_facts(self):
        yield Fact(action="calculate_total")

    @Rule(Fact(action="calculate_total"))
    def apply_discount(self):
        # Placeholder: simple print to simulate rule processing
        print("Rules engine: calculating total with potential discounts")
