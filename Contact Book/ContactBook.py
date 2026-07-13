import json
import os


class ContactBook:
    contacts = {}


    def __init__(self):
        self.main()
    
    def main(self):
        self.load_contacts()

        while True:
            print(""" 
                        --------------Contact Book----------------
                        1. Add Contacts
                        2. View all Contacts
                        3. Search Contacts
                        4. Update Contacts
                        5. Delete Contacts
                        6. Exit
            
            
            """)
            
            choice = input("Enter Choice : ")
            if choice == "1":
                self.add_contact()
            elif choice == "2":
                self.view_contacts()
            elif choice == "3":
                self.search_contact()
            elif choice == "4":
                self.update_contact()
            elif choice == "5":
                self.delete_contact()
            elif choice == "6":
                print("Goodbye!")
                break
            else:
                print("Invalid choice. Please try again")


    def load_contacts(self):
        if os.path.exists("contacts.json"):
            with open("contacts.json","r") as f:
                self.contacts = json.load(f)
        else:
            self.contacts = {}

    def save_contacts(self):
        with open("contacts.json", "w") as f:
            json.dump(self.contacts,f)

    def add_contact(self):
        name = input("Enter the Name : ")
        phone = input("Enter the Phone Number : ")
        email = input("Enter the Email Address : ")
        if name in self.contacts:
            print("Contact already exists")
        else:
            self.contacts[name] = {"Phone": phone, "Email": email}
            self.save_contacts()
            print("Contact added successfully")
    
    def view_contacts(self):
        for name,details in self.contacts.items():
             print("Name  :", name)
             print("Phone :", details["Phone"])
             print("Email :", details["Email"])
             print("----------------------------")


    def search_contact(self):
        name = input("Enter the Name to search: ")
        if name in self.contacts:
            details = self.contacts[name]
            print("Name  :", name)
            print("Phone :", details["Phone"])  
            print("Email :", details["Email"])
            print("----------------------------")
        else:
            print("Contact not found.")
        
    def update_contact(self):
        name = input("Enter the Name to update: ")
        if name in self.contacts:
            phone = input("Enter new phone number: ")
            email = input("Enter new email address: ")
            self.contacts[name] = {"Phone": phone, "Email": email}
            self.save_contacts()
            print("Contact updated successfully.")
        
        else:
            print("Contact not found.")
    

    def delete_contact(self):
        name = input("Enter the Name to delete: ")
        if name in self.contacts:
            del self.contacts[name]
            self.save_contacts()
            print("Contact deleted successfully.")
        else:
            print("Contact not found.")
        
    
            
cb = ContactBook()




            
                         

    
    
    
        
    
