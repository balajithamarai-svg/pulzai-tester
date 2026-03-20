# Parking Lot Management System

total_slots = 5
parking_lot = []

while True:
    print("\nParking Lot Management System")
    print("1. Park Vehicle")
    print("2. Remove Vehicle")
    print("3. Show Available Slots")
    print("4. Show Parked Vehicles")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        if len(parking_lot) < total_slots:
            vehicle = input("Enter vehicle number: ")
            parking_lot.append(vehicle)
            print("Vehicle parked successfully.")
        else:
            print("Parking lot is full.")

    elif choice == "2":
        vehicle = input("Enter vehicle number to remove: ")
        if vehicle in parking_lot:
            parking_lot.remove(vehicle)
            print("Vehicle removed successfully.")
        else:
            print("Vehicle not found.")

    elif choice == "3":
        print("Available slots:", total_slots - len(parking_lot))

    elif choice == "4":
        print("Parked Vehicles:", parking_lot)

    elif choice == "5":
        print("Exiting system...")
        break

    else:
        print("Invalid choice")
