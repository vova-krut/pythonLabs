class Product:
    def __init__(self, name: str, description: str, price: float):
        if price <= 0:
            raise ValueError("Price can not be less or equal to 0")
        self.name = name
        self.description = description
        self.price = price

    def __str__(self):
        return f"{self.name}: {self.price}"


class Customer:
    def __init__(self, name: str, surname: str, email: str, phone: str):
        self.name = name
        self.surname = surname
        self.email = email
        self.phone = phone

    def __str__(self):
        return f"{self.name} {self.surname}"


class Order:
    def __init__(self, customer: Customer, products: list):
        self._customer = customer
        self._products = products

    def __str__(self):
        return f"""Customer: {self._customer} 
        Products: {[str(product) for product in self._products]} 
        Total: {self.total_value()}"""

    def add_product(self, product: Product):
        self._products.append(product)

    def remove_product(self, product: Product):
        self._products.remove(product)

    def total_value(self):
        return sum(product.price for product in self._products)
