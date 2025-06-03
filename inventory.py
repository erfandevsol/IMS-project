projectName = "Inventory Management System"
print(f"\n** Welcome to {projectName} **")

class setProduct:
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

inventory = []   

def add_product():
  print("\n# Please enter your product information. ")
  
  productCode = input("- Enter your product code: ")
  productName = input("- Enter your product name: ")
  productPrice = input("- Enter your price: ")
  productQuantity = input("- Enter your quantity: ")
  
  product = setProduct(productCode, productName, float(productPrice), int(productQuantity))
  
  inventory.append(product)
  
  print("\n--- Product added successfully! ---")
  
def show_all_products():
  if len(inventory) > 0:
    for index in range(len(inventory)):
      print(f"\nProduct {index + 1}")
      inventory[index].show_info()
  else:
    print("\n-!- Inventory is empty -!-")
        
while True:
  print("\n- What can I help you with?")
  print("1. Add Product")
  print("2. Show All Products")
  print("3. Search Product")
  print("4. Exit")

  userChoice = int(input("\nEnter your choice (1,2,3,4): "))
  
  if userChoice == 1:  
    add_product()
  elif userChoice == 2:
    show_all_products()
  elif userChoice == 3:
    print("\n--- Exiting the program. Goodbye! ---")
    break
  elif userChoice == 4:
    print("\n--- Exiting the program. Goodbye! ---")
    break
  else:
    print("\n-!- Invalid choice. Please enter 1, 2, or 3 -!-")
  