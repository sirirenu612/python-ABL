
# Manufacturing Cost and Profitability Analysis

quantity = int(input("Enter number of products: "))
material = float(input("Enter material cost per product: "))
labour = float(input("Enter labour charges per product: "))
wastage = float(input("Enter wastage cost per product: "))
machine = float(input("Enter machine cost per product: "))
selling_price = float(input("Enter selling price per product: "))
target = float(input("Enter target profit: "))

total_cost = (material + labour + wastage + machine) * quantity
total_sales = selling_price * quantity
profit = total_sales - total_cost

print("Total Manufacturing Cost:", total_cost)
print("Total Sales:", total_sales)
print("Total Profit:", profit)

if profit >= target:
    print("Profit Target Achieved")
else:
    print("Profit Target Not Achieved")

# Smart Parking Fee Management

def get_time(message):
    while True:
        value = input(message)

        # Check HH:MM format
        if len(value) != 5 or value[2] != ":":
            print("Invalid format. Enter time as HH:MM.")
            continue

        hour_text = value[0:2]
        minute_text = value[3:5]

        if not hour_text.isdigit() or not minute_text.isdigit():
            print("Invalid time. Use digits in HH:MM format.")
            continue

        hour = int(hour_text)
        minute = int(minute_text)

        if hour < 0 or hour > 23 or minute < 0 or minute > 59:
            print("Invalid time. Hours: 00-23, minutes: 00-59.")
            continue

        return hour * 60 + minute


# Vehicle rates
rates = {
    "bike": 20,
    "car": 50,
    "heavy": 100
}

daily_limits = {
    "bike": 200,
    "car": 500,
    "heavy": 1000
}

# Get vehicle category
while True:
    vehicle = input(
        "Enter vehicle category (bike/car/heavy): "
    ).lower()

    if vehicle in rates:
        break

    print("Invalid vehicle category. Try again.")

# Get entry and exit times
entry = get_time("Enter entry time (HH:MM): ")
exit_time = get_time("Enter exit time (HH:MM): ")

# Calculate duration and overnight status
overnight = False

if exit_time < entry:
    exit_time += 24 * 60
    overnight = True

duration = exit_time - entry

if duration == 0:
    print("Entry and exit times cannot be identical.")
else:
    # Round up to the next full hour
    billable_hours = (duration + 59) // 60

    # Calculate hourly fee
    hourly_fee = billable_hours * rates[vehicle]

    # Apply daily maximum to hourly fee
    parking_fee = min(
        hourly_fee, daily_limits[vehicle]
    )

    # Add overnight fee
    overnight_fee = 0

    if overnight:
        overnight_fee = 100

    # Apply penalty for parking over 12 hours
    penalty = 0

    if duration > 12 * 60:
        penalty = 200

    total_fee = parking_fee + overnight_fee + penalty

    # Display bill
    print("\n--- PARKING BILL ---")
    print("Vehicle category:", vehicle)
    print("Parking duration:", duration // 60,
          "hours", duration % 60, "minutes")
    print("Billable hours:", billable_hours)
    print("Hourly parking fee: Rs.", hourly_fee)
    print("Fee after daily limit: Rs.", parking_fee)
    print("Overnight fee: Rs.", overnight_fee)
    print("Penalty: Rs.", penalty)
    print("Total parking fee: Rs.", total_fee)  ~ ~ ~mermid
    
