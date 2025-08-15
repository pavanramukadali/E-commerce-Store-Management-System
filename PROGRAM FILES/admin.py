import sqlite3

def add_category():
    conn = sqlite3.connect("store.db")
    cursor = conn.cursor()
    category_name = input("Enter Category Name: ")
    try:
        cursor.execute("INSERT INTO categories (category_name) VALUES (?)", (category_name,))
        conn.commit()
        print(f"✅ Category '{category_name}' added!")
    except sqlite3.IntegrityError:
        print("❌ Category already exists!")
    conn.close()

def add_product():
    conn = sqlite3.connect("store.db")
    cursor = conn.cursor()
    product_name = input("Enter Product Name: ")
    price = float(input("Enter Price: "))
    stock = int(input("Enter Stock: "))
    category_id = int(input("Enter Category ID: "))
    cursor.execute("INSERT INTO products (product_name, price, stock, category_id) VALUES (?, ?, ?, ?)",
                   (product_name, price, stock, category_id))
    conn.commit()
    conn.close()
    print(f"✅ Product '{product_name}' added!")

def update_stock():
    conn = sqlite3.connect("store.db")
    cursor = conn.cursor()
    product_id = int(input("Enter Product ID: "))
    new_stock = int(input("Enter New Stock: "))
    cursor.execute("UPDATE products SET stock=? WHERE product_id=?", (new_stock, product_id))
    conn.commit()
    conn.close()
    print("✅ Stock updated!")

def delete_product():
    conn = sqlite3.connect("store.db")
    cursor = conn.cursor()
    product_id = int(input("Enter Product ID to delete: "))
    cursor.execute("DELETE FROM products WHERE product_id=?", (product_id,))
    conn.commit()
    conn.close()
    print("✅ Product deleted!")

def reset_products():
    conn = sqlite3.connect("store.db")
    cursor = conn.cursor()

    cursor.execute("DELETE FROM products")
    cursor.execute("DELETE FROM categories")
    # Reset AUTOINCREMENT for both tables
    cursor.execute("DELETE FROM sqlite_sequence WHERE name='products'")
    cursor.execute("DELETE FROM sqlite_sequence WHERE name='categories'")

    sample_categories = ["Electronics", "Clothing", "Footwear", "Accessories"]
    for cat in sample_categories:
        cursor.execute("INSERT INTO categories (category_name) VALUES (?)", (cat,))

    cursor.execute("SELECT category_id, category_name FROM categories")
    category_map = {name: cid for cid, name in cursor.fetchall()}

    sample_products = [
        ("Laptop", 55000, 10, category_map["Electronics"]),
        ("Smartphone", 25000, 15, category_map["Electronics"]),
        ("Headphones", 1500, 25, category_map["Electronics"]),
        ("T-shirt", 500, 50, category_map["Clothing"]),
        ("Jeans", 1200, 30, category_map["Clothing"]),
        ("Shoes", 2000, 20, category_map["Footwear"]),
        ("Watch", 3000, 10, category_map["Accessories"])
    ]
    cursor.executemany("INSERT INTO products (product_name, price, stock, category_id) VALUES (?, ?, ?, ?)", sample_products)

    conn.commit()
    conn.close()
    print("✅ All products and categories deleted, IDs reset, sample data re-added!")
