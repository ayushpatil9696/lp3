# Dynamic Programming function to solve 0-1 Knapsack problem
def solve_knapsack(max_weight, item_weights, item_values, num_items):
    # Create a DP table to store the maximum value that can be achieved
    # with 'i' items and total weight 'w'
    dp_table = [[0 for _ in range(max_weight + 1)] for _ in range(num_items + 1)]

    # Build the DP table in bottom-up manner
    for i in range(num_items + 1):
        for w in range(max_weight + 1):
            if i == 0 or w == 0:
                dp_table[i][w] = 0
            elif item_weights[i-1] <= w:
                dp_table[i][w] = max(item_values[i-1] + dp_table[i-1][w-item_weights[i-1]], dp_table[i-1][w])
            else:
                dp_table[i][w] = dp_table[i-1][w]

    return dp_table[num_items][max_weight]

# Test driver code
if __name__ == "__main__":
    item_values = [60, 100, 120]  # Values of items
    item_weights = [10, 20, 30]  # Weights of items
    max_weight = 50  # Maximum weight capacity of knapsack
    num_items = len(item_values)  # Number of items

    print(f"The maximum value that can be put in a knapsack of capacity {max_weight} is {solve_knapsack(max_weight, item_weights, item_values, num_items)}")

# TIME COMPLEXITY IS = O(nW), where nn is the number of items and WW is the maximum weight capacity of the knapsack.
# SPACE COMPLEXITY IS = O(nW)