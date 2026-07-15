import json
import os

class contact_book:
     
    def __init__(self,filename="contacts.json"):
        self.filename = filename
        self.contacts = {}
        self.load_contacts()
    
    def load_contacts(self):

        if os.path.exists(self.filename):
            with open(self.filename, "r") as f:
                self.contacts = json.load(f)
        else:
            self.contacts = {
                "Anis": ["anis@example.com", "123-456-7890"],
                "John": ["john@gmail.com", "987-654-3210"],
                "Ahmad": ["ahmad32@gmail.com", "555-555-5555"],
                "Zakaria": ["zak456@gmail.com", "111-111-1111"],
            "Arif": ["arif789@gmail.com", "333-333-3333"]
        }
        self.save_contacts()
            
    
    def save_contacts(self):
        with open(self.filename, "w") as f:
            json.dump(self.contacts, f,indent=4)
            
    def search_contact(self, name):
        if name in self.contacts:
            return self.contacts[name]
        else:
            return "Contact not found."
        
    def add_contact(self, name, email, phone):
        if name not in self.contacts:
            self.contacts[name]=[email,phone]
            self.save_contacts()

            return f"contact {name} added successfully"
            
        else:
            return "Contact already exists."
         
     
    def delete_contact(self, name):
        if name in self.contacts:
            del self.contacts[name]
            self.save_contacts()
            return f"Contact {name} deleted successfully."
        else:
            return "Contact not found."
        
cont=contact_book()
print(cont.search_contact("Arif"))
print(cont.add_contact("saqib", "saqi@gmail.com", "774-234-4444"))
print(cont.add_contact("Hamza","ham879@gmail.com","999-888-754"))
print(cont.delete_contact("hamza"))

cont.load_contacts()
cont.save_contacts()