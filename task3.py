
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
