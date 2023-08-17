class Item:
    # Implement the Item here
    def __init__(self, name: str, price: int):
        self.name = name
        self.price = price


class ShoppingCart:
    # Implement the ShoppingCart here
    shoppingBasket = {}

    def add(self, item: Item):
        self.shoppingBasket.setdefault(item, 0)
        self.shoppingBasket[item] += 1

    def total(self) -> int:
        return sum(item.price * self.shoppingBasket[item] for item in self.shoppingBasket)

    def __len__(self):
        return sum(list(self.shoppingBasket.values()))


i1 = Item("banane", 6)
i2 = Item("oua", 10)
c = ShoppingCart()
c.add(i1)
c.add(i1)
c.add(i1)
c.add(i2)
c.add(i2)
c.add(i2)
c.add(i2)
print(c.total())
print(len(c))

