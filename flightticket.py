class FlightBookingSystem:
    def __init__(self):
        self.tickets = {}  # Stores booked tickets

    def book_ticket(self):
        name = input("Enter your name: ")
        flight_no = input("Enter Flight Number: ")
        departure = input("Enter Departure City: ")
        destination = input("Enter Destination City: ")
        seat_no = f"Seat-{len(self.tickets) + 1}"  # Auto-assign a seat number
        ticket_id = f"TKT{len(self.tickets) + 1001}"  # Unique Ticket ID
        
        self.tickets[ticket_id] = {
            "Name": name,
            "Flight No": flight_no,
            "From": departure,
            "To": destination,
            "Seat No": seat_no
        }

        print(f"\n✅ Ticket Booked Successfully! Your Ticket ID: {ticket_id}\n")

    def view_ticket(self):
        ticket_id = input("Enter your Ticket ID: ")
        if ticket_id in self.tickets:
            print("\n🎟️ Ticket Details:")
            for key, value in self.tickets[ticket_id].items():
                print(f"{key}: {value}")
            print()
        else:
            print("\n❌ Invalid Ticket ID. Please try again.\n")

    def cancel_ticket(self):
        ticket_id = input("Enter your Ticket ID to Cancel: ")
        if ticket_id in self.tickets:
            del self.tickets[ticket_id]
            print("\n🚫 Ticket Cancelled Successfully!\n")
        else:
            print("\n❌ Invalid Ticket ID. Cannot cancel.\n")

    def menu(self):
        while True:
            print("\n✈️  Flight Ticket Booking System")
            print("1. Book a Ticket")
            print("2. View Ticket")
            print("3. Cancel Ticket")
            print("4. Exit")

            choice = input("Enter your choice: ")

            if choice == "1":
                self.book_ticket()
            elif choice == "2":
                self.view_ticket()
            elif choice == "3":
                self.cancel_ticket()
            elif choice == "4":
                print("\nThank you for using the Flight Booking System! ✈️\n")
                break
            else:
                print("\n❌ Invalid Choice. Please try again.\n")

# Run the Flight Booking System
if __name__ == "__main__":
    system = FlightBookingSystem()
    system.menu()
