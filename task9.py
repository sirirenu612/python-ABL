
n = int(input("Enter number of products: "))

for i in range(n):
    print("\nProduct", i + 1)

    name = input("Enter product name: ")
    ordered = int(input("Enter ordered quantity: "))
    dispatched = int(input("Enter dispatched quantity: "))
    returned = int(input("Enter returned quantity: "))
    stock = int(input("Enter initial inventory: "))

    # Validate records
    if ordered < 0 or dispatched < 0 or returned < 0 or stock < 0:
        print("Invalid negative quantity!")

    elif dispatched > ordered:
        print("Inconsistent Record: Dispatch exceeds order!")

    elif returned > dispatched:
        print("Inconsistent Record: Returns exceed dispatch!")

    else:
        outstanding = ordered - dispatched
        updated_stock = stock - dispatched + returned

        print("\nProduct:", name)
        print("Outstanding Orders:", outstanding)
        print("Updated Inventory:", updated_stock)

        if outstanding == 0:
            print("Order Status: Fully Dispatched")
        else:
            print("Order Status: Pending Dispatch")

print("\nRetail Order Analysis Completed")
