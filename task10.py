
appliances = []

n = int(input("Enter number of appliances: "))

for i in range(n):
    print("\nAppliance", i + 1)

    name = input("Enter appliance name: ")
    before = float(input("Enter electricity usage before: "))
    after = float(input("Enter electricity usage after: "))

    # Validate consumption
    if before < 0 or after < 0:
        print("Invalid electricity consumption!")

    elif before == 0:
        print("Cannot calculate savings percentage!")
        continue

    else:
        savings = before - after
        percentage = (savings / before) * 100

        # Conditional statements
        if savings > 0:
            status = "Energy Saved"

        elif savings < 0:
            status = "Energy Consumption Increased"

        else:
            status = "No Change"

        appliances.append({
            "name": name,
            "before": before,
            "after": after,
            "savings": savings,
            "percentage": percentage,
            "status": status
        })

# Rank appliances by savings percentage
appliances.sort(
    key=lambda x: x["percentage"],
    reverse=True
)

print("\n===== ENERGY SAVINGS REPORT =====")

rank = 1

for a in appliances:
    print("\nRank:", rank)
    print("Appliance:", a["name"])
    print("Before Usage:", a["before"], "kWh")
    print("After Usage:", a["after"], "kWh")
    print("Energy Savings:", a["savings"], "kWh")
    print("Savings Percentage:", round(a["percentage"], 2), "%")
    print("Status:", a["status"])

    rank += 1

print("\nEnergy Analysis Completed")
