import os
import csv

projectName = "Inventory Management System"
print(f"\n** Welcome to {projectName} **")


class Product:
    def __init__(self, code, name, price, quantity):
        self.code = code
        self.name = name
        self.price = price
        self.quantity = quantity

    def show_info(self):
        print(f"Code: {self.code}")
        print(f"Name: {self.name}")
        print(f"Price: {self.price}")
        print(f"Quantity: {self.quantity}")


def load_from_csv(filename="inventory.csv"):
    if not os.path.exists(filename):
        return
    with open(filename, mode="r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            code = int(row["Code"])
            name = row["Name"]
            price = float(row["Price"])
            quantity = int(row["Quantity"])
            inventory.append(Product(code, name, price, quantity))
    print("--- Inventory loaded from CSV ---")


def save_to_csv(filename="inventory.csv"):
    with open(filename, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Code", "Name", "Price", "Quantity"])
        for product in inventory:
            writer.writerow(
                [product.code, product.name, product.price, product.quantity]
            )
    print("--- Inventory saved to CSV ---")


inventory = []
load_from_csv()


def to_continue():
    while True:
        print("\n- Do you want to continue?")
        print("1. Yes")
        print("2. No")

        try:
            userChoice = int(input("\nEnter your choice: "))
        except ValueError:
            print("\n-!- Invalid choice -!-")
            continue

        if userChoice == 1:
            add_product()
        elif userChoice == 2:
            print("\n--- Exiting the program. Goodbye! ---")
            break
        else:
            print("\n-!- There is no such option -!-")


def add_product():
    print("\n# Please enter your product information. ")

    productCode = input("- Enter your product code: ")
    productName = input("- Enter your product name: ")
    productPrice = input("- Enter your price: ")
    productQuantity = input("- Enter your quantity: ")

    product = Product(
        productCode, productName, float(productPrice), int(productQuantity)
    )

    inventory.append(product)
    save_to_csv()

    print("\n--- Product added successfully! ---")


def show_all_products():
    if len(inventory) > 0:
        for i, product in enumerate(inventory, start=1):
            print(f"\nProduct {i}")
            product.show_info()
    else:
        print("\n-!- Inventory is empty -!-")


def search_product():
    searchQuery = input("\n# Search your product by Name/Code: ").lower()
    found = False

    for product in inventory:
        if (
            searchQuery == str(product.code).lower()
            or searchQuery == product.name.lower()
        ):
            found = True
            product.show_info()
            break
        else:
            found = False
            continue

    if not found:
        print("\n-!- Product not Found -!-")


def delete_product():
    deleteQuery = input(
        "\n# Enter Name/Code of the product you want to delete: "
    ).lower()

    for product in inventory:
        if (
            deleteQuery == str(product.code).lower()
            or deleteQuery == product.name.lower()
        ):
            # confirmation = input("\n- Are you sure you want to delete this product? (Y/N): ").lower()
            confirmation = (
                str(input("- Are you sure you want to delete this product? (Y/N): "))
                .strip()
                .lower()
            )

            if confirmation == "y":
                inventory.remove(product)
                save_to_csv()
                print("\n--- Product deleted successfully! ---")
            elif confirmation == "n":
                print("\n- Deletion canceled.")
        return

    print("-!- Product not found -!-")


while True:
    print("\n- What can I help you with?")
    print("1. Add Product")
    print("2. Show All Products")
    print("3. Search Product")
    print("4. Delete Product")
    print("5. Exit")

    try:
        userChoice = int(input("\nEnter your choice: "))
    except ValueError:
        print("\n-!- Invalid choice -!-")
        continue

    match userChoice:
        case 1:
            add_product()
            to_continue()
        case 2:
            show_all_products()
        case 3:
            search_product()
        case 4:
            delete_product()
        case 5:
            print("\n--- Exiting the program. Goodbye! ---")
            break
        case _:
            print("\n-!- There is no such option -!-")
