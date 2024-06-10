import random
import string


# class variables
class Ticket:
    totalTicketsCreated = 2000
    pendingTickets = 0
    closedTickets = 0

    # ticket attributes
    def __init__(self, staffID, requesterName, contactEmail, description):
        self.ticketNumber = Ticket.totalTicketsCreated
        Ticket.totalTicketsCreated += 1
        self.staffID = staffID
        self.requesterName = requesterName
        self.contactEmail = contactEmail
        self.description = description
        self.ticketResponse = "Not Yet Provided"
        self.ticketStatus = "Open"
        Ticket.pendingTickets += 1
        self.generatedPassword = None

    # displaying ticket info
    def displayTicket(self):
        print(f"Ticket Number: {self.ticketNumber}")
        print(f"Ticket Creator: {self.requesterName}")
        print(f"Staff ID: {self.staffID}")
        print(f"Email Address: {self.contactEmail}")
        print(f"Description: {self.description}")
        print(f"Response: {self.ticketResponse}")
        if self.generatedPassword:
            print(f"Password: {self.generatedPassword}")
        print(f"Ticket Status: {self.ticketStatus}\n")

    # submitting ticketResponse
    def submitResponse(self, ticketResponse):
        self.ticketResponse = ticketResponse
        self.ticketStatus = "Closed"
        Ticket.pendingTickets -= 1
        Ticket.closedTickets += 1

    # resolving generatedPassword change request and closing ticket
    def resolvePC(self):
        if "generatedPassword change" in self.description.lower(): # checking for lowercase
            newPassword = self.generatePassword()
            self.ticketResponse = f"Password changed to: {newPassword}"
            self.ticketStatus = "Closed"
            Ticket.pendingTickets -= 1
            Ticket.closedTickets += 1
            self.generatedPassword = newPassword

        # generating a new generatedPassword
    def generatePassword(self):
        # extracting the first two characters of staffID and the first three characters of the ticket requesterName
        staffID_chars = self.staffID[:2]
        requesterName_chars = self.requesterName[:3]

        # generating a random 3-character string for additional complexity
        random_chars = ''.join(random.choices(string.ascii_letters, k=3))

        # concatenation
        newPassword = staffID_chars + requesterName_chars + random_chars

        return newPassword

    # reopening closed ticket
    def reopenTicket(self):
        self.ticketStatus = "Reopened"
        Ticket.pendingTickets += 1
        Ticket.closedTickets -= 1

    # displaying ticket statistics
    @classmethod
    def ticket_stats(cls):
        # make sure area below is correct, could be two lines instead of one
        return f"Ticket Created: {cls.totalTicketsCreated - 2000}\nTickets Resolved: {cls.closedTickets}\nTickets To Solve: {cls.pendingTickets}"

# MAIN PROGRAM
def main():
    tickets = []

    while True:
        # Display menu for user interaction
        print("nMenu:")
        print("1. Create Ticket")
        print("2. Resolve Ticket")
        print("3. Change Password (if Password Change Request)")
        print("4. View All Tickets")
        print("5. View Open Tickets")
        print("6. View Closed Tickets")
        print("0. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            requesterName = input("Enter Creator Name: ")
            staffID = input("Enter Staff ID: ")
            contactEmail = input("Enter Email Address: ")

            description = input("Enter Description")

            tickets.append(Ticket(staffID, requesterName, contactEmail, description))
            # make sure this part above is correct
            print("Ticket created successfully.")
        elif choice == "2":
            for i, ticket in enumerate(tickets, start=1):
                print(f"{i}. Ticket Number: {ticket.ticketNumber} (Status: {ticket.ticketStatus})")
            ticket_index = int(input("Enter the index of the ticket to resolve: ")) -1
            # the -1 could be needed one line below where it is, potential error
            if 0 <= ticket_index < len(tickets):
                ticketResponse = input("Enter ticketResponse for the selected ticket: ")
                tickets[ticket_index].submitResponse(ticketResponse)
                print("Ticket resolved successfully.")
            else:
                print("Invalid ticket index.")
        elif choice == "3":
            print("Open Tickets:\n")
            for i, ticket in enumerate(tickets, start=1):
                if ticket.ticketStatus == "Open":
                    print(f"{i}. Ticket Number: {ticket.ticketNumber} (Status: {ticket.ticketStatus})")

            ticket_index = int(input("enter the index of the Password Change Request to change the generatedPassword: ")) - 1

            if 0 <= ticket_index < len(tickets):
                tickets[ticket_index].resolvePC()
                print("Password changed successfully.")
            else:
                print("Invalid ticket index.")
        elif choice == "4":
            print("\nAll Tickets:")
            for ticket in tickets:
                ticket.displayTicket()
            print("\nTicket Statistics:")
            print(Ticket.ticket_stats())
        elif choice == "5":
            print("\nOpen Tickets:\n")
            for ticket in tickets:
                if ticket.ticketStatus == "Open":
                    ticket.displayTicket()
            print("\nTicket Statistics (Before Resolution and Password Change):\n")
            print(Ticket.ticket_stats())
        elif choice == "6":
            print("\nClosed Tickets:\n")
            for ticket in tickets:
                if ticket.ticketStatus == "Closed":
                    ticket.displayTicket()
            print("\nTicket Statistics (Before Resolution and Password Change):\n")
            print(Ticket.ticket_stats())
        elif choice == "0":
            # exit
            print("exiting the program.")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()