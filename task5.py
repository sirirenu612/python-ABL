
capacity = int(input("Enter bus capacity: "))
passengers = int(input("Enter initial passengers: "))
stops = int(input("Enter number of stops: "))

for stop in range(1, stops + 1):
    print("\nStop", stop)

    boarding = int(input("Passengers boarding: "))
    alighting = int(input("Passengers alighting: "))

    if alighting > passengers:
        print("Error: Alighting count exceeds passengers!")
        continue

    passengers = passengers - alighting + boarding

    print("Passengers after stop:", passengers)

    if passengers > capacity:
        print("Capacity violation!")
    else:
        print("Within bus capacity.")

print("\nSimulation completed.")
