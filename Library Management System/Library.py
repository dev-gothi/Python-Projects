from semi import Book, Member, Transaction
from datetime import date
import json
import os

class Library:
    def __init__(self):
        self.books = []
        self.members = []
        self.transactions = []


    
    def loaddata(self):
        if os.path.exists("data.json"):
            with open("data.json","r") as f:
                data = json.load(f)

            for b in data["books"]:
                self.books.append(Book.fromdict(b))

            for m in data["members"]:
                self.members.append(Member.fromdict(m))
            
            for t in data["transactions"]:
                self.transactions.append(Transaction.fromdict(t))
        
        else:
            return


    def savedata(self):
        data = {
            "books" :[book.todict() for book in self.books],
            "members" : [member.todict() for member in self.members],
            "transactions" :[tran.todict() for tran in self.transactions]
            
            }  
        with open("data.json","w") as f:
            json.dump(data,f)

            



    
    def addbook(self, bookid, title, author, genre):
        book = Book(bookid, title, author, genre)
        self.books.append(book)
        print(f"Book '{title}' added successfully")

    
    def addmember(self, memberid, name, email):
        member = Member(memberid, name, email)
        self.members.append(member)
        print(f"Member '{name}' added successfully")

    
    def searchbook(self, title):
        for book in self.books :
            if book.title.lower() == title.lower():
                return book

        print(f"Book '{title}' not found")
        return None    
        
    def viewtransactions(self):
        for tran in self.transactions:
            print(tran)    

    def viewbooks(self):
        for book in self.books:
            print(book)
        
    def viewmembers(self):
        for member in self.members:
            print(member)
    
    def findmember(self, memberid):
        for member in self.members:
            if member.memberid == memberid:
                return member
        print(f"Member with ID '{memberid}' not found")
        return None
    
    def findbook(self, bookid):
        for book in self.books:
            if book.bookid ==bookid:
                return book
            
        print(f"Book with ID '{bookid}' not found")
        return None
    
    def issuebook(self,memberid,bookid):

        member = self.findmember(memberid)
        if member is None:
            print("Member not found")
            return
        
        book = self.findbook(bookid)
        if book is None:
            print("Book not found")
            return
        
        if book.isavailable == False:
           print("Book already issued")
           return
        
        if book.isavailable:
            member.borrowedbooks.append(book.bookid)
            book.isavailable = False
            tranid = f"{len(self.transactions)+1:03d}"
            tran  = Transaction(tranid,memberid,bookid)
            self.transactions.append(tran)
            print(f"Book '{book.title}' issued to member '{member.name}' successfully")


    def returnbook(self,memberid,bookid):
        member = self.findmember(memberid)
        if member is None:
            print("Member not found")
            return
        book = self.findbook(bookid)
        if book is None:
            print("Book not found")
            return
        if bookid not in member.borrowedbooks:
            print(f"Book '{book.title}' is not borrowed by member '{member.name}'")
            return
        
        tran = None
        for tran in self.transactions:
            if tran.memberid ==memberid and tran.bookid ==bookid and tran.returndate==None:
                member.borrowedbooks.remove(bookid)
                book.isavailable = True
                tran.returndate = date.today()
                tran.calfine()
                print(f"The Book is returned and fine is '{tran.fine}'")
                return
        print("Book already returned")
        return


            

        
         
        


        
    
        


        