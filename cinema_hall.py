from abc import ABC

# This is user class part

class User(ABC):
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone               

# This is Star Cinema part

class Star_Cinema:
    def __init__(self, name):
        self._name = name
        self._hall_list = []
        self._admin_list = []        

    def viewer_email(self, email):
        return self._seats.get(email, None)
      
    def entry_hall(self, hall):
        if isinstance(hall, Hall):
            self._hall_list.append(hall)
        elif isinstance(hall, Admin):
            self._admin_list.append(hall)
        

    def get_hall_list(self):
        return self._hall_list
      
# This is Hall part

class Hall:
    def __init__(self, name, rows, cols, hall_no):
        self._name = name      
        self._seats = {}
        self._show_list = []
        self._rows = rows        
        self._cols = cols        
        self._hall_no = hall_no                      
    
    def entry_show(self, id, movie_name, time):        
        self._show_list.append((id, movie_name, time))
        self._seats[id] = [['free' for _ in range(self._cols)]
                            for _ in range(self._rows)]
    
    def book_seats(self, id, seat_list):
        if id not in self._seats:
            print("Invalid show id")
            return
        for row, col in seat_list:
            if row >= self._rows or col >= self._cols:
                print("Invalid seat number")
                continue
            if self._seats[id][row][col] == 'booked':
                print("Seat already booked")
                continue
            self._seats[id][row][col] = 'booked'
                        
    def view_show_list(self):
        return self._show_list

    def view_available_seats(self, id):
        if id not in self._seats:
            print("Invalid show id")
            return
        return [[col for col, val in enumerate(row)
                 if val == 'free'] for row in self._seats[id]]

# This is Admin part

class Admin(User):
    def __init__(self, name, email, phone, cinema):
        super().__init__(name, email, phone)
        self.cinema = cinema
    
    def get_hall_by_name(self, hall_name):
        for hall in self.cinema._hall_list:
            if hall._name == hall_name:
                return hall
        return None

    def view_show_list(self, hall_name):
        hall = self.get_hall_by_name(hall_name)
        if hall is not None:
            return hall.view_show_list()
        else:
            print("Hall not found")

    def view_available_seats(self, hall_name, show_id):
        hall = self.get_hall_by_name(hall_name)
        if hall is not None:
            return hall.view_available_seats(show_id)
        else:
            print("Hall not found")

    def delete_viewer(self, hall_name, email):
        hall = self.get_hall_by_name(hall_name)
        if hall is not None and email in hall._seats:
            del hall._seats[email]
        else:
            print("Hall or viewer not found")


# This is Main part
cinema_proj = Star_Cinema("Star Cinema Hall")

def counter():
    name = input("Enter Your Name: ")
    email = input("Enter Your Email : ")
    phone = input("Enter Your Phone : ")   
    rows = int(input("Enter number of rows: "))
    cols = int(input("Enter number of columns: "))
    hall_no = input("Enter hall number: ")
    viewer_hall = Hall(name, rows, cols, hall_no)
    cinema_proj.entry_hall(viewer_hall)
        
    while True:
        print(f"Welcome {viewer_hall._name}!!")
        print("1. Entry")
        print("2. View all shows")
        print("3. View available seats in a show")       
        print("4. Book tickets in a show")               
        print("5. Exit")    
        
        choice = int(input("Enter Your Choice : "))
        if choice == 1:
            id = input("Enter show id: ")
            movie_name = input("Enter movie name: ")
            time = input("Enter show time: ")
            viewer_hall.entry_show(id, movie_name, time) 
        elif choice == 2:
            for hall in cinema_proj._hall_list:
                print("Hall No: ", hall._hall_no)
                print("Show list: ", hall.view_show_list())
        elif choice == 3:
            hall_no = input("Enter hall number: ")
            id = input("Enter show id: ")
            for hall in cinema_proj._hall_list:
                if hall._hall_no == hall_no:
                    print("Available seats: ", hall.view_available_seats(id))                  
        elif choice == 4:
            hall_no = input("Enter hall number: ")
            id = input("Enter show id: ")
            seat_list = [tuple(map(int, input("Enter row and column of seat: ").split(',')))
                         for _ in range(int(input("Enter number of seats to book: ")))]
            for hall in cinema_proj._hall_list:
                if hall._hall_no == hall_no:
                    hall.book_seats(id, seat_list)                                  
        elif choice == 5:            
            break
        else:
            print("Invalid Input")

# This is the main admin part

def admin():
    name = input("Enter Your Name : ")
    email = input("Enter Your Email : ")
    phone = input("Enter Your Phone : ")       
    admin = Admin(name, email, phone, cinema_proj)
    cinema_proj.entry_hall(admin)
    
    while True:
        print(f"Welcome {admin.name}!!")
        print("1. Show list")
        print("2. Available seats")               
        print("3. Delete viewer")               
        print("4. Exit")
        
        choice = int(input("Enter Your Choice : "))                   
        if choice == 1:
            hall = input("Enter hall name: ")            
            print("List of show: ", admin.view_show_list(hall))
        elif choice == 2:
            hall = input("Enter hall name: ")
            show_id = input("Enter show id: ")
            print("Total available seats is: ", admin.view_available_seats(hall, show_id))
        elif choice == 3:
            hall = input("Enter hall name: ")            
            viewer_email = input("Enter viewer email to delete: ")
            admin.delete_viewer(hall, viewer_email)       
        elif choice == 4:
            break
        else:
            print("Invalid Input")            

# This is user and admin front part
while True:
    print("Welcome to Star Cinema Hall!!")
    print("1. User")   
    print("2. Admin")   
    print("3. Exit")
    choice = int(input("Enter your choice : "))
    if choice == 1:
        counter()    
    if choice == 2:
        admin()    
    elif choice == 3:
        break
    else:
        print("Invalid Input!!")
