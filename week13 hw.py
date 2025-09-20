import datetime


# Search, Borrow, Return: Book does not exist in inventory
class BookNotAvailableError(Exception):
    def __init__(self, book_name):
        self.book_name=book_name
    def __str__(self):
        return f"{self.book_name} is not available in the library."

# Search, Borrow: Book stock is 0
class InsufficientBookError(Exception):
    def __init__(self, book_name):
        self.book_name=book_name
    def __str__(self):
        return f"No copies of {self.book_name} left."

# Borrow: User has reached the borrow limit
class BorrowLimitError(Exception):
    def __init__(self, user_name, borrow_limit):
        self.user_name=user_name
        self.borrow_limit=borrow_limit
    def __str__(self):
        return f"{self.user_name} has reached the borrow limit of {self.borrow_limit} books."   #不同身分有不同上限

# Return: User did not borrow the book
class DidNotBorrowError(Exception):
    def __init__(self, user_name, book_name):
        self.user_name=user_name
        self.book_name=book_name
    def __str__(self):
        return f"{self.user_name} did not borrow {self.book_name}."

# Apply_LAB, Apply_Conference: Non-Grad/Professor attempts to apply
class NotAllowedError(Exception):
    def __init__(self, user_name, room_type):
        self.user_name=user_name
        self.room_type=room_type
    def __str__(self):
        return f"{self.user_name} is not allowed to reserve {self.room_type}."

# Apply_LAB, Apply_Conference: Attempting to apply for already booked resource
class AlreadyBookedError(Exception):
    def __init__(self, room_type, room_id, date):
        self.room_type=room_type
        self.room_id=room_id
        self.date=date
    def __str__(self):
        return f"{self.room_type} {self.room_id} is already booked on {self.date}."




class UndergraduateStudent:
    def __init__(self, name):      #當建立物件時，不需從外部傳入books_borrowed
        self.name=name
        self.books_borrowed=[]      #__init__: 只會在建立新的學生物件時執行一次
    
    def borrowBook(self, book_borrowed):
        self.books_borrowed.append(book_borrowed)
        self.books_borrowed=sorted(self.books_borrowed)
    
    def returnBook(self, book_returned):
        self.books_borrowed.remove(book_returned)
        self.books_borrowed=sorted(self.books_borrowed)
    
class GraduateStudent(UndergraduateStudent):
    def __init__(self, name):
        UndergraduateStudent.__init__(self, name)
        self.lab={}
    
    def applyLab(self, date, lab_id):
        self.lab[date]=lab_id
        self.lab=dict(sorted(self.lab.items()))

class Professor(GraduateStudent):
    def __init__(self, name):
        GraduateStudent.__init__(self, name)
        self.conf={}

    def applyConference(self, date, conf_id):
        self.conf[date]=conf_id
        self.conf=dict(sorted(self.conf.items()))




