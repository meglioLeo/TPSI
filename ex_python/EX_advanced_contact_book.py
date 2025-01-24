class Contact:
    
    contacts = []   #empty list that will store the contacts    
    
    def __init__(self, name, phone_number, email, notes):
        self.name = name     #full name of the contact
        self.phone_number = phone_number  #is composed of 10 digits
        self.email = email 
        self.notes = notes   #additional information about the contact
        Contact.contacts.append(self)   #add the contact to the list of contacts

    def print_contact_info(self):   #print and doesn't return anything
        print(f"Name: {self.name}, Phone Number: {self.phone_number}, Email: {self.email}, Notes: {self.notes}")

    @classmethod     #class method that creates a contact with default values
    def create_contact(cls):
        name = "Mario Rossi"
        phone_number = 0000000000
        email = "mario.rossi@gmail.com"
        notes = ""
        new_contact = cls(name, phone_number, email, notes)
        Contact.contacts.append(new_contact)  #add the default contact to the list of contacts
        return new_contact
    
    def update_notes(self, notes):
        self.notes = notes

    @staticmethod
    def find_contact_by_name(contacts, name):
        for contact in contacts:    #iterate through the list of contacts
            if contact.name == name:
                return contact         #return the contact if it is found
        return None              #return None if the contact is not found
    
contact1 = Contact("John Doe", 1234567890, "john.doe@gmail.com", "")
contact2 = Contact("Jane Doe", 2987654321, "", "Friend")
contact3 = Contact.create_contact()

contact1.print_contact_info()
contact2.print_contact_info()
contact3.print_contact_info()

contact1.update_notes("Family")
contact1.print_contact_info()

Contact.find_contact_by_name(Contact.contacts, "John Doe").print_contact_info()   
#the last print statement is needed because the method returns a contact, so it has to be printed