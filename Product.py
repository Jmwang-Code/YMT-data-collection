class Product:
    def __init__(self, area, category, price, change):
        self.area = area
        self.category = category
        self.price = price
        self.change = change

    def __str__(self):
        return f"Product(area={self.area}, category={self.category}, price={self.price}, change={self.change})"
