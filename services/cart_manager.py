class CartManager:
    def __init__(self):
        self.selected_products = []

    def add_product(self, product):
        self.selected_products.append(product)

    def clear(self):
        self.selected_products.clear()

    def total_price(self):
        return sum(product.price for product in self.selected_products)
