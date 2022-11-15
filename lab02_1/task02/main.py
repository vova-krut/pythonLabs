import pizza
from datetime import datetime


def main():
    day_of_week = get_day_of_week()
    pizza_of_the_day = get_pizza_of_the_day(day_of_week, pizza.pizza_days)

    print(f"Hello, it is {day_of_week + 1} day of the week today!")
    print(f"So today's pizza of the day is {pizza_of_the_day.title}")
    print("What additional ingredients would you like ?")

    additional_ingredients = get_additional_ingredients()
    customers_pizza = pizza_of_the_day(additional_ingredients)

    print(customers_pizza)
    print(f"Your total is {customers_pizza.get_cost()}")


def get_pizza_of_the_day(day_of_week: int, pizza_days: dict[int, type[pizza.Pizza]]):
    pizza_of_the_day = pizza_days[day_of_week]

    return pizza_of_the_day


def get_day_of_week():
    day_of_week = datetime.weekday(datetime.today())

    return day_of_week


def get_additional_ingredients():
    additional_ingredients = input()
    if additional_ingredients:
        additional_ingredients_list = list(
            map(
                lambda ingredient: ingredient.strip(),
                additional_ingredients.split(","),
            )
        )

        return additional_ingredients_list


if __name__ == "__main__":
    main()
