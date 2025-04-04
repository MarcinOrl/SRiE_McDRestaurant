import tkinter as tk
from tkinter import ttk
from gui.product_list import ProductList
from gui.selected_list import SelectedList
from gui.summary_panel import SummaryPanel
from services.cart_manager import CartManager
from models.product import Product
import json


def run_app():
    root = tk.Tk()
    root.title("Restaurant App")
    root.geometry("500x300")

    cart = CartManager()
    with open("data/products.json") as f:
        products = [Product(**product) for product in json.load(f)]

    left = ProductList(root, products, cart)
    left.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    right = SelectedList(root, cart)
    right.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

    left.set_selected_list(right)

    summary = SummaryPanel(root, cart)
    summary.pack(side=tk.BOTTOM, fill=tk.X)

    root.mainloop()
