import os
from csv import DictReader, writer
from pandas import DataFrame
from webbrowser import open as webbrowser_open
from fastapi import FastAPI
from pydantic import BaseModel

projectName = "Inventory Management System"
app = FastAPI(name=projectName)


# Define a class to represent a product in the inventory
class Product(BaseModel):
    code: int
    name: str = "   "
    price: float = 0
    quantity: int = 0

    # Print product details
    def show_info(self):
        return {
            "Code": self.code,
            "Name": self.name,
            "Price": self.price,
            "Quantity": self.quantity,
        }


# Filenames for session (temporary) and original (master) inventory
SESSION_FILE = "session_data.csv"
ORIGINAL_FILE = "products.csv"


# Load product data from a CSV file into the inventory list
def load_from_csv(filename=ORIGINAL_FILE):
    if not os.path.exists(filename):
        return  # If file doesn't exist, skip loading
    with open(filename, mode="r", newline="", encoding="utf-8") as file:
        reader = DictReader(file)
        for row in reader:
            code = int(row["Code"])
            name = row["Name"]
            price = float(row["Price"])
            quantity = int(row["Quantity"])
            inventory.append(Product(code=code, name=name, price=price, quantity=quantity))
    print(f"\n--- Inventory loaded from {ORIGINAL_FILE} ---")


# Save current inventory to session file (used during the session only)
def save_to_csv(filename=SESSION_FILE):
    with open(filename, mode="w", newline="", encoding="utf-8") as file:
        csv_file = writer(file)
        csv_file.writerow(["Code", "Name", "Price", "Quantity"])
        for product in inventory:
            csv_file.writerow(
                [product.code, product.name, product.price, product.quantity]
            )
    print(f"\n--- Inventory saved to {SESSION_FILE} ---")


# Initialize inventory list
inventory = []
load_from_csv()

print(f"\n** Welcome to {projectName} **")


# Show all products in the inventory
@app.get("/products")
def show_all_products():
    if len(inventory) > 0:
        return [product.show_info() for product in inventory]
    else:
        return {"message": "Inventory is empty"}


# Add a new product to inventory
@app.post("/products")
def add_product(product: Product):
    inventory.append(product)
    save_to_csv()
    return {"message": "Product added successfully!"}


# Edit an existing product by code or name
@app.put("/products/{product_id}")
def edit_product(product_id: int, updated: Product):
    for i, product in enumerate(inventory):
        if product.code == product_id:
            inventory[i] = updated
            save_to_csv()
            return {"message": "Product updated successfully!"}
    return {"message": "Product not found."}


# Delete a product from the inventory
@app.delete("/products/{product_id}")
def delete_product(product_id: int):
    for i, product in enumerate(inventory):
        if product.code == product_id:
            inventory.pop(i)
            save_to_csv()
            return {"message": "Product deleted successfully!"}
    return {"message": "Product not found."}


# Sort products by name, price or quantity
@app.get("/products/sort")
def sort_products(sort: str):
    if sort == "name":
        sorted_list = sorted(inventory, key=lambda p: p.name.lower())
    elif sort == "price":
        sorted_list = sorted(inventory, key=lambda p: p.price)
    elif sort == "quantity":
        sorted_list = sorted(inventory, key=lambda p: p.quantity, reverse=True)
    else:
        return {"message": "Invalid sort option."}

    # Replace current list with sorted list
    inventory.clear()
    inventory.extend(sorted_list)

    print("\n--- Products sorted and saved to session file ---")
    for i, product in enumerate(inventory, start=1):
        print(f"\nProduct {i}")
        product.show_info()

    save_to_csv()


# Search for a product by name or code
@app.get("/products/search")
def search_product(searchQuery: str):
    searchQuery = searchQuery.lower()

    for product in inventory:
        if (
            searchQuery == str(product.code).lower()
            or searchQuery == product.name.lower()
        ):
            return {"product": product.show_info()}

    return {"message": "Product not found."}


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

    df = DataFrame(data)
    filename = "inventory_export.xlsx"
    df.to_excel(filename, index=False)

    print(f"\n--- Excel file created: {filename} ---")

    # Open file in default spreadsheet app
    webbrowser_open(filename)


# Ask user to confirm saving session changes to the original file
@app.post("/confirm_save_changes")
def confirm_save_changes(confirm: int):
    if confirm == 1:
        with (
            open(SESSION_FILE, "r", encoding="utf-8") as src,
            open(ORIGINAL_FILE, "w", encoding="utf-8", newline="") as dst,
        ):
            dst.write(src.read())
        return {"message": f"Changes saved to {ORIGINAL_FILE}"}
    elif confirm == 2:
        return {"message": "Changes discarded."}
    else:
        return {"message": "Invalid choice."}
