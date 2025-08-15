from db_setup import setup_database
from product import view_products
from order import place_order, view_orders
from admin import add_category, add_product, update_stock, delete_product, reset_products

def admin_panel():
    while True:
        print("\n--- Admin Panel ---")
        print("1. Add Category")
        print("2. Add Product")
        print("3. Update Stock")
        print("4. Delete Product")
        print("5. Reset Products & Categories (IDs start from 1)")
        print("6. Back to Main Menu")
        choice = input("Enter choice: ")

        if choice == "1":
            add_category()
        elif choice == "2":
            add_product()
        elif choice == "3":
            update_stock()
        elif choice == "4":
            delete_product()
        elif choice == "5":
            reset_products()  # this now resets both products & categories
        elif choice == "6":
            break
        else:
            print("❌ Invalid choice!")


def main_menu():
    setup_database()
    while True:
        print("\n=== E-commerce Store ===")
        print("1. View Products")
        print("2. Place Order")
        print("3. View Orders")
        print("4. Admin Panel")
        print("5. Exit")
        choice = input("Enter choice: ")

        if choice == "1":
            view_products()
        elif choice == "2":
            place_order()
        elif choice == "3":
            view_orders()
        elif choice == "4":
            admin_panel()
        elif choice == "5":
            print("👋 Goodbye!")
            break
        else:
            print("❌ Invalid choice!")

if __name__ == "__main__":
    main_menu()
