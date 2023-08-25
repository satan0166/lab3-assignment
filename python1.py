class FlightTable:
    def __init__(self):
        self.data = []
    
    def add_entry(self, pid, process, start_time, priority):
        self.data.append((pid, process, start_time, priority))
    
    def print_table(self):
        print("{:<5} {:<10} {:<15} {:<8}".format("P_ID", "Process", "Start Time (ms)", "Priority"))
        print("="*40)
        for entry in self.data:
            print("{:<5} {:<10} {:<15} {:<8}".format(entry[0], entry[1], entry[2], entry[3]))
    
    def sort_by_pid(self):
        self.data.sort(key=lambda entry: entry[0])
    
    def sort_by_start_time(self):
        self.data.sort(key=lambda entry: entry[2])
    
    def sort_by_priority(self):
        self.data.sort(key=lambda entry: entry[3], reverse=True)

def main():
    flight_table = FlightTable()
    flight_table.add_entry("P1", "VSCode", 100, "MID")
    flight_table.add_entry("P23", "Eclipse", 234, "MID")
    flight_table.add_entry("P93", "Chrome", 189, "High")
    flight_table.add_entry("P42", "JDK", 9, "High")
    flight_table.add_entry("P9", "CMD", 7, "High")
    flight_table.add_entry("P87", "NotePad", 23, "Low")
    
    while True:
        print("\nSort Options:")
        print("1. Sort by P_ID\n2. Sort by Start Time\n3. Sort by Priority\n4. Quit")
        choice = input("Enter your choice: ")
        
        if choice == "1":
            flight_table.sort_by_pid()
        elif choice == "2":
            flight_table.sort_by_start_time()
        elif choice == "3":
            flight_table.sort_by_priority()
        elif choice == "4":
            break
        else:
            print("Invalid choice. Please select a valid option.")
            continue
        
        flight_table.print_table()

if __name__ == "__main__":
    main()
