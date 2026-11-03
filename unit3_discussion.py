
"""
Unit 3 Discussion: List Operations

INSTRUCTIONS:
This assignment focuses on understanding how lists behave when elements
are inserted, removed, and searched. You will analyze how Python lists
shift elements in memory and how different operations impact performance.
"""


def insert_at(lst, index, value):
    """
    Insert a value into the list at the specified index.

    Requirements:
    - Use a list operation to insert the value.
    - Explain what happens to existing elements after insertion.
    - Explain how insertion performance varies depending on position.
    """

    # Insert the value at the requested index.
    # Existing elements at and after this position shift one position right.
    # Inserting near the beginning requires more shifting than at the end.
    lst.insert(index, value)


def delete_at(lst, index):
    """
    Remove and return the value at the specified index.

    Requirements:
    - Validate that the index exists.
    - Return the removed value.
    - Return None if the index is invalid.
    """

    # Validate the index before attempting deletion.
    # This prevents errors when the list is empty or the index is invalid.
    if not isinstance(index, int) or index < 0 or index >= len(lst):
        return None

    # Remove and return the selected value.
    # Elements after the deleted position shift one position left.
    # Deleting near the beginning requires more shifting than deleting
    # the last element.
    return lst.pop(index)


def search_value(lst, value):
    """
    Search for a value within the list.

    Requirements:
    - Return the index if the value is found.
    - Return -1 if the value is not found.
    - Explain why this is a linear search.
    """

    # Linear search checks each element sequentially until a match is found.
    # In the worst case, every element must be checked.
    for index, item in enumerate(lst):
        if item == value:
            return index

    # Return -1 when the value does not exist in the list.
    return -1


def main():
    print("=== UNIT 3: LIST OPERATIONS ===")

    # ==============================
    # INSERTION TESTS
    # ==============================

    print("\n=== INSERTION TESTS ===")

    # Create a sample list for insertion demonstrations.
    numbers = [10, 20, 30, 40]
    print("Original list:", numbers)

    # Insert at the beginning.
    insert_at(numbers, 0, 5)
    print("After inserting 5 at the beginning:", numbers)

    # Insert in the middle.
    insert_at(numbers, 3, 25)
    print("After inserting 25 in the middle:", numbers)

    # Insert at the end.
    insert_at(numbers, len(numbers), 50)
    print("After inserting 50 at the end:", numbers)

    # ==============================
    # DELETION TESTS
    # ==============================

    print("\n=== DELETION TESTS ===")

    # Create a separate list for deletion demonstrations.
    numbers = [10, 20, 30, 40, 50]
    print("Original list:", numbers)

    # Delete from the beginning.
    removed = delete_at(numbers, 0)
    print("Removed from beginning:", removed)
    print("Updated list:", numbers)

    # Delete from the middle.
    removed = delete_at(numbers, 1)
    print("Removed from middle:", removed)
    print("Updated list:", numbers)

    # Delete from the end.
    removed = delete_at(numbers, len(numbers) - 1)
    print("Removed from end:", removed)
    print("Updated list:", numbers)

    # ==============================
    # SEARCH TESTS
    # ==============================

    print("\n=== SEARCH TESTS ===")

    numbers = [10, 20, 30, 40, 50]
    print("Search list:", numbers)

    # Search for a value that exists.
    result = search_value(numbers, 30)
    print("Searching for 30. Index found:", result)

    # Search for a value that does not exist.
    result = search_value(numbers, 99)
    print("Searching for 99. Index found:", result)

    # ==============================
    # EDGE CASES
    # ==============================

    print("\n=== EDGE CASES ===")

    # Edge Case 1: Insert into an empty list.
    empty_list = []
    print("Empty list before insertion:", empty_list)

    insert_at(empty_list, 0, 100)
    print("Empty list after insertion:", empty_list)

    # Edge Case 2: Attempt to delete from an empty list.
    empty_list = []
    removed = delete_at(empty_list, 0)
    print("Attempt to delete from an empty list:", removed)
    print("List after attempted deletion:", empty_list)

    # Edge Case 3: Attempt to delete using an invalid index.
    numbers = [10, 20, 30]
    removed = delete_at(numbers, 10)
    print("Attempt to delete using an invalid index:", removed)
    print("List remains unchanged:", numbers)

    # Edge Case 4: Search an empty list.
    empty_list = []
    result = search_value(empty_list, 10)
    print("Searching an empty list:", result)

    # ==============================
    # REAL-WORLD SCENARIO
    # ==============================

    print("\n=== REAL-WORLD SCENARIO: GROCERY SHOPPING LIST ===")

    # A grocery shopping application uses a list to manage items.
    grocery_list = ["Milk", "Bread", "Eggs"]
    print("Original grocery list:", grocery_list)

    # Add Apples at the second position.
    insert_at(grocery_list, 1, "Apples")
    print("After adding Apples:", grocery_list)

    # Remove Bread because it is no longer needed.
    removed_item = delete_at(grocery_list, 2)
    print("Removed grocery item:", removed_item)
    print("Updated grocery list:", grocery_list)

    # Search for Milk to check whether it is on the list.
    item_index = search_value(grocery_list, "Milk")
    print("Milk found at index:", item_index)

    print("\n=== ALL TESTS COMPLETED ===")


if __name__ == "__main__":
    main()
