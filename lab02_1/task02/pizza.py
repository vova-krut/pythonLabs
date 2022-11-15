class Pizza:
    def __init__(self, ingredients: list[str], additional_ingredients: list[str] | None, sauce: str | None):
        if additional_ingredients:
            ingredients += additional_ingredients

        self.ingredients = ingredients
        self.sauce = sauce

    def __str__(self) -> str:
        return f"Ingredients: {self.ingredients}, sauce: {self.sauce}"

    def get_cost(self):
        price_of_ingredient = 2.99
        price_of_sauce = 1.99

        total = len(self.ingredients) * price_of_ingredient
        total += price_of_sauce if self.sauce else 0

        return round(total, 2)


class NeapolitanPizza(Pizza):
    title = "Neapolitan pizza"

    def __init__(self, additional_ingredients: list[str] | None, sauce="ketchup"):
        ingredients = ["salami", "cheese", "mushrooms"]
        super().__init__(ingredients, additional_ingredients, sauce)


class ChicagoPizza(Pizza):
    title = "Chicago pizza"

    def __init__(self, additional_ingredients: list[str] | None, sauce="mayonnaise"):
        ingredients = ["chicken", "cheese", "pepper"]
        super().__init__(ingredients, additional_ingredients, sauce)


class NewYorkStylePizza(Pizza):
    title = "New-York Style pizza"

    def __init__(self, additional_ingredients: list[str] | None, sauce="carbonara"):
        ingredients = ["beef", "onions", "cheese"]
        super().__init__(ingredients, additional_ingredients, sauce)


class SicilianPizza(Pizza):
    title = "Sicilian pizza"

    def __init__(self, additional_ingredients: list[str] | None, sauce="BBQ"):
        ingredients = ["chicken", "onions", "pickles"]
        super().__init__(ingredients, additional_ingredients, sauce)


class GreekPizza(Pizza):
    title = "Greek pizza"

    def __init__(self, additional_ingredients: list[str] | None, sauce="chili"):
        ingredients = ["salami", "mozzarella", "pickles"]
        super().__init__(ingredients, additional_ingredients, sauce)


class CaliforniaPizza(Pizza):
    title = "California pizza"

    def __init__(self, additional_ingredients: list[str] | None, sauce="garlic"):
        ingredients = ["salami", "tomato", "onions"]
        super().__init__(ingredients, additional_ingredients, sauce)


class DetroitPizza(Pizza):
    title = "Detroit pizza"

    def __init__(self, additional_ingredients: list[str] | None, sauce="buffalo"):
        ingredients = ["salami", "pepper", "pickles"]
        super().__init__(ingredients, additional_ingredients, sauce)


class StLouisPizza(Pizza):
    title = "St.Louis pizza"

    def __init__(self, additional_ingredients: list[str] | None, sauce="5 nights"):
        ingredients = ["chicken", "pepper", "onion"]
        super().__init__(ingredients, additional_ingredients, sauce)


pizza_days = {
    0: NeapolitanPizza,
    1: ChicagoPizza,
    2: NewYorkStylePizza,
    3: SicilianPizza,
    4: GreekPizza,
    5: CaliforniaPizza,
    6: DetroitPizza,
}
