books = ["C programming", "JAVA", "Numerical Method", "Data Structure"]

def show_books():
   print("\nBooks in library are:")
   if len(books) == 0:
      print("No books available in list")
   else:
      for i, b in enumerate(books, 1):
         print(i, b)

def add_book():
   name = input("Enter the book name: ")
   books.append(name)
   print("Book added successfully")

def borrow_book():
   name = input("Enter the book name to borrow: ")
   if name in books:
      books.remove(name)
      print("You have borrowed the book successfully")
   else:
      print("Book not found!")

def return_book():
   name = input("Write name the book to return: ")
   books.append(name)
   print("Book returned successfully")

def main():
   while True:
      print("\n=====Library Management System=====")
      print("1. Show Books")
      print("2. Add Book")
      print("3. Borrow Book")
      print("4. Return Book")
      print("5. Exit")

      choice = input("Enter your choice(1-5): ")
      if choice == "1":
         show_books()
      elif choice == "2":
         add_book()
      elif choice == "3":
         borrow_book()
      elif choice == "4":
         return_book()
      elif choice == "5":
         print("Exiting...")
         break
      else:
         print("Invalid choice. Please try again.")

if __name__ == "__main__":
   main()