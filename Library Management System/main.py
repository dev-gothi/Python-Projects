from Library import Library
lib = Library()

lib.loaddata()
while True:
    print("-----------------------------")
    print("1. Add Book")
    print("2. Add Member")
    print("3. Search Books")
    print("4. View All Books")
    print("5. View All Members")
    print("6. Issue Book")
    print("7. Return Book")
    print("8. View All Transactions")
    print("9. Exit")

    choice = input("Enter your choice: ")
    if choice == "1":
        bookid = input("Enter Book ID: ")
        title = input("Enter Book Title: ")
        author = input("Enter Book Author: ")
        genre = input("Enter Book Genre: ")
        lib.addbook(bookid, title, author, genre)
        lib.savedata()
    elif choice == "2":
        memberid = input("Enter Member Id :")
        name = input("Enter Name :")
        email = input("Enter Email :")
        lib.addmember(memberid, name, email)
        lib.savedata()
    elif choice == "3":
        title = input("Enter Book to be Searched :")
        lib.searchbook(title)
        
    elif choice == "4":
        lib.viewbooks()

    elif choice == "5":
        lib.viewmembers()
    elif choice == "6":
        memberid = input("Enter Member ID: ")
        bookid = input("Enter Book ID: ")
        lib.issuebook(memberid, bookid)
        lib.savedata()
    
    elif choice == "7":
        memberid = input("Enter Member ID: ")
        bookid = input("Enter Book ID: ")
        lib.returnbook(memberid, bookid)
        lib.savedata()
    elif choice == "8":
        lib.viewtransactions()
    elif choice == "9":
        print("Thank You for using DG Library System")
        break
    else:
        print("Please Enter Valid Choice")