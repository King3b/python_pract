on_loan = {
    "The Hobbit": "Blessings",
    "Harry Potter": "John",
    "The Great Gatsby": "Sarah",
    "1984": "Mike",
    "The Alchemist": "David"
}


def check_out(title, user):
    on_loan[title] = user
    return on_loan


def return_book(title):
    if title in on_loan:
        del on_loan[title]
        return f"{title} has been returned."
    else:
        return f"{title} is not currently on loan."


def is_on_loan(title):
    if title in on_loan:
        return True
    else:
        return False


def menu():
    while True:
        print("""
--- LIBRARY MENU ---
1 : Checkout book
2 : Return book
3 : Check if book is on loan
4 : View books on loan
5 : Exit
""")

        opt = input("Select option: ")

        if opt == "1":
            title = input("Enter title: ")
            user = input("Enter user name: ")
            print(check_out(title, user))

        elif opt == "2":
            title = input("Enter title: ")
            print(return_book(title))

        elif opt == "3":
            title = input("Enter title: ")
            print(is_on_loan(title))

        elif opt == "4":
            print(on_loan)

        elif opt == "5":
            print("Goodbye! 👋")
            break

        else:
            print("Invalid option.")

is_on_loan("The Alchemist")

menu()