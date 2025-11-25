#!/usr/bin/env python3

class CashRegister:
    def __init__(self, discount=0):
        self.total = 0
        self.discount = discount
        self.items = []
        self.transactions = []  # track all transactions

    def add_item(self, title, price, quantity=1):
        self.total += price * quantity
        transaction = {"title": title, "price": price, "quantity": quantity}
        self.transactions.append(transaction)
        for _ in range(quantity):
            self.items.append(title)

    def apply_discount(self):
        if self.discount > 0:
            self.total *= (1 - self.discount / 100)
            print(f"After the discount, the total comes to ${self.total:.0f}.")
        else:
            print("There is no discount to apply.")

    def void_last_transaction(self):
        if self.transactions:
            last = self.transactions.pop()
            self.total -= last["price"] * last["quantity"]
            for _ in range(last["quantity"]):
                self.items.pop()
        else:
            self.total = 0

