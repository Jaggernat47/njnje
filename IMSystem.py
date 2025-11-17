inventory = []

def add_product(inventory):
    print("You selected: Add a New Item\n")
    print("======================================================")
    
    while True:
        try:
            quantity = int(input("Enter the number of items you want to add: "))
            if quantity > 0:
                break
            else:
                print("Quantity must be a positive number.")
        except ValueError:
            print("Invalid input. Please enter a whole number.")

    for i in range(quantity):
        print(f"\n--- Product {i+1} ---")
        
        products = {} 

        products["ID"] = input("\nProduct ID: ")
        products["Name"] = input("Product Name: ")
        
        while True:
            try:
                products["Quantity"] = int(input("Product Quantity: "))
                break
            except ValueError:
                print("Invalid input. Quantity must be a whole number.")

        while True:
            try:
                products["Price"] = float(input("Product Price: "))
                break
            except ValueError:
                print("Invalid input. Price must be a number.")

        inventory.append(products)
        print(f"Product {products['Name']} added to inventory.")
        
    print("======================================================")
    
    option = input("\nType [back] to return to main menu: ").strip().lower()
    if option == "back":
        print("Returning to main menu...\n")
    else:
        print("Error")


def update_product_quantity(inventory):
    print("You selected: Update Product Quantity\n")
    print("======================================================\n")

    print(f"{'ID':<10}{'Name':<16}{'Price':<10}{'Quantity':<10}")
    print("------------------------------------------------------")

    for item in inventory:
        print(f"{item['ID']:<10}{item['Name']:<16}${item['Price']:<10}{item['Quantity']:<10}")
    
    if not inventory:
        print("Inventory is empty. Add products first.")
        print("======================================================")
        return
        
    product_id = input("\nEnter the Product ID to update: ")

    found = False
    for item in inventory:
        if item["ID"] == product_id:
            print(f"Current Quantity: {item['Quantity']}")
            while True:
                try:
                    new_quantity = int(input("Enter new quantity: "))
                    break
                except ValueError:
                    print("Invalid input. Please enter a whole number.")
                    
            item["Quantity"] = new_quantity
            print("Quantity updated successfully!")
            found = True
            break
            
    if not found:
        print("Product ID not found.")
        
    print("======================================================")
    
    option = input("\nType [back] to return to main menu: ").strip().lower()
    if option == "back":
        print("Returning to main menu...\n")
    else:
        print("Error")


def display_product_list(inventory):
    print("You selected: Display Product List\n")
    print("======================================================")
    
    if not inventory:
        print("Inventory is currently empty.")
        print("======================================================")
        return

    print(f"{'ID':<10}{'Name':<16}{'Price':<10}{'Quantity':<10}")
    print("------------------------------------------------------")

    for item in inventory:
        print(f"{item['ID']:<10}{item['Name']:<16}${item['Price']:<10}{item['Quantity']:<10}")
        
    print("------------------------------------------------------")
    print("======================================================")
    

    option = input("\nType [back] to return to main menu: ").strip().lower()
    if option == "back":
        print("Returning to main menu...\n")
    else:
        print("Error")


def calculate_total_value(inventory):
    print("You selected: Calculate Total Inventory Value\n")
    print("======================================================")
    
    if not inventory:
        print("Inventory is empty, total value is $0.00.")
        print("======================================================")
        return
        
    total_value = 0

    for item in inventory:
        total_value += item["Quantity"] * item["Price"]

    print(f"Total Inventory Value: ${total_value:.2f}")
    print("======================================================")
    

    option = input("\nType [back] to return to main menu: ").strip().lower()
    if option == "back":
        print("Returning to main menu...\n")
    else:
        print("Error")


def generate_inventory_report(inventory):
    print("You selected: Generate Inventory Report\n")
    print("======================================================")
    
    if not inventory:
        print("Inventory is empty. No report to generate.")
        print("======================================================")
        return
        
    print("\nProducts with the LOWEST STOCK:")
    low_stock_found = False
    for item in inventory:
        if item["Quantity"] < 10:
            print(f"{item['ID']} - {item['Name']} (Qty: {item['Quantity']})")
            low_stock_found = True
    if not low_stock_found:
        print("No products are currently low in stock.")
    print("------------------------------------------")

    highest = max(inventory, key=lambda x: x["Quantity"])
    print("\nProducts with the HIGHEST STOCK:")
    print(f"{highest['ID']} - {highest['Name']} (Qty: {highest['Quantity']})")
    print("------------------------------------------")

    avg_price = sum(item["Price"] for item in inventory) / len(inventory)
    print("\nAverage Price of All Products:")
    print(f"${avg_price:.2f}")
    print("------------------------------------------")
    print("======================================================")
    
    option = input("\nType [back] to return to main menu: ").strip().lower()
    if option == "back":
        print("Returning to main menu...\n")
    else:
        print("Error")


def main():
    print("Welcome to the Inventory Management System!")
    
    global inventory
    
    while True:
        menu = "\nMenu:\n1. Add a New Product\n2. Update Product Quantity\n3. Display Product List\n4. Calculate Total Inventory Value\n5. Generate Inventory Report\n6. Exit"
        print(menu)
        
        try:
            choice = int(input("\nEnter your choice (1-6): "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue
            
        if choice == 1:
            add_product(inventory)
        elif choice == 2:
            update_product_quantity(inventory)
        elif choice == 3:
            display_product_list(inventory)
        elif choice == 4:
            calculate_total_value(inventory)
        elif choice == 5:
            generate_inventory_report(inventory)
        elif choice == 6:
            print("Exiting the Inventory Management System. Goodbye! ??")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    main()