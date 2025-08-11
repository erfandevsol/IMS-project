import os
import csv
import pandas as pd
import webbrowser

projectName = "Inventory Management System"


# Define a class to represent a product in the inventory
class Product:
    def __init__(self, code, name, price, quantity):
        self.code = code
        self.name = name
        self.price = price
        self.quantity = quantity

    # Print product details
    def show_info(self):
        print(f"Code: {self.code}")
        print(f"Name: {self.name}")
        print(f"Price: {self.price}")
        print(f"Quantity: {self.quantity}")


# Filenames for session (temporary) and original (master) inventory
SESSION_FILE = "session_data.csv"
ORIGINAL_FILE = "products.csv"


# Load product data from a CSV file into the inventory list
def load_from_csv(filename=ORIGINAL_FILE):
    if not os.path.exists(filename):
        return  # If file doesn't exist, skip loading
    with open(filename, mode="r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            code = int(row["Code"])
            name = row["Name"]
            price = int(row["Price"])
            quantity = int(row["Quantity"])
            inventory.append(Product(code, name, price, quantity))
    print(f"\n--- Inventory loaded from {ORIGINAL_FILE} ---")


# Save current inventory to session file (used during the session only)
def save_to_csv(filename=SESSION_FILE):
    with open(filename, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Code", "Name", "Price", "Quantity"])
        for product in inventory:
            writer.writerow(
                [product.code, product.name, product.price, product.quantity]
            )
    print(f"\n--- Inventory saved to {SESSION_FILE} ---")


# Utility to ensure numeric input (used for price/quantity)
def get_valid_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("\n-!- Invalid input. Please enter an number -!-")


# Initialize inventory list
inventory = []
load_from_csv()

print(f"\n** Welcome to {projectName} **")
print("\n-$- What can I help you with? -$-")


# Show all products in the inventory
def show_all_products():
    if len(inventory) > 0:
        for i, product in enumerate(inventory, start=1):
            print(f"\nProduct {i}")
            product.show_info()
    else:
        print("\n-!- Inventory is empty -!-")


# Add a new product to inventory
def add_product():
    print("\n# Please enter your product information. ")

    productCode = input("- Enter your product code: ")
    productName = input("- Enter your product name: ")
    productPrice = get_valid_int("- Enter your price: ")
    productQuantity = get_valid_int("- Enter your quantity: ")

    product = Product(productCode, productName, productPrice, productQuantity)

    inventory.append(product)
    print("\n--- Product added successfully! ---")

    save_to_csv()


# Edit an existing product by code or name
def edit_product():
    editQuery = input("\n# Enter Name/Code of the product you want to edit: ").lower()

    for product in inventory:
        if (
            editQuery == str(product.name).lower()
            or editQuery == str(product.code).lower()
        ):
            print("\nCurrent Product Info: ")
            product.show_info()

            # Ask user what to change
            if input("\n- Change code? (Y/N): ").strip().lower() == "y":
                new_code = input("- Enter new code: ")
                product.code = new_code

            if input("\n- Change name? (Y/N): ").strip().lower() == "y":
                new_name = input("- Enter new name: ")
                product.name = new_name

            if input("\n- Change price? (Y/N): ").strip().lower() == "y":
                while True:
                    try:
                        new_price = get_valid_int("- Enter new price: ")
                        product.price = new_price
                        break
                    except ValueError:
                        print("\n-!- Invalid price, please enter a number -!-")

            if input("\n- Change quantity? (Y/N): ").strip().lower() == "y":
                while True:
                    try:
                        new_quantity = get_valid_int("- Enter new quantity: ")
                        product.quantity = new_quantity
                        break
                    except ValueError:
                        print("\n-!- Invalid quantity, please enter an integer -!-")

            print("\nEdited product information:")
            product.show_info()
            print("\n--- Product updated successfully! ---")

            save_to_csv()
            return

        else:
            continue

    print("\n-!- Product not found -!-")


# Delete a product from the inventory
def delete_product():
    deleteQuery = input(
        "\n# Enter Name/Code of the product you want to delete: "
    ).lower()

    for product in inventory:
        if (
            deleteQuery == str(product.code).lower()
            or deleteQuery == product.name.lower()
        ):
            print("\nCurrent Product Info: ")
            product.show_info()

            # Confirm before deletion
            confirmation = (
                input("\n- Are you sure you want to delete this product? (Y/N): ")
                .strip()
                .lower()
            )

            if confirmation == "y":
                inventory.remove(product)
                print("\n--- Product deleted successfully! ---")
                save_to_csv()
            elif confirmation == "n":
                print("\n- Deletion canceled.")
            return

        else:
            continue

    print("\n-!- Product not found -!-")


# Sort products by name, price or quantity
def sort_products():
    print("\n# Sort products by:")
    print("1. Name (A–Z)")
    print("2. Price (Low to High)")
    print("3. Quantity (High to Low)")

    try:
        choice = int(input("\nEnter your choice: "))
    except ValueError:
        print("\n-!- Invalid input -!-")
        return

    match choice:
        case 1:
            sorted_list = sorted(inventory, key=lambda p: p.name.lower())
        case 2:
            sorted_list = sorted(inventory, key=lambda p: p.price)
        case 3:
            sorted_list = sorted(inventory, key=lambda p: p.quantity, reverse=True)
        case _:
            print("\n-!- There is no such option -!-")

    # Replace current list with sorted list
    inventory.clear()
    inventory.extend(sorted_list)

    print("\n--- Products sorted and saved to session file ---")
    for i, product in enumerate(inventory, start=1):
        print(f"\nProduct {i}")
        product.show_info()

    save_to_csv()


# Search for a product by name or code
def search_product():
    searchQuery = input("\n# Search your product by Name/Code: ").lower()
    found = False

    for product in inventory:
        if (
            searchQuery == str(product.code).lower()
            or searchQuery == product.name.lower()
        ):
            found = True
            print("\nSearched product:")
            product.show_info()
            break
        else:
            found = False
            continue

    if not found:
        print("\n-!- Product not Found -!-")


# Export the inventory to an Excel file and open it
def export_to_excel():
    if not inventory:
        print("\n-!- No products to export -!-")
        return

    data = [
        {
            "Code": product.code,
            "Name": product.name,
            "Price": product.price,
            "Quantity": product.quantity,
        }
        for product in inventory
    ]

    df = pd.DataFrame(data)
    filename = "inventory_export.xlsx"
    df.to_excel(filename, index=False)

    print(f"\n--- Excel file created: {filename} ---")
    webbrowser.open(filename)  # Open file in default spreadsheet app


# Ask user to confirm saving session changes to the original file
def confirm_save_changes():
    print("\n# Do you want to save the changes to the original file?")
    print("1. Yes, save changes")
    print("2. No, discard changes")

    while True:
        choice = int(input("\nEnter your choice: "))

        match choice:
            case 1:
                with (
                    open(SESSION_FILE, "r", encoding="utf-8") as src,
                    open(ORIGINAL_FILE, "w", encoding="utf-8", newline="") as dst,
                ):
                    dst.write(src.read())
                print(f"\n--- Changes saved to {ORIGINAL_FILE} ---")
                break
            case 2:
                print("\n--- Changes discarded ---")
                break
            case _:
                print("-!- Invalid choice -!-")


# --- Main program loop ---
try:
    while True:
        print("\n- Program menu:")
        print("1. Show All Products")
        print("2. Add Product")
        print("3. Edit Product")
        print("4. Delete Product")
        print("5. Sort Products")
        print("6. Search Product")
        print("7. Export to Excel")
        print("8. Save Changes")
        print("9. Exit")

        try:
            userChoice = int(input("\nEnter your choice: "))
        except ValueError:
            print("\n-!- Invalid choice -!-")
            continue

        match userChoice:
            case 1:
                show_all_products()
            case 2:
                add_product()
            case 3:
                edit_product()
            case 4:
                delete_product()
            case 5:
                sort_products()
            case 6:
                search_product()
            case 7:
                export_to_excel()
            case 8:
                confirm_save_changes()
            case 9:
                confirm_save_changes()
                print("\n--- Exiting the program. Goodbye! ---")
                break
            case _:
                print("\n-!- There is no such option -!-")

# Handle Ctrl + C exit gracefully
except KeyboardInterrupt:
    print("\n\n--- Program interrupted by user (Ctrl + C) ---")
    confirm_save_changes()
    print("\n--- Exiting the program. Goodbye! ---")