if __name__=="__main__":
    Inventory_List=input().split(" ")   #[PythonBasics,2,DataStructures,5]
    Length=len(Inventory_List)
    Inventory_Dict={}
    while len(Inventory_List)>=2:
        # print(Dict_Inventory)
        Inventory_Dict[Inventory_List[0]]=int(Inventory_List[1])
        Inventory_List.pop(0)
        Inventory_List.pop(0)
    # print(Dict_Inventory)
    # PythonBasics 2 DataStructures 5 MachineLearning 3
    Inventory_Dict=dict(sorted(Inventory_Dict.items()))   #items(): dict轉list，{'a': 1, 'b': 2} into [('a', 1), ('b', 2)]

    labA_reserve=[]
    labB_reserve=[]
    labC_reserve=[]
    labD_reserve=[]
    labE_reserve=[]
    lab={"LabA": labA_reserve, "LabB": labB_reserve, "LabC": labC_reserve, "LabD": labD_reserve, "LabE": labE_reserve}
    
    roomA_reserve=[]
    roomB_reserve=[]
    roomC_reserve=[]
    roomD_reserve=[]
    roomE_reserve=[]
    conf={"RoomA": roomA_reserve, "RoomB": roomB_reserve, "RoomC": roomC_reserve, "RoomD": roomD_reserve, "RoomE": roomE_reserve}
    
    Users={}
    while True:
        Input_List=input().split(" ")
        Command=Input_List[0]
        if Command=="EXIT":
            break


        elif Command=="CREATE_USER":
            User_Type=Input_List[1]
            User=Input_List[2]
            if User_Type=="U":
                s=UndergraduateStudent(User)
            if User_Type=="G":
                s=GraduateStudent(User)
            if User_Type=="P":
                s=Professor(User)
            Users[User]=s


        elif Command=="SEARCH":
            BookSearching=Input_List[1]
            try:
                if BookSearching not in Inventory_Dict:
                    raise BookNotAvailableError(BookSearching)
                
                CopiesLeft=int(Inventory_Dict[BookSearching])
                if CopiesLeft==0:
                    raise InsufficientBookError(BookSearching)

                print(f"{BookSearching} has {CopiesLeft} copies left.")

            except (BookNotAvailableError, InsufficientBookError) as ErrorMsg:
                print(ErrorMsg)


        elif Command=="BORROW":
            User=Input_List[1]
            BookBorrowing=Input_List[2]
            s=Users.get(User)  #
            try:
                if BookBorrowing not in Inventory_Dict:
                    raise BookNotAvailableError(BookBorrowing)
                
                CopiesLeft=int(Inventory_Dict[BookBorrowing])
                if CopiesLeft==0:
                    raise InsufficientBookError(BookBorrowing)
                
                if type(s)==UndergraduateStudent:  #
                    NumBooks=len(s.books_borrowed)
                    if NumBooks==5:
                        raise BorrowLimitError(User, "5")
                if type(s)==GraduateStudent:  #
                    NumBooks=len(s.books_borrowed)
                    if NumBooks==8:
                        raise BorrowLimitError(User, "8")                   
                if type(s)==Professor:  #
                    NumBooks=len(s.books_borrowed)
                    if NumBooks==10:
                        raise BorrowLimitError(User, "10")
                                    
                s.borrowBook(BookBorrowing)
                Inventory_Dict[BookBorrowing]-=1

            except (BookNotAvailableError, InsufficientBookError, BorrowLimitError) as ErrorMsg:
                print(ErrorMsg)


        elif Command=="RETURN":
            User=Input_List[1]
            BookReturning=Input_List[2]
            s=Users.get(User)  #
            try:
                if BookReturning not in Inventory_Dict:
                    raise BookNotAvailableError(BookReturning)

                if BookReturning not in s.books_borrowed:
                    raise DidNotBorrowError(User, BookReturning)                

                s.returnBook(BookReturning)
                Inventory_Dict[BookReturning]+=1

            except(DidNotBorrowError, BookNotAvailableError) as ErrorMsg:
                print(ErrorMsg)


        elif Command=="APPLY_LAB":
            User=Input_List[1]
            Date=Input_List[2]
            Lab_Name=Input_List[3]
            Lab_ID=Input_List[3][-1]
            s=Users.get(User)  #
            try:
                if type(s)==UndergraduateStudent:
                    raise NotAllowedError(User, "labs")

                if Lab_ID=="A":
                    if Date in labA_reserve:
                        raise AlreadyBookedError("Lab", Lab_Name, Date)
                    labA_reserve.append(Date)

                if Lab_ID=="B":
                    if Date in labB_reserve:
                        raise AlreadyBookedError("Lab", Lab_Name, Date)
                    labB_reserve.append(Date)

                if Lab_ID=="C":
                    if Date in labC_reserve:
                        raise AlreadyBookedError("Lab", Lab_Name, Date)
                    labC_reserve.append(Date)

                if Lab_ID=="D":
                    if Date in labD_reserve:
                        raise AlreadyBookedError("Lab", Lab_Name, Date)
                    labD_reserve.append(Date)
                    
                if Lab_ID=="E":
                    if Date in labE_reserve:
                        raise AlreadyBookedError("Lab", Lab_Name, Date)
                    labE_reserve.append(Date)

                s.applyLab(Date, Lab_Name)
            
            except (NotAllowedError, AlreadyBookedError) as ErrorMsg:
                print(ErrorMsg)


        elif Command=="APPLY_CONFERENCE":
            User=Input_List[1]
            Date=Input_List[2]
            Room_Name=Input_List[3]
            Room_ID=Input_List[3][-1]
            s=Users.get(User)  #
            try:
                if type(s)==UndergraduateStudent or type(s)==GraduateStudent:
                    raise NotAllowedError(User, "conference rooms")
                
                if Room_ID=="A":
                    if Date in roomA_reserve:
                        raise AlreadyBookedError("Conference Room", Room_Name, Date)
                    roomA_reserve.append(Date)

                if Room_ID=="B":
                    if Date in roomB_reserve:
                        raise AlreadyBookedError("Conference Room", Room_Name, Date)
                    roomB_reserve.append(Date)

                if Room_ID=="C":
                    if Date in roomC_reserve:
                        raise AlreadyBookedError("Conference Room", Room_Name, Date)
                    roomC_reserve.append(Date)

                if Room_ID=="D":
                    if Date in roomD_reserve:
                        raise AlreadyBookedError("Conference Room", Room_Name, Date)
                    roomD_reserve.append(Date)

                if Room_ID=="E":
                    if Date in roomE_reserve:
                        raise AlreadyBookedError("Conference Room", Room_Name, Date)
                    roomE_reserve.append(Date)

                s.applyConference(Date, Room_Name)

            except (NotAllowedError, AlreadyBookedError) as ErrorMsg:
                print(ErrorMsg)


        elif Command=="SHOW":
            User=Input_List[1]
            s=Users.get(User)  #
            print("")
            print(f"--- {User}'s Status ---")
            print(f"Borrowed Books: {s.books_borrowed}")
            if type(s)==GraduateStudent:
                print(f"Reserved Labs: {s.lab}")

            if type(s)==Professor:
                print(f"Reserved Labs: {s.lab}")
                print(f"Reserved Conferences: {s.conf}")   

            print("")


