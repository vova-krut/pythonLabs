import tickets
from datetime import datetime

conference = tickets.Event("It conference", datetime(2022, 12, 29), 59.99)

ticket = tickets.Ticket(conference)
advance_ticket = tickets.AdvanceTicket(conference)
late_ticket = tickets.LateTicket(conference)
student_ticket = tickets.StudentTicket(conference)

print(ticket)
print(advance_ticket)
print(late_ticket)
print(student_ticket)

forgotten_ticket = conference.get_ticket_by_number(1)
print(forgotten_ticket)
