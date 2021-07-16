from datetime import datetime
datetime=datetime.now()
current_time=datetime

tables=[]

class Table:
    def __init__(self, number):
       self.number = number
       self.occupied = False
       self.start_time = None
       self.end_time = None
       self.time_played = None
       self.current_time = None
       self.cost=None

    def checkout(self):
      self.occupied=True
      self.start_time=datetime.now()
      print(f"You checkout Table {self.number} {self.occupied} {self.start_time.strftime('%m/%d/%Y %H:%M%:%S')}")


    def checkin(self):
        self.occupied=False
        self.start_time=None
        self.end_time=timedelta.now()
        self.time_played=self.end_time-self.start_time
        print(f"Table Closed  Table {self.number} {self.occupied} {self.end_time.strftime('%m/%d/%Y %H:%M%:%S')}")

#class ActivityLog():
   # def __init__(self, date):
       # self.date = date
       # self.entry_list = []
       # self.clock=None

    def cost_calc(self, end, start):
        self.delta_time =self.end_time - self.start_time
        self.delta_min = delta_time.now()
        self.hours = round(delta_sec / (60 * 60))
        self.total_time_minutes = self.total_time.total_seconds() / 60
        self.cost = f"${(hours * 30.00) + (minutes * 0.50)}"
        return cost
           
def display_tables():
    
    for table in tables:
        if table.occupied==False:
            status="Available"
            print(f"Table {table.number}: {status}")

        else:
            status="Occupied"
            print(f"\n Table--{table.number} start_time--{table.start_time.strftime('%m/%d/%Y %H:%M%:%S')}  status--{table.occupied} ")
        
        
def to_add_file():
     date=str(datetime.now())
     file_ext=".txt"
     file_name=date + file_ext
     with open(file_name,"w") as file:
         array=[]
         for table in tables:
            table_info=f"Table {table.number} Start time: {table.start_time} End time{table.end_time} Time played: {table.time_played} Cost:{table.cost}\n"
            file.write(table_info)


   #POPULATE POOL TABE ARRAY (1-12) 
for i in range (1,13):
  table=Table(i)
  tables.append(table)
  
  
print(f" \n----UNIVERSITY OF TEXAS POOL TABLE MANAGMANT--------\n")
print("TO CHECKOUT Table: Enter 1: ")
print("TO CHECKIN Table: Enter  2: ")
print("TO VIEW ALL Table: enter 3: ")
print("To QUIT the app:enter 'q': ")
print("******************************************************")

while True:

    choice=input("please select your choice from the menu:")
    print("*******************PoolTable List**************")

    try:
        if choice== "1":

            display_tables()
            table_number=int(input("Enter table Number to check-out:"))
            table=tables[table_number-1]
            table.time_start=datetime.now()
            table.checkout()

            # give the option to choose which table to checkin

        elif choice=="2":
            display_tables()
            table_number=int(input("Enter Checkin Number:"))
            table=tables[table_number-1]
            table.end_time=datetime.now()
            cost = "${(delat* 30.00) + (minutes * 0.50)}"
            print(cost)
            print(f"Table {table_number} has been closed out at: {end_time.strftime('%m/%d/%Y %H:%M%:%S')}")


        elif choice=="3":
            for table in tables:
                print(f"Table No--{table.number}-- current_time--{current_time.strftime('%m/%d/%Y %H:%M%:%S')}--status--{table.occupied}")

        elif choice=="q":
            to_add_file()
            break

        else: 

             print("Thank you for using our shop!!")

    except IndexError:
        print("please select with in 1 and 12 range")

      
   