# Function to solve the Fractional Knapsack Problem
def fractional_knapsack(capacity, weights, values):
    # Calculate value per unit weight for each item
    value_per_weight = [(val / weight, weight, val) for val, weight in zip(values, weights)]
    
    # Sort items by value per unit weight in descending order
    value_per_weight.sort(reverse=True)
    
    # Initialize total value in knapsack
    total_value = 0
    
    for val_per_wt, wt, val in value_per_weight:
        if capacity >= wt:
            # If the whole item can fit, add its full value
            total_value += val
            capacity -= wt
        else:
            # If only a fraction can fit, add that fraction of the value
            fraction = capacity / wt
            total_value += val * fraction
            break  # Knapsack is full

    return total_value

# Test driver code
if __name__ == "__main__":
    capacity = 50  # Maximum weight the knapsack can hold
    weights = [10, 20, 30]  # Weights of available items
    values = [60, 100, 120]  # Values of available items
    
    max_value = fractional_knapsack(capacity, weights, values)
    print(f"The maximum value that can be placed into the knapsack is: {max_value}")

# TIME COMPLEXITY IS = O(nlogn)
# SPACE COMPLEXITY IS = O(n)