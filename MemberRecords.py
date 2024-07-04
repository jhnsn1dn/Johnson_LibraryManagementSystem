# Initialize an empty dictionary to store member records.
member_data = {}


# Function to add a new member record.
def add_member():
    while(True):
        member_id = input("Enter member ID: ")
        if (member_id in member_data):
            print(f"Sorry, this ID ({member_id}) is already in use.");
        if ("L" in member_id):
            print
            continue
        else:
            break;
        
    member_name = input("Enter member name: ")
    
# Storing details inputted above in a dictionary called member_profile
    member_profile = {
        "member id": member_id,
        "name of member": member_name
    }

    member_data[member_id] = member_profile
    print(f"member with name {member_name} and ID {member_id} has been added.")


# Function to check and make sure two members don't share the same ID
def id_checker(checking_id):
    if checking_id in member_data:
        print(f"Sorry, this ID ({checking_id}) is already in use.")
    else:
        pass;

# Function to retrieve a member record by ID.
def retrieve_member_information():
    member_id = input("Enter member ID to retrieve: ")
    if member_id in member_data:
        member = member_data[member_id]
        print("member Information:")
        print(f"member Name: {member['name of member']}")
    else:
        print("member not found.")


# Function to update a member record by ID.
def update_member_information():
    member_id = input("Enter member ID to update: ")
    if member_id in member_data:
        member = member_data[member_id]
        print(f"Updating record for {member['name of member']}:")
        member['name of member'] = input("Enter new member name: ")
        print("Updating member information: ")
    else:
        print("member ID not found.")


# Function to delete member record by ID.
def delete_member_information():
    member_id = input("Enter member ID to delete: ")
    if member_id in member_data:
        member_name = member_data[member_id]['name of member']
        del member_data[member_id]
        print(f"Record for {member_name} has been deleted.")
    else:
        print("member ID not found.")


# Main program loop
while True:
    print("\nmember Management System")
    print("1. Add member Information")
    print("2. Retrieve member Information")
    print("3. Update member Information")
    print("4. Delete member Information")
    print("5. Exit")

    choice = input("Enter member choice (1/2/3/4/5): ")

    if choice == '1':
        add_member()
    elif choice == '2':
        retrieve_member_information()
    elif choice == '3':
        update_member_information()
    elif choice == '4':
        delete_member_information()
    elif choice == '5':
        print("Exiting member Management System. \nGoodbye!")
        break
    else:
        print("Invalid choice. Please select a valid option: (1/2/3/4/5).")

# Member class
class Member:
    def __init__(self, name, member_id):
        self.__name = name
        self.__member_id = member_id
        self.__borrowed_books = []

    # Getters and Setters for the Member class
    def get_name(self):
        return self.__name
    
    def set_name(self, name):
        self.__name = name
    
    def get_member_id(self):
        return self.__member_id
    
    def set_member_id(self, member_id):
        self.__member_id = member_id

    def get_borrowed_books(self):
        return self.__borrowed_books

    def borrow_book(self, book):
        self.__borrowed_books.append(book)
        book.set_borrowed(True)
    
    def return_book(self, book):
        self.__borrowed_books.remove(book)
        book.set_borrowed(False)

# Subclass for different types of members
class Librarian(Member):
    def __init__(self, name, librarian_id):
        super().__init__(name, librarian_id)

class Student(Member):
    def __init__(self, name, member_id):
        super().__init__(name, member_id)

class Teacher(Member):
    def __init__(self, name, teacher_id):
        super().__init__(name, teacher_id)