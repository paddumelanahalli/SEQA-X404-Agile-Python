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


1. Normal Case – Overlapping Items (IF branch)
store_a = {"Python_Books": 10}
store_b = {"Python_Books": 5}

2. Normal Case – No Overlap (ELSE branch)
store_a = {"Python_Books": 10}
store_b = {"Java_Books": 5}


Expected Output:

{"Python_Books": 10, "Java_Books": 5}


✔ Tests new key insertion

3. Mixed Case – Partial Overlap
store_a = {"Python_Books": 10, "Java_Books": 3}
store_b = {"Python_Books": 2, "C_Books": 8}


Expected Output:

{"Python_Books": 12, "Java_Books": 3, "C_Books": 8}


✔ Tests both IF and ELSE in same run
✔ Important structural coverage

4. store_b Empty (Loop Skipped)
store_a = {"Python_Books": 10}
store_b = {}


Expected Output:

{"Python_Books": 10}


✔ Tests zero-iteration path
5. store_a Empty
store_a = {}
store_b = {"Java_Books": 5}


Expected Output:

{"Java_Books": 5}


✔ Tests pure ELSE path
6. Both Empty
store_a = {}
store_b = {}


Expected Output:

{}


✔ Edge case – minimal structure

7. Duplicate Across Multiple Items
store_a = {"Python": 5, "Java": 3}
store_b = {"Python": 4, "Java": 2}


Expected Output:

{"Python": 9, "Java": 5}


✔ Tests multiple IF executions

8. Negative Quantities (Business Rule Issue)
store_a = {"Python": 10}
store_b = {"Python": -3}


Current Output (Problematic):

{"Python": 7}


Discussion:

Should inventory allow negative stock?

Structural logic works, but business rule may fail.

9. Non-Numeric Quantity (Type Error Case)
store_a = {"Python": 10}
store_b = {"Python": "five"}


Expected Result:
Program crashes with:

TypeError: unsupported operand type(s)


✔ Tests structural failure
✔ Tests data type validation absence

10. Case Sensitivity Problem
store_a = {"python_books": 10}
store_b = {"Python_Books": 5}


Expected Output:

{"python_books": 10, "Python_Books": 5}


Discussion:

Are these the same product?

Structural match fails due to case sensitivity.

11. Very Large Numbers
store_a = {"Python": 10**12}
store_b = {"Python": 10**12}


✔ Tests numeric stability

12. Side Effect Test (Important Structural Check)
store_a = {"Python": 10}
store_b = {"Python": 5}

result = merge_inventories(store_a, store_b)

print("Result:", result)
print("Original store_a:", store_a)


Expected:

Result: {'Python': 15}
Original store_a: {'Python': 10}


✔ Verifies .copy() prevented mutation

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
    
