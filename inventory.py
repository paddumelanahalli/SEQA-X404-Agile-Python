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
