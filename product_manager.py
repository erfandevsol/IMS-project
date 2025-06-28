# product_manager.py

import os
import csv

CSV_FILE = "inventory.csv"

def load_products():
    products = []
    if not os.path.exists(CSV_FILE):
        return
    with open(CSV_FILE, newline="", encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            row["code"] = int(row["code"])
            row["name"] = row["Name"]
            row["price"] = float(row["price"])
            row["quantity"] = int(row["quantity"])
            products.append(row)
    return products


def save_products(products):
    with open(CSV_FILE, "w", newline="", encoding="utf-8") as csvfile:
        fieldnames = ["Code", "Name", "Price", "Quantity"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(products)


def find_product(products, code):
    for product in products:
        if product["code"] == code:
            return product
    return None
