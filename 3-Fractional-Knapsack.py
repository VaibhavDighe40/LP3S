def fractional_knapsack(items, capacity):
    # Sort items by profit-to-weight ratio in descending order
    items.sort(key=lambda x: x[1] / x[0], reverse=True)

    total_profit, knapsack = 0, []

    # Iterate through sorted items
    for weight, profit in items:
        # Take as much as possible or the whole item if it fits
        fraction = min(capacity, weight) / weight
        # Add the selected portion to the knapsack
        knapsack.append((min(capacity, weight), fraction * profit))
        # Update total profit and remaining capacity
        total_profit += fraction * profit
        capacity -= min(capacity, weight)

    return total_profit, knapsack

# User input
num_items = int(input("Enter the number of items: "))
items = [(float(input(f"Enter weight for item {i + 1}: ")),
          float(input(f"Enter profit for item {i + 1}: ")))
         for i in range(num_items)]
knapsack_capacity = float(input("Enter the knapsack capacity: "))

# Solve the fractional knapsack problem and display the results
max_profit, selected_items = fractional_knapsack(items, knapsack_capacity)
print(f"\nMaximum profit in the knapsack: {max_profit}")
print("Selected items:")
for weight, profit in selected_items:
    print(f"  Weight: {weight}, Profit: {profit}")

"""""
Enter the number of items: 3 
Enter weight for item 1: 18
Enter profit for item 1: 25
Enter weight for item 2: 15
Enter profit for item 2: 24
Enter weight for item 3: 10
Enter profit for item 3: 15
Enter the knapsack capacity: 20

Maximum profit in the knapsack: 31.5
Selected items:
  Weight: 15.0, Profit: 24.0
  Weight: 5.0, Profit: 7.5
  Weight: 0.0, Profit: 0.0
"""""