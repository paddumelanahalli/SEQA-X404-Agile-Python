def merge_inventories(store_a, store_b):
    """
    Merges two dictionaries representing store inventory.
    If an item exists in both, sum the quantities.
    """
    combined = store_a.copy()
    
    for item, quantity in store_b.items():
        if item in combined:
            combined[item] += quantity
        else:
            combined[item] = quantity
            
    return combined

# Example Usage
if __name__ == "__main__":
    warehouse_1 = {"Python_Books": 10, "Java_Books": 5}
    warehouse_2 = {"Python_Books": 2, "C_Books": 8}
    
    final_stock = merge_inventories(warehouse_1, warehouse_2)
    print(f"Merged Inventory: {final_stock}")

'''

def manual_tests():
    print("\n--- Test 1: Overlapping Items ---")
    print(merge_inventories({"Python": 5}, {"Python": 3}))

    print("\n--- Test 2: No Overlap ---")
    print(merge_inventories({"Python": 5}, {"Java": 3}))

    print("\n--- Test 3: store_b Empty ---")
    print(merge_inventories({"Python": 5}, {}))

    print("\n--- Test 4: store_a Empty ---")
    print(merge_inventories({}, {"Java": 3}))

    print("\n--- Test 5: Both Empty ---")
    print(merge_inventories({}, {}))

AI Integration Exercise

Ask students:

“Generate edge-case test data for a dictionary merge function handling inventory quantities.”

Expected AI-generated negative tests:

Non-numeric quantities

None values

Very large numbers

Mixed key types

Case sensitivity issues ("python" vs "Python")

'''
    
