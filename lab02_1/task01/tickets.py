import json
from datetime import datetime


class Event:
    def __init__(self, name: str, date: datetime, base_ticket_price: float,
                 ticket_types_prices={"default": 1.0, "student": 0.5, "late": 1.1, "advance": 0.6}):

        self.name = name
        self.date = date
        self.base_ticket_price = base_ticket_price
        self.ticket_types_prices = ticket_types_prices

    def get_ticket_price(self, type: str):
        if type not in self.ticket_types_prices:
            raise TypeError(f"Event {self.name} does not have {type} tickets")

        return self.ticket_types_prices[type] * self.base_ticket_price

    def get_ticket_by_number(self, id: int):
        tickets = self.__get_json_data()[self.name]
        for ticket in tickets:
            if ticket['id'] == id:
                return ticket

    def register_ticket(self, type: str):
        json_data = self.__get_json_data()

        if self.name not in json_data:
            json_data[self.name] = [{"id": 1, "type": type}]
        else:
            json_data = self.__add_data_to_json(json_data, type)

        self.__save_data_to_file(json_data)

    def __get_json_data(self) -> dict[str, list]:
        with open('data.json', encoding='utf-8') as json_file:
            try:
                data = json.load(json_file)
            except json.JSONDecodeError:
                data = {self.name: []}

        return data

    def __add_data_to_json(self, json_data: dict[str, list], type: str):
        event_tickets = json_data[self.name]

        next_id = event_tickets[-1]['id'] + 1

        event_tickets.append({"id": next_id, "type": type})

        json_data[self.name] = event_tickets

        return json_data

    def __save_data_to_file(self, json_data: dict[str, list]):
        with open('data.json', 'w', encoding='utf-8') as json_file:
            json_string = json.dumps(json_data)

            json_file.write(json_string)


class Ticket:
    def __init__(self, event: Event, type="default"):
        self.event = event
        self.type = type
        self.event.register_ticket(self.type)

    def __str__(self):
        return f"Event: {self.event.name}, ticket type: {self.type}, price: {self.get_price()}"

    def get_price(self):
        price = self.event.get_ticket_price(self.type)

        return round(price, 2)


class AdvanceTicket(Ticket):
    def __init__(self, event: Event):
        super().__init__(event, "advance")


class StudentTicket(Ticket):
    def __init__(self, event: Event):
        super().__init__(event, "student")


class LateTicket(Ticket):
    def __init__(self, event: Event):
        super().__init__(event, "late")
