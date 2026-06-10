# Smart Inventory Management System

inventory = {}

LOW_STOCK_THRESHOLD = 10


def add_product():
    pid = input("Enter Product ID: ")
    name = input("Enter Product Name: ")
    category = input("Enter Category: ")
    qty = int(input("Enter Quantity: "))
    price = float(input("Enter Price: "))
    supplier = input("Enter Supplier: ")

    inventory[pid] = {
        "name": name,
        "category": category,
        "qty": qty,
        "price": price,
        "supplier": supplier
    }

    print("✅ Product Added Successfully!")


def update_inventory():
    pid = input("Enter Product ID: ")

    if pid in inventory:
        inventory[pid]["qty"] = int(input("New Quantity: "))
        inventory[pid]["price"] = float(input("New Price: "))
        print("✅ Inventory Updated!")
    else:
        print("❌ Product Not Found!")


def search_product():
    keyword = input("Enter Product ID or Name: ").lower()

    found = False

    for pid, product in inventory.items():
        if keyword == pid.lower() or keyword == product["name"].lower():
            print("\nProduct Found:")
            print(pid, product)
            found = True

    if not found:
        print("❌ Product Not Found")


def display_inventory():
    if not inventory:
        print("Inventory Empty")
        return

    print("\n--- Inventory ---")
    print("ID\tName\tQty\tPrice\tCategory")

    for pid, p in inventory.items():
        print(f"{pid}\t{p['name']}\t{p['qty']}\t{p['price']}\t{p['category']}")


def low_stock_alert():
    print("\n--- Low Stock Products ---")

    found = False

    for pid, p in inventory.items():
        if p["qty"] < LOW_STOCK_THRESHOLD:
            print(f"{p['name']} -> Qty: {p['qty']}")
            found = True

    if not found:
        print("No Low Stock Products")


def out_of_stock_alert():
    print("\n--- Out Of Stock Products ---")

    found = False

    for pid, p in inventory.items():
        if p["qty"] == 0:
            print(f"{p['name']} is OUT OF STOCK")
            found = True

    if not found:
        print("No Out Of Stock Products")


def category_management():
    categories = set()

    for p in inventory.values():
        categories.add(p["category"])

    print("Categories:", categories)


def inventory_report():
    total_items = 0
    total_value = 0

    for p in inventory.values():
        total_items += p["qty"]
        total_value += p["qty"] * p["price"]

    print("\n--- Inventory Report ---")
    print("Total Items:", total_items)
    print("Total Inventory Value:", total_value)


def delete_product():
    pid = input("Enter Product ID to Delete: ")

    if pid in inventory:
        del inventory[pid]
        print("✅ Product Deleted")
    else:
        print("❌ Product Not Found")


while True:
    print("\n===== SMART INVENTORY MANAGEMENT SYSTEM =====")
    print("1. Add Product")
    print("2. Update Inventory")
    print("3. Search Product")
    print("4. Display Inventory")
    print("5. Low Stock Alert")
    print("6. Out Of Stock Alert")
    print("7. Category Management")
    print("8. Inventory Report")
    print("9. Delete Product")
    print("0. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        add_product()
    elif choice == "2":
        update_inventory()
    elif choice == "3":
        search_product()
    elif choice == "4":
        display_inventory()
    elif choice == "5":
        low_stock_alert()
    elif choice == "6":
        out_of_stock_alert()
    elif choice == "7":
        category_management()
    elif choice == "8":
        inventory_report()
    elif choice == "9":
        delete_product()
    elif choice == "0":
        print("Thank You!")
        break
    else:
        print("Invalid Choice")