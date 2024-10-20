class HotelManagement: # this class is responsible for managing the rooms and reservations
    def __init__(self):
        self.rooms = [f"Room {i}" for i in range(1, 21)] # Hotel have 20 rooms
        self.reservation = {}

    def display_rooms(self):
        print("Available rooms in the hotel:")
        for room in self.rooms:
            print(room)  

if __name__== "__main__":
    hotel = HotelManagement()
    hotel.display_rooms()           