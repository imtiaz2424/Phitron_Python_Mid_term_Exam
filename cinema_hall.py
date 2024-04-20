class Star_Cinema:
    __hall_list = []

    @classmethod
    def entry_hall(self, hall):
        self.__hall_list.append(hall)

class User:
    def __init__(self, id, name, password):
        self.id = id
        self.name = name
        self.password = password
        self.book_seats = []


class Hall(Star_Cinema):
    def __init__(self, rows, cols, hall_no):
        self.__seats = {}
        self.__show_list = []        
        self.__rows = rows
        self.__cols = cols
        self.__hall_no = hall_no
        self.users = []        
        self.entry_hall(self)   


    def entry_show(self, id, movie_name, time):
        show_info = (id, movie_name, time)
        self.__show_list.append(show_info)
        alloc_seat = [['free' for _ in range (self.__cols)]
                      for _ in range(self.__rows)]
        self.__seats[id] = alloc_seat


    def add_user(self, id, name, password):
        user = User(id, name, password)
        self.users.append(user)
        return user

    
    def book_seats(self, id, seat_list):
        if id not in self.__seats:
             print("\n\tID not found.")
             return
        
        for row, col in seat_list:
            if row >= self.__rows or col >= self.__cols:
                print("\n\tInvalid seat at row {row} and column {col}.")
                return
            if self.__seats[id][row][col] != 'free':
                print(f"\n\tSeat at row {row} and column {col} is already booked.")
                self.__seats[id][row][col] = 'booked'
                return
            else:
                User.book_seats.append(User)                
        print("\n\tSeats booked successfully")       
    
    
    def view_show_list(self):
        return self.__show_list
    
    def view_available_seats(self, id):
        if id not in self.__seats:
            print("\n\tShow ID not found.")
            return        
        available_seats = [(i,j) for i in range(self.__rows)
                           for j in range(self.__cols)
                           if self.__seats[id][i][j] == 'free']
        return available_seats

class Counter:
    def __init__(self, cinema):
        self.__cinema = cinema

    def view_all_shows(self):
        shows = []
        for hall in self.__cinema._Star_Cinema__hall_list:
            shows.extend(hall.view_show_list())
        return shows

    def view_available_seats(self, hall_no, show_id):
        for hall in self.__cinema._Star_Cinema__hall_list:
            if hall._Hall__hall_no == hall_no:
                return hall.view_available_seats(show_id)
        print("\n\tHall not found.")
        return

    def book_tickets(self, hall_no, show_id, seat_list):
        for hall in self.__cinema._Star_Cinema__hall_list:
            if hall._Hall__hall_no == hall_no:
                return hall.book_seats(show_id, seat_list)
        print("\n\tHall not found.")
        return
        

hall_show = Hall(1, "Imto", 2)
admin = hall_show.add_user(1, 'admin', 'admin')
fahim = hall_show.add_user(20, 'Fahim', '1234')
hall_show.book_seats(2, [(0, 0), (0, 1)])

booking = True
current_user = admin

while booking:
    if current_user == None:
        print("\n\tShow ID not found.")
        op1 = input("\n\tLogin or Signup (L/S): ")

        if op1 == 'S':
            id = int(input("\n\tEnter your id: ")) 
            name = input("\n\tEnter your name: ")
            password = input("\n\tEnter your password: ")

            current_user = hall_show.add_user(id, name, password)
        
        elif op1 == 'L':
            id = int(input("\n\tEnter your id: "))            
            password = input("\n\tEnter your password: ")

            not_match = False
            for user in hall_show.users:
                if user.id == id and user.password == password:
                    current_user = user
                    not_match = True
                    break
            
            if not_match == False:
                print("\n\tNo user found !")

    else:
        if current_user.name == 'admin':
            print("Options: \n")
            print("1:  Add seat")
            print("2:  Show Users")
            print("3:  Show Seat")
            print("4:  Logout")

            choice = int(input("\nEnter Options: "))

            if choice == 1:
                id = int(input("\n\tEnter show id: ")) 
                s = input("\n\tEnter your seat (format: row,col): ").split(',')
                seat_list = [(int(s[0]), int(s[1]))] 

                hall_show.book_seats(id, seat_list)
            
            elif choice == 4:
                current_user = None 
                
        else:
            print("Options: \n")
            print("1:  Seat Booking")
            print("2:  No of seat")
            print("3:  Show Seat")
            print("4:  Show Date Booking")
            print("5:  Show Returned Seat")
            print("6:  Logout")

            choice = int(input("\nEnter Option: "))

            if choice == 1:
                id = int(input("\n\tEnter show id: ")) 
                s = input("\n\tEnter your seat (format: row,col): ").split(',')
                seat_list = [(int(s[0]), int(s[1]))] 

                hall_show.book_seats(id, seat_list)

            elif choice == 6:
                current_user = None
