#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    
    cache = {}
    route = []

    # Loop through tickets list and create our cache (key = source, value = destination)
    for i in tickets:
        cache[i.source] = i.destination

    # Set our starting point to the cache with key set to None (first location)
    current_value = cache['NONE']

    # While the length of our route is less than the number of tickets
    while len(route) < length:
        # Add the current destination to the route list
        route.append(current_value)
        # Change current_value to the current key's destination (starting point for the next flight)
        current_value = cache[current_value]

    return route

# * We can hash each ticket such that the starting location is the key and
#   the destination is the value. Then, when constructing the entire
#   route, the `i`th location in the route can be found by checking the
#   hash table for the `i-1`th location.

# ticket_1 = Ticket("NONE", "PDX")
# ticket_2 = Ticket("PDX", "DCA")
# ticket_3 = Ticket("DCA", "NONE")

# tickets = [ticket_1, ticket_2, ticket_3]

# print(reconstruct_trip(tickets, 3))

ticket_1 = Ticket("PIT", "ORD")
ticket_2 = Ticket("XNA", "SAP")
ticket_3 = Ticket("SFO", "BHM")
ticket_4 = Ticket("FLG", "XNA")
ticket_5 = Ticket("NONE", "LAX")
ticket_6 = Ticket("LAX", "SFO")
ticket_7 = Ticket("SAP", "SLC")
ticket_8 = Ticket("ORD", "NONE")
ticket_9 = Ticket("SLC", "PIT")
ticket_10 = Ticket("BHM", "FLG")

tickets = [ticket_1, ticket_2, ticket_3, ticket_4, ticket_5, 
            ticket_6, ticket_7, ticket_8, ticket_9, ticket_10]

print(reconstruct_trip(tickets, 10))