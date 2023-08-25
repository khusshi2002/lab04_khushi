class FlightRecord:
    def __init__(self, p_id, process, start_time, priority):
        self.p_id = p_id
        self.process = process
        self.start_time = start_time
        self.priority = priority
    
    def display(self):
        print(f"{self.p_id}\t{self.process}\t{self.start_time}\t{self.priority}")

class FlightTable:
    def __init__(self):
        self.records = []
    
    def add_record(self, record):
        self.records.append(record)
    
    def sort_by_p_id(self):
        self.records.sort(key=lambda record: record.p_id)
    
    def sort_by_start_time(self):
        self.records.sort(key=lambda record: record.start_time)
    
    def sort_by_priority(self):
        self.records.sort(key=lambda record: record.priority, reverse=True)
    
    def display_table(self):
        print("P_ID\tProcess\tStart Time (ms)\tPriority")
        for record in self.records:
            record.display()

def main():
    flight_table = FlightTable()
    
    flight_table.add_record(FlightRecord("P1", "VSCode", 100, "MID"))
    flight_table.add_record(FlightRecord("P23", "Eclipse", 234, "MID"))
    flight_table.add_record(FlightRecord("P93", "Chrome", 189, "High"))
    flight_table.add_record(FlightRecord("P42", "JDK", 9, "High"))
    flight_table.add_record(FlightRecord("P9", "CMD", 7, "High"))
    flight_table.add_record(FlightRecord("P87", "NotePad", 23, "Low"))
    
    print("Sorting options:")
    print("1. Sort by P_ID")
    print("2. Sort by Start Time")
    print("3. Sort by Priority")
    
    option = int(input("Enter sorting option: "))
    
    if option == 1:
        flight_table.sort_by_p_id()
    elif option == 2:
        flight_table.sort_by_start_time()
    elif option == 3:
        flight_table.sort_by_priority()
    else:
        print("Invalid option")
        return
    
    flight_table.display_table()

if __name__ == "__main__":
    main()