#-----------------------------------------------------------
# debug
    # isinstance: s是這個類別或其父類別的實例嗎？
        # if isinstance(s, GraduateStudent):
        # s是GraduateStudent，同時也是UnderGraduateStudent
        # 身分會出錯，因此要使用type(s)==GraduateStudent

    # type(s)函式：
        # type(s) 的意思是「s的型別」
        # e.g. type(s)==UndergraduateStudent

#-----------------------------------------------------------
#'A'

# import datetime


# # Search, Borrow, Return: Book does not exist in inventory
# class BookNotAvailableError(Exception):
#     def __init__(self, book_name):
#         self.book_name=book_name
#     def __str__(self):
#         return f"{self.book_name} is not available in the library."

# # Search, Borrow: Book stock is 0
# class InsufficientBookError(Exception):
#     def __init__(self, book_name):
#         self.book_name=book_name
#     def __str__(self):
#         return f"No copies of {self.book_name} left."

# class BorrowLimitError(Exception):
#     def __init__(self, user_name, borrow_limit):
#         self.user_name=user_name
#         self.borrow_limit=borrow_limit
#     def __str__(self):
#         return f"{self.user_name} has reached the borrow limit of {self.borrow_limit} books."   #不同身分有不同上限

# # Return: User did not borrow the book
# class DidNotBorrowError(Exception):
#     def __init__(self, user_name, book_name):
#         self.user_name=user_name
#         self.book_name=book_name
#     def __str__(self):
#         return f"{self.user_name} did not borrow {self.book_name}."

# # Apply_LAB, Apply_Conference: Non-Grad/Professor attempts to apply
# class NotAllowedError(Exception):
#     def __init__(self, user_name, room_type):
#         self.user_name=user_name
#         self.room_type=room_type
#     def __str__(self):
#         return f"{self.user_name} is not allowed to reserve {self.room_type}."

# # Apply_LAB, Apply_Conference: Attempting to apply for already booked resource
# class AlreadyBookedError(Exception):
#     def __init__(self, room_type, room_id, date):
#         self.room_type=room_type
#         self.room_id=room_id
#         self.date=date
#     def __str__(self):
#         return f"{self.room_type} {self.room_id} is already booked on {self.date}."




# class UndergraduateStudent:
#     def __init__(self, name):      #當建立物件時，不需從外部傳入books_borrowed
#         self.name=name
#         self.books_borrowed=[]      #__init__: 只會在建立新的學生物件時執行一次
    
#     def borrowBook(self, book_borrowed):
#         self.books_borrowed.append(book_borrowed)
#         self.books_borrowed=sorted(self.books_borrowed)
    
#     def returnBook(self, book_returned):
#         self.books_borrowed.remove(book_returned)
#         self.books_borrowed=sorted(self.books_borrowed)
    
# class GraduateStudent(UndergraduateStudent):
#     def __init__(self, name):
#         UndergraduateStudent.__init__(self, name)
#         self.lab={}
    
#     def applyLab(self, date, lab_id):
#         self.lab[date]=lab_id
#         self.lab=dict(sorted(self.lab.items()))

# class Professor(GraduateStudent):
#     def __init__(self, name):
#         GraduateStudent.__init__(self, name)
#         self.conf={}

#     def applyConference(self, date, conf_id):
#         self.conf[date]=conf_id
#         self.conf=dict(sorted(self.conf.items()))




# if __name__=="__main__":
#     Inventory_List=input().split(" ")   #[PythonBasics,2,DataStructures,5]
#     Length=len(Inventory_List)
#     Inventory_Dict={}
#     while len(Inventory_List)>=2:
#         # print(Dict_Inventory)
#         Inventory_Dict[Inventory_List[0]]=int(Inventory_List[1])
#         Inventory_List.pop(0)
#         Inventory_List.pop(0)
#     # print(Dict_Inventory)
#     # PythonBasics 2 DataStructures 5 MachineLearning 3
#     Inventory_Dict=dict(sorted(Inventory_Dict.items()))   #items(): dict轉list，{'a': 1, 'b': 2} into [('a', 1), ('b', 2)]

#     labA_reserve=[]
#     labB_reserve=[]
#     labC_reserve=[]
#     labD_reserve=[]
#     labE_reserve=[]
#     lab={"LabA": labA_reserve, "LabB": labB_reserve, "LabC": labC_reserve, "LabD": labD_reserve, "LabE": labE_reserve}
    
#     roomA_reserve=[]
#     roomB_reserve=[]
#     roomC_reserve=[]
#     roomD_reserve=[]
#     roomE_reserve=[]
#     conf={"RoomA": roomA_reserve, "RoomB": roomB_reserve, "RoomC": roomC_reserve, "RoomD": roomD_reserve, "RoomE": roomE_reserve}
    
#     Users={}
#     while True:
#         Input_List=input().split(" ")
#         Command=Input_List[0]
#         if Command=="EXIT":
#             break


#         elif Command=="CREATE_USER":
#             User_Type=Input_List[1]
#             User=Input_List[2]
#             if User_Type=="U":
#                 s=UndergraduateStudent(User)
#             if User_Type=="G":
#                 s=GraduateStudent(User)
#             if User_Type=="P":
#                 s=Professor(User)
#             Users[User]=s


#         elif Command=="SEARCH":
#             BookSearching=Input_List[1]
#             try:
#                 if BookSearching not in Inventory_Dict:
#                     raise BookNotAvailableError(BookSearching)
                
#                 CopiesLeft=int(Inventory_Dict[BookSearching])
#                 if CopiesLeft==0:
#                     raise InsufficientBookError(BookSearching)

#                 print(f"{BookSearching} has {CopiesLeft} copies left.")

#             except (BookNotAvailableError, InsufficientBookError) as ErrorMsg:
#                 print(ErrorMsg)


#         elif Command=="BORROW":
#             User=Input_List[1]
#             BookBorrowing=Input_List[2]
#             s=Users.get(User)  #
#             try:
#                 if BookBorrowing not in Inventory_Dict:
#                     raise BookNotAvailableError(BookBorrowing)
                
#                 CopiesLeft=int(Inventory_Dict[BookBorrowing])
#                 if CopiesLeft==0:
#                     raise InsufficientBookError(BookBorrowing)
                
#                 if type(s)==UndergraduateStudent:  #
#                     NumBooks=len(s.books_borrowed)
#                     if NumBooks==5:
#                         raise BorrowLimitError(User, "5")
#                 if type(s)==GraduateStudent:  #
#                     NumBooks=len(s.books_borrowed)
#                     if NumBooks==8:
#                         raise BorrowLimitError(User, "8")                   
#                 if type(s)==Professor:  #
#                     NumBooks=len(s.books_borrowed)
#                     if NumBooks==10:
#                         raise BorrowLimitError(User, "10")
                                    
#                 s.borrowBook(BookBorrowing)
#                 Inventory_Dict[BookBorrowing]-=1

#             except (BookNotAvailableError, InsufficientBookError, BorrowLimitError) as ErrorMsg:
#                 print(ErrorMsg)


#         elif Command=="RETURN":
#             User=Input_List[1]
#             BookReturning=Input_List[2]
#             s=Users.get(User)  #
#             try:
#                 if BookReturning not in Inventory_Dict:
#                     raise BookNotAvailableError(BookReturning)

#                 if BookReturning not in s.books_borrowed:
#                     raise DidNotBorrowError(User, BookReturning)

#                 s.returnBook(BookReturning)
#                 Inventory_Dict[BookReturning]+=1

#             except(DidNotBorrowError, BookNotAvailableError) as ErrorMsg:
#                 print(ErrorMsg)


#         elif Command=="APPLY_LAB":
#             User=Input_List[1]
#             Date=Input_List[2]
#             Lab_ID=Input_List[3][-1]
#             s=Users.get(User)  #
#             try:
#                 if type(s)==UndergraduateStudent:
#                     raise NotAllowedError(User, "labs")

#                 if Lab_ID=="A":
#                     if Date in labA_reserve:
#                         raise AlreadyBookedError("Lab", Lab_ID, Date)
#                     labA_reserve.append(Date)

#                 if Lab_ID=="B":
#                     if Date in labB_reserve:
#                         raise AlreadyBookedError("Lab", Lab_ID, Date)
#                     labB_reserve.append(Date)

#                 if Lab_ID=="C":
#                     if Date in labC_reserve:
#                         raise AlreadyBookedError("Lab", Lab_ID, Date)
#                     labC_reserve.append(Date)

#                 if Lab_ID=="D":
#                     if Date in labD_reserve:
#                         raise AlreadyBookedError("Lab", Lab_ID, Date)
#                     labD_reserve.append(Date)
                    
#                 if Lab_ID=="E":
#                     if Date in labE_reserve:
#                         raise AlreadyBookedError("Lab", Lab_ID, Date)
#                     labE_reserve.append(Date)

#                 s.applyLab(Date, Lab_ID)
            
#             except (NotAllowedError, AlreadyBookedError) as ErrorMsg:
#                 print(ErrorMsg)


#         elif Command=="APPLY_CONFERENCE":
#             User=Input_List[1]
#             Date=Input_List[2]
#             Room_ID=Input_List[3][-1]
#             s=Users.get(User)  #
#             try:
#                 if type(s)==UndergraduateStudent or type(s)==GraduateStudent:
#                     raise NotAllowedError(User, "conference rooms")
                
#                 if Room_ID=="A":
#                     if Date in roomA_reserve:
#                         raise AlreadyBookedError("Conference Room", Room_ID, Date)
#                     roomA_reserve.append(Date)

#                 if Room_ID=="B":
#                     if Date in roomB_reserve:
#                         raise AlreadyBookedError("Conference Room", Room_ID, Date)
#                     roomB_reserve.append(Date)

#                 if Room_ID=="C":
#                     if Date in roomC_reserve:
#                         raise AlreadyBookedError("Conference Room", Room_ID, Date)
#                     roomC_reserve.append(Date)

#                 if Room_ID=="D":
#                     if Date in roomD_reserve:
#                         raise AlreadyBookedError("Conference Room", Room_ID, Date)
#                     roomD_reserve.append(Date)

#                 if Room_ID=="E":
#                     if Date in roomE_reserve:
#                         raise AlreadyBookedError("Conference Room", Room_ID, Date)
#                     roomE_reserve.append(Date)

#                 s.applyConference(Date, Room_ID)

#             except (NotAllowedError, AlreadyBookedError) as ErrorMsg:
#                 print(ErrorMsg)


#         elif Command=="SHOW":
#             User=Input_List[1]
#             s=Users.get(User)  #
#             print("")
#             print(f"---{User}'s Status---")
#             print(f"Borrowed Books: {s.books_borrowed}")
#             if type(s)==GraduateStudent:
#                 print(f"Reserved Labs: {s.lab}")

#             if type(s)==Professor:
#                 print(f"Reserved Labs: {s.lab}")
#                 print(f"Reserved Conferences: {s.conf}")   

#             print("")



#-----------------------------------------------------------
# 好耶可以跑

# # Search, Borrow, Return: Book does not exist in inventory
# class BookNotAvailableError(Exception):
#     def __init__(self, book_name):
#         self.book_name=book_name
#     def __str__(self):
#         return f"{self.book_name} is not available in the library."

# # Search, Borrow: Book stock is 0
# class InsufficientBookError(Exception):
#     def __init__(self, book_name):
#         self.book_name=book_name
#     def __str__(self):
#         return f"No copies of {self.book_name} left."

# # Borrow: User has reached the borrow limit
# class BorrowLimitError(Exception):
#     def __init__(self, name):
#         self.name=name
#     def __str__(self):
#         return f"{self.name} has reached the borrow limit of 5 books."

