from __future__ import annotations

import random
from dataclasses import dataclass, field
from datetime import datetime
from typing import Dict, List, Optional


@dataclass
class Product:
    name: str
    price: float
    quantity: int
    category: str
    sku: str
    is_active: bool = True


@dataclass
class CartItem:
    product: Product
    quantity: int


@dataclass
class ShoppingCart:
    items: List[CartItem] = field(default_factory=list)

    def add_item(self, product: Product, quantity: int = 1) -> None:
        if quantity <= 0:
            raise ValueError("Quantity must be positive")
        for existing in self.items:
            if existing.product.sku == product.sku:
                existing.quantity += quantity
                return
        self.items.append(CartItem(product=product, quantity=quantity))

    def remove_item(self, sku: str, quantity: Optional[int] = None) -> None:
        for index, item in enumerate(self.items):
            if item.product.sku == sku:
                if quantity is None or quantity >= item.quantity:
                    del self.items[index]
                else:
                    item.quantity -= quantity
                return
        raise KeyError(f"No item found with sku {sku}")

    def total(self) -> float:
        return sum(item.product.price * item.quantity for item in self.items)

    def summary(self) -> str:
        if not self.items:
            return "Your cart is empty."
        lines = [f"Cart contains {len(self.items)} item(s):"]
        for item in self.items:
            lines.append(f"- {item.product.name} x{item.quantity}: ${item.product.price * item.quantity:.2f}")
        lines.append(f"Total: ${self.total():.2f}")
        return "\n".join(lines)


def format_currency(amount: float) -> str:
    return f"${amount:,.2f}"


def build_sample_inventory() -> Dict[str, Product]:
    products = {
        "A100": Product("Laptop Stand", 24.99, 8, "Accessories", "A100"),
        "B200": Product("Mechanical Keyboard", 89.50, 5, "Peripherals", "B200"),
        "C300": Product("USB-C Cable", 12.00, 15, "Accessories", "C300"),
        "D400": Product("Monitor Arm", 59.99, 3, "Furniture", "D400"),
        "E500": Product("Webcam", 49.95, 6, "Peripherals", "E500"),
    }
    return products


def filter_products(products: Dict[str, Product], category: Optional[str] = None) -> List[Product]:
    matching = []
    for product in products.values():
        if product.is_active and (category is None or product.category.lower() == category.lower()):
            matching.append(product)
    return sorted(matching, key=lambda item: item.name)


def generate_sales_report(products: Dict[str, Product]) -> str:
    lines = ["Sales Report", "=" * 20]
    for product in sorted(products.values(), key=lambda item: item.price, reverse=True):
        if product.is_active:
            lines.append(f"{product.name} | {product.category} | {format_currency(product.price)} | Qty: {product.quantity}")
    return "\n".join(lines)


def create_daily_digest() -> str:
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    score = random.randint(70, 100)
    return f"Daily digest generated at {timestamp} with quality score {score}."


def describe_product(product: Product) -> str:
    return f"{product.name} ({product.sku}) is a {product.category.lower()} item priced at {format_currency(product.price)}."


def run_demo() -> None:
    inventory = build_sample_inventory()
    cart = ShoppingCart()

    print("Hello from the expanded demo script!")
    print("Available products:")
    for product in filter_products(inventory):
        print(f"- {describe_product(product)}")

    cart.add_item(inventory["A100"], 2)
    cart.add_item(inventory["B200"], 1)
    cart.add_item(inventory["C300"], 3)

    print("\nCart preview:")
    print(cart.summary())

    print("\nSales report:")
    print(generate_sales_report(inventory))

    print(f"\n{create_daily_digest()}")


if __name__ == "__main__":
    run_demo()
