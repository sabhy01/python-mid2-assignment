import src

from src.inventory import add_book, remove_book, list_books
from src.transactions import issue_book, return_book
from src.analytics import most_borrowed_books, visualize_usage
from src.logger import export_logs

# Sample interaction loop
if _name_ == "_main_":
    while True:
        print("""
        === Library Management System ===
        1. Add Book
        2. Remove Book
        3. List Books
        4. Issue Book
        5. Return Book
        6. View Most Borrowed Books
        7. Visualize Usage
        8. Export Logs
        9. Exit
        """)
        choice = input("Enter choice: ")

        if choice == '1':
            title = input("Book Title: ")
            author = input("Author: ")
            add_book(title, author)

        elif choice == '2':
            title = input("Book Title to remove: ")
            remove_book(title)

        elif choice == '3':
            list_books()

        elif choice == '4':
            user = input("User Name: ")
            title = input("Book Title: ")
            issue_book(user, title)

        elif choice == '5':
            user = input("User Name: ")
            title = input("Book Title: ")
            return_book(user, title)

        elif choice == '6':
            most_borrowed_books()

        elif choice == '7':
            visualize_usage()

        elif choice == '8':
            export_logs()

        elif choice == '9':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")