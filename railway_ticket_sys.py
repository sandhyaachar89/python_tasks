
import datetime

class Train:
    def __init__(self, train_no, train_name, source, destination, seats, fare):
        self.train_no = train_no
        self.train_name = train_name
        self.source = source
        self.destination = destination
        self.seats = seats
        self.fare = fare

    def display_details(self):
        print(f"\nTrain No: {self.train_no}")
        print(f"Train Name: {self.train_name}")
        print(f"From: {self.source}  To: {self.destination}")
        print(f"Available Seats: {self.seats}")
        print(f"Fare per Ticket: ₹{self.fare}")

class Reservation:
    def __init__(self):
        self.trains = []
        self.bookings = []
        self.load_sample_trains()

    def load_sample_trains(self):
        self.trains.append(Train(101, "Chennai Express", "Chennai", "Bangalore", 50, 350))
        self.trains.append(Train(102, "Udaya Express", "Bangalore", "Mysore", 40, 200))
        self.trains.append(Train(103, "Coimbatore Express", "Chennai", "Coimbatore", 30, 500))

    def display_trains(self):
        print("\n========== AVAILABLE TRAINS ==========")
        for train in self.trains:
            train.display_details()
            print("-------------------------------------")

    def find_train(self, train_no):
        for train in self.trains:
            if train.train_no == train_no:
                return train
        return None

    def book_ticket(self):
        self.display_trains()
        train_no = int(input("\nEnter Train Number to Book: "))
        train = self.find_train(train_no)

        if not train:
            print("Train not found!")
            return

        name = input("Enter Passenger Name: ")
        age = int(input("Enter Age: "))
        seats = int(input("Enter Number of Tickets: "))

        if seats > train.seats:
            print("Not enough seats available!")
            return

        total_fare = seats * train.fare
        date = datetime.date.today()

        train.seats -= seats

        booking = {
            "name": name,
            "age": age,
            "train_no": train_no,
            "train_name": train.train_name,
            "from": train.source,
            "to": train.destination,
            "seats": seats,
            "total_fare": total_fare,
            "date": date
        }

        self.bookings.append(booking)
        print("\n Ticket booked successfully!")
        print(f"Passenger: {name}")
        print(f"Train: {train.train_name}")
        print(f"From {train.source} → {train.destination}")
        print(f"Seats: {seats}")
        print(f"Total Fare: ₹{total_fare}")
        print(f"Date: {date}")

    def view_bookings(self):
        if not self.bookings:
            print("\nNo bookings yet!")
            return
        print("\n========== ALL BOOKINGS ==========")
        for b in self.bookings:
            print(f"Passenger: {b['name']} | Train: {b['train_name']} | Date: {b['date']} | Fare: ₹{b['total_fare']}")
            print("---------------------------------")

    def cancel_ticket(self):
        name = input("\nEnter Passenger Name to Cancel Booking: ")
        found = False
        for booking in self.bookings:
            if booking["name"].lower() == name.lower():
                found = True
                self.bookings.remove(booking)
                train = self.find_train(booking["train_no"])
                if train:
                    train.seats += booking["seats"]
                print(" Ticket cancelled successfully!")
                break
        if not found:
            print(" No booking found with that name!")

def main():
    system = Reservation()

    while True:
        print("\n========== RAILWAY TICKET RESERVATION ==========")
        print("1. View Trains")
        print("2. Book Ticket")
        print("3. View All Bookings")
        print("4. Cancel Ticket")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            system.display_trains()
        elif choice == '2':
            system.book_ticket()
        elif choice == '3':
            system.view_bookings()
        elif choice == '4':
            system.cancel_ticket()
        elif choice == '5':
            print(" Thank you for using Railway Reservation System!")
            break
        else:
            print(" Invalid choice! Try again.")

if __name__ == "__main__":
    main()