# # Return: User did not borrow the book
# class DidNotBorrowError(Exception):
#     def __init__(self, name, book_name):
#         self.name=name
#         self.book_name=book_name
#     def __str__(self):
#         return f"{self.name} did not borrow {self.book_name}."



# class UndergraduateStudent:
#     def __init__(self, name):      #當建立物件時，不需從外部傳入books_borrowed
#         self.name=name
#         self.books_borrowed=[]      #__init__: 只會在建立新的學生物件時執行一次
    
#     def borrowBook(self, book_borrowed):
#         self.books_borrowed.append(book_borrowed)
#         self.books_borrowed=sorted(self.books_borrowed)
    
#     def returnBook(self, book_returned):
#         self.books_borrowed.remove(book_returned)
#         self.books_borrowed=sorted(self.books_borrowed)



# if __name__=="__main__":
#     List_Inventory=input().split(" ")   #[PythonBasics,2,DataStructures,5]
#     Length=len(List_Inventory)
#     Dict_Inventory={}
#     while len(List_Inventory)>=2:
#         # print(Dict_Inventory)
#         Dict_Inventory[List_Inventory[0]]=int(List_Inventory[1])
#         List_Inventory.pop(0)
#         List_Inventory.pop(0)
#     # print(Dict_Inventory)
#     # PythonBasics 2 DataStructures 5 MachineLearning 3
#     Dict_Inventory=dict(sorted(Dict_Inventory.items()))   #items(): dict轉list，{'a': 1, 'b': 2} into [('a', 1), ('b', 2)]

#     Users={}
#     while True:
#         List_Input=input().split(" ")
#         Command=List_Input[0]
#         if Command=="EXIT":
#             break

#         elif Command=="CREATE_USER":
#             User_Type=List_Input[1]
#             User=List_Input[2]
#             if User_Type=="U":
#                 s=UndergraduateStudent(User)
#             # if User_Type=="G":
#             #     s=GraduateStudent(User)
#             # if User_Type=="P":
#             #     s=Professor(User)
#             Users[User]=s

#         elif Command=="SEARCH":
#             BookSearching=List_Input[1]
#             try:
#                 if BookSearching not in Dict_Inventory:
#                     raise BookNotAvailableError(BookSearching)
                
#                 CopiesLeft=int(Dict_Inventory[BookSearching])
#                 if CopiesLeft==0:
#                     raise InsufficientBookError(BookSearching)

#                 print(f"{BookSearching} has {CopiesLeft} copies left.")

#             except (BookNotAvailableError, InsufficientBookError) as ErrorMsg:
#                 print(ErrorMsg)

#         elif Command=="BORROW":
#             User=List_Input[1]
#             BookBorrowing=List_Input[2]
#             s=Users.get(User)  #
#             try:
#                 if BookBorrowing not in Dict_Inventory:
#                     raise BookNotAvailableError(BookBorrowing)
                
#                 CopiesLeft=int(Dict_Inventory[BookBorrowing])
#                 if CopiesLeft==0:
#                     raise InsufficientBookError(BookBorrowing)
                
#                 if isinstance(s, UndergraduateStudent):
#                     NumBooks=len(s.books_borrowed)
#                     if NumBooks+1>5:
#                         raise BorrowLimitError(User)
                
#                 s.borrowBook(BookBorrowing)
#                 Dict_Inventory[BookBorrowing]-=1

#             except (BookNotAvailableError, InsufficientBookError, BorrowLimitError) as ErrorMsg:
#                 print(ErrorMsg)

#         elif Command=="RETURN":
#             User=List_Input[1]
#             BookReturning=List_Input[2]
#             s=Users.get(User)  #
#             try:
#                 if BookReturning not in s.books_borrowed:
#                     raise DidNotBorrowError(User, BookReturning)
                
#                 if BookReturning not in Dict_Inventory:
#                     raise BookNotAvailableError(BookReturning)

#                 s.returnBook(BookReturning)
#                 Dict_Inventory[BookReturning]+=1

#             except(DidNotBorrowError, BookNotAvailableError) as ErrorMsg:
#                 print(ErrorMsg)

#         elif Command=="SHOW":
#             User=List_Input[1]
#             s=Users.get(User)  #
#             print("")
#             print(f"---{User}'s Status---")
#             print(f"Borrowed Books: {s.books_borrowed}")
#             print("")

#         # elif Command=="APPLY_LAB":


#         # elif Command=="APPLY_CONFERENCE":