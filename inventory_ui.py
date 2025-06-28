# inventory_ui.py

def print_menu():
  print("\n- What can I help you with?")
  print("1. Add Product")
  print("2. Show All Products")
  print("3. Search Product")
  print("4. Delete Product")
  print("5. Exit")

def print_products(products):
    print("\nProduct List:")
    for p in products:
        print(f"{p['code']}: {p['name']} - ${p['price']} ({p['quantity']} in stock)")
