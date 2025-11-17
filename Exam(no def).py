print("Welcome to the Inventory Management System!")

inventory = []

while True:
    menu = "\nMenu:\n1. Add a New Product\n2. Update Product Quantity\n3.Display Product List\n4. Calculate Total Inventory Value\n5. Generate Inventory Report\n6. Exit"
    print(menu)

    choice_input = input("\nEnter your choice (1-6): ")

    if not choice_input.isdigit():
        print("Invalid input. Please enter a number from 1 to 6.\n")
        continue

    choice = int(choice_input)
    if choice < 1 or choice > 6:
        print("Invalid choice. Please select a valid menu option.\n")
        continue


    if choice == 1:
        print("You selected: Add a New Product\n")

        qty_input = input("Enter the number of items you want to add: ")
        if not qty_input.isdigit() or int(qty_input) <= 0:
            print("Invalid number. Please enter a positive integer.\n")
            continue

        quantity = int(qty_input)

        for i in range(quantity):
            print(f"\n--- Product {i+1} ---")
            products = {}

            products["ID"] = input("\nProduct ID: ").strip()
            products["Name"] = input("Product Name: ").strip()

            q = input("Product Quantity: ")
            if not q.isdigit():
                print("Invalid quantity. Must be a number.")
                continue
            products["Quantity"] = int(q)

            p = input("Product Price: ")
            if p.replace('.', '', 1).isdigit() == False:
                print("Invalid price. Must be numeric.")
                continue
            products["Price"] = float(p)

            inventory.append(products)

            back = input("\nType [back] to return to main menu: ").strip().lower()
            while back != "back":
                print("Invalid input. Please type 'back'.")
                back = input("Type [back] to return to main menu: ").strip().lower()

            print("Returning to main menu...\n")
            break


    elif choice == 2:
        print("You selected: Update Product Quantity\n")

        if not inventory:
            print("Inventory is empty. Add products first.\n")
            continue

        product_id = input("Enter the Product ID to update: ").strip()
        found = False

        for item in inventory:
            if item["ID"] == product_id:
                print(f"Current Quantity: {item['Quantity']}")
                new_q = input("Enter new quantity: ")

                if not new_q.isdigit():
                    print("Invalid input. Quantity must be a number.\n")
                    found = True
                    break

                item["Quantity"] = int(new_q)
                print("Quantity updated successfully!")
                found = True
                break

        if not found:
            print("Product ID not found.\n")
            continue

        back = input("\nType [back] to return to main menu: ").strip().lower()
        while back != "back":
            print("Invalid input. Please type 'back'.")
            back = input("Type [back] to return to main menu: ").strip().lower()

        print("Returning to main menu...\n")


    elif choice == 3:
        print("You selected: Display Product List\n")

        if not inventory:
            print("Inventory is empty.\n")
            continue

        print(f"{'ID':<10}{'Name':<16}{'Price':<10}{'Quantity':<10}")
        print("------------------------------------------------------")

        for item in inventory:
            print(f"{item['ID']:<10}{item['Name']:<16}${item['Price']:<10}{item['Quantity']:<10}")

        back = input("\nType [back] to return to main menu: ").strip().lower()
        while back != "back":
            print("Invalid input. Please type 'back'.")
            back = input("Type [back] to return to main menu: ").strip().lower()

        print("Returning to main menu...\n")


    elif choice == 4:
        print("You selected: Calculate Total Inventory Value\n")

        total_value = 0
        for item in inventory:
            total_value += item["Quantity"] * item["Price"]

        print(f"Total Inventory Value: ${total_value}")

        back = input("\nType [back] to return to main menu: ").strip().lower()
        while back != "back":
            print("Invalid input. Please type 'back'.")
            back = input("Type [back] to return to main menu: ").strip().lower()

        print("Returning to main menu...\n")


    elif choice == 5:
        print("You selected: Generate Inventory Report\n")

        print("\nProducts with LOW STOCK (Quantity < 10):")
        print("------------------------------------------")
        for item in inventory:
            if item["Quantity"] < 10:
                print(f"{item['ID']} - {item['Name']} (Qty: {item['Quantity']})")

        highest = max(inventory, key=lambda x: x["Quantity"])

        print("\nProduct with the HIGHEST STOCK:")
        print("------------------------------------------")
        print(f"{highest['ID']} - {highest['Name']} (Qty: {highest['Quantity']})")

        avg_price = sum(item["Price"] for item in inventory) / len(inventory)

        print("\nAverage Price of All Products:")
        print("------------------------------------------")
        print(f"${avg_price}")

        back = input("\nType [back] to return to main menu: ").strip().lower()
        while back != "back":
            print("Invalid input. Please type 'back'.")
            back = input("Type [back] to return to main menu: ").strip().lower()

        print("Returning to main menu...\n")


    elif choice == 6:
        print("Exiting the Inventory Management System. Goodbye!")
        break
