import json

class RoomBooking:

    rooms_items = []
    customer_budget = {}

    def __init__(self, hotel, room_no, add_items):
        self.hotel = hotel
        self.room_no = room_no
        self.add_items = add_items

    def add_hotel(self):
        """
        add Hotel name and creat a list.
        """
        return "Hotel added: {} = {}".format(self.hotel, [])

    def add_room_items(self):
        """
        Method to add Room and Items. 
        """
        room_no = {}
        room_no[self.room_no] = self.add_items
        self.rooms_items.append(room_no)
        return "Added room and items to the Hotel."

    def view_items(self):
        """
        Method to view the list of Rooms, Items present in the room and its Price.
        """
        print("Room No.            Items               Price")
        print("-" * 50)
        for i in self.rooms_items:
            for key, value in i.items():
                print(key)
                value = json.loads(value)
            for key, val in value.items():
                length = 15 - (len(key) - 4)
                print("  " * 10, key, " " * length, val)
            print("-" * 50)

    def budget(self):
        """
        Method to view the list of Rooms, Items present in the room and its Price.
        Output : Dictionary.
        """
        for i in self.rooms_items:
            total_amount = 0
            for key, value in i.items():
                Room = key
                value = json.loads(value)
            for val in value.values():
                total_amount += val
                self.customer_budget[Room] = total_amount
        return self.customer_budget


hotel = str(input("Enter the name of the Hotel: "))
while True:
    print()
    room_no = input("Add room number: ")
    if room_no == "":
        break

    add_items = input("Add 5 items to Room: ")
    r = RoomBooking(hotel, room_no, add_items)

    print()
    print(r.add_hotel())
    print(r.add_room_items())

view_items = input("Press Enter to view the items in the Room: ")
r.view_items()

def budget_range(budget):
    """
    Method to list the budget rooms based on Customer Input.
    """
    amount = r.budget()
    budget_rooms = {}

    for key, value in amount.items():
        if value <= int(budget):
            budget_rooms[key] = value
    return budget_rooms

while True:
    print()
    budget = input("Enter your budget :")
    try:
        if budget == "":
            break
    except ValueError as e:
        print("Error!! Enter the integer value.")
    
    print()
    print("Rooms and Price List.")
    print("-"*30)
    for key, value in r.budget().items():
        print("Room {} = {}/-".format(key, value))
    
    print()
    print("Customer Budget Rooms list")
    print("-"*50)
    for key, value in budget_range(budget).items():
        print("Room {} = {}/-".format(key, value))
