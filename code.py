# ==========================================================
# PROJECT NO. 19: INVENTORY MANAGEMENT SYSTEM
# Language: Python 3
# Concepts: Lists, Dictionaries, Functions, CRUD
# ==========================================================

# All products are stored as dictionaries inside this list.
inventory = []

# The first product ID will be I101.
next_id = 101


# ----------------------------------------------------------
# 1. ADD ITEM
# ----------------------------------------------------------
def add_item():
    global next_id

    name = input("Enter item name: ").strip()

    if not name:
        print("Invalid item name. Name cannot be empty.")
        return

    try:
        quantity = int(input("Enter quantity: "))
        price = float(input("Enter price: "))
    except ValueError:
        print("Invalid input. Enter a whole number for quantity and a number for price.")
        return

    # Quantity must be a non-negative whole number.
    if quantity < 0:
        print("Invalid quantity. Quantity must be a non-negative whole number.")
        print("Item not added.")
        return

    # Price must not be negative.
    if price < 0:
        print("Invalid price. Price must be non-negative.")
        print("Item not added.")
        return

    item_id = "I" + str(next_id)

    item = {
        "id": item_id,
        "name": name,
        "quantity": quantity,
        "price": price
    }

    inventory.append(item)
    next_id += 1

    print("Item added.")
    print(f"ID: {item_id} | {name} | Qty: {quantity} | Price: {price:g}")

    if quantity < 5:
        print(f"Low stock alert: {name} ({quantity})")


# ----------------------------------------------------------
# 2. VIEW ALL ITEMS
# ----------------------------------------------------------
def view_items():
    if not inventory:
        print("Inventory is empty.")
        return

    print("\n" + "-" * 65)
    print(f"{'ID':<10}{'Name':<20}{'Quantity':<15}{'Price':<15}")
    print("-" * 65)

    for item in inventory:
        print(
            f"{item['id']:<10}"
            f"{item['name']:<20}"
            f"{item['quantity']:<15}"
            f"{item['price']:<15.2f}"
        )

    print("-" * 65)


# ----------------------------------------------------------
# 3. SEARCH ITEM BY ID
# ----------------------------------------------------------
def search_item():
    item_id = input("Enter item ID: ").strip().upper()

    for item in inventory:
        if item["id"] == item_id:
            print("\nItem found:")
            print(f"ID: {item['id']}")
            print(f"Name: {item['name']}")
            print(f"Quantity: {item['quantity']}")
            print(f"Price: {item['price']:g}")
            return

    print(f"Item ID {item_id} not found.")


# ----------------------------------------------------------
# 4. UPDATE ITEM
# ----------------------------------------------------------
def update_item():
    item_id = input("Enter item ID: ").strip().upper()

    for item in inventory:
        if item["id"] == item_id:
            print(f"Updating: {item['name']}")
            print("1. Update name")
            print("2. Update quantity")
            print("3. Update price")
            print("4. Update all details")

            choice = input("Choose what to update: ").strip()

            if choice in ("1", "4"):
                new_name = input("Enter new name: ").strip()
                if not new_name:
                    print("Invalid name. Update cancelled.")
                    return
                item["name"] = new_name

            if choice in ("2", "4"):
                try:
                    new_quantity = int(input("Enter new quantity: "))
                except ValueError:
                    print("Invalid quantity. Update cancelled.")
                    return

                if new_quantity < 0:
                    print("Invalid quantity. Quantity must be non-negative.")
                    return

                item["quantity"] = new_quantity

            if choice in ("3", "4"):
                try:
                    new_price = float(input("Enter new price: "))
                except ValueError:
                    print("Invalid price. Update cancelled.")
                    return

                if new_price < 0:
                    print("Invalid price. Price must be non-negative.")
                    return

                item["price"] = new_price

            if choice not in ("1", "2", "3", "4"):
                print("Invalid update option.")
                return

            print("Item updated successfully.")
            return

    print(f"Item ID {item_id} not found.")


# ----------------------------------------------------------
# 5. DELETE ITEM
# ----------------------------------------------------------
def delete_item():
    item_id = input("Enter item ID: ").strip().upper()

    for item in inventory:
        if item["id"] == item_id:
            inventory.remove(item)
            print("Item deleted.")
            print(f"Items left: {len(inventory)}")
            return

    print(f"Item ID {item_id} not found.")


# ----------------------------------------------------------
# 6. CALCULATE TOTAL STOCK VALUE
# ----------------------------------------------------------
def total_stock_value():
    total = 0

    for item in inventory:
        total += item["quantity"] * item["price"]

    # Display whole numbers without unnecessary decimal places.
    print(f"Total stock value: {total:g}")


# ----------------------------------------------------------
# 7. LOW STOCK REPORT
# ----------------------------------------------------------
def low_stock_report():
    print("\nLOW STOCK REPORT (Quantity below 5)")
    found = False

    for item in inventory:
        if item["quantity"] < 5:
            print(
                f"{item['id']} | {item['name']} | "
                f"Qty: {item['quantity']}"
            )
            found = True

    if not found:
        print("No low stock items found.")


# ----------------------------------------------------------
# 8. MAIN MENU
# ----------------------------------------------------------
def main():
    while True:
        print("\n========== INVENTORY MANAGEMENT SYSTEM ==========")
        print("1. Add Item")
        print("2. View Items")
        print("3. Update Item")
        print("4. Delete Item")
        print("5. Total Stock Value")
        print("6. Low Stock Report")
        print("7. Search Item")
        print("8. Exit")
        print("==================================================")

        choice = input("Enter menu option: ").strip()

        if choice == "1":
            add_item()
        elif choice == "2":
            view_items()
        elif choice == "3":
            update_item()
        elif choice == "4":
            delete_item()
        elif choice == "5":
            total_stock_value()
        elif choice == "6":
            low_stock_report()
        elif choice == "7":
            search_item()
        elif choice == "8":
            print("Thank you for using Inventory Management System!")
            break
        else:
            print("Invalid menu option. Please choose 1 to 8.")


# Run the program.
if __name__ == "__main__":
    main()
