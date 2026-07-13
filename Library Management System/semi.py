import datetime

class Book:
    def __init__(self,bookid, title, author,genre):
        self.bookid = bookid
        self.title = title
        self.author = author
        self.genre = genre
        self.isavailable = True
    
    def __str__(self):
        # f" to return the string representation 
        return f"Book ID : {self.bookid} | Title: {self.title} | Author: {self.author} | Genre: {self.genre}"
    
    def todict(self):
        #This method converts book to dictionary format
        return {
            "bookid": self.bookid,
            "title": self.title,
            "author": self.author,
            "genre": self.genre,
            "isavailable": self.isavailable
        }
    @classmethod
    def fromdict(cls, data):
        #This method converts dictionary to book object
       book = cls(data["bookid"], data["title"],data["author"],data["genre"])
       book.isavailable = data["isavailable"]
       return book
    

class Member:
    def __init__(self,memberid,name,email):
        self.memberid = memberid
        self.name = name
        self.email = email
        self.borrowedbooks = []
    
    def __str__(self):
        # f" to return the string representation 
        return f"Member ID : {self.memberid} | Name : {self.name} | Email : {self.email} | Borrowed Books : {len(self.borrowedbooks)}"
    
    def todict(self):
        #This method converts member to dictionary format
        return {
            "memberid": self.memberid,
            "name": self.name,
            "email": self.email,
            "borrowedbooks": self.borrowedbooks
        }

    @classmethod
    def fromdict(cls, data):
        #This method converts dictionary to member object
        member = cls(data["memberid"], data["name"],data["email"])
        member.borrowedbooks = data["borrowedbooks"]
        return member

       
    
class Transaction:

    def __init__(self,tranid,memberid,bookid):
        self.tranid = tranid
        self.memberid = memberid
        self.bookid = bookid
        self.issuedate = datetime.date.today()
        self.duedate = self.issuedate + datetime.timedelta(days=14)
        self.returndate = None
        self.fine = 0.0

    def __str__(self):
        return f"Transaction ID :{self.tranid} | Member ID : {self.memberid} | Book ID : {self.bookid} | Issue Date : {self.issuedate} | Due Date : {self.duedate} | Return Date : {self.returndate} | Fine : {self.fine}"
    

    def calfine(self):
        if self.returndate is None:
            return
        
        if self.returndate > self.duedate:
            late = (self.returndate - self.duedate).days
            self.fine = late * 1.0
        
        else:
            self.fine = 0.0

    
    def todict(self):
        #This method converts transaction to dictionary format
        return {
            "tranid" : self.tranid,
            "memberid" : self.memberid,
            "bookid" : self.bookid,
            "issuedate": str(self.issuedate),
            "duedate": str(self.duedate),
            "returndate": str(self.returndate) if self.returndate else None,    
            "fine": self.fine
        }

    @classmethod
    def fromdict(cls, data):
        #This method converts dictionary to transaction object
        tran = cls(data["tranid"],data["memberid"],data["bookid"])
        tran.issuedate = datetime.date.fromisoformat(data["issuedate"])

        tran.duedate = datetime.date.fromisoformat(data["duedate"])

        tran.returndate = datetime.date.fromisoformat(data["returndate"]) if data["returndate"] else None

        tran.fine = data["fine"]
        return tran
    

    

