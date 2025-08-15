import sqlite3

def create_connection():
    return sqlite3.connect("store.db")

def setup_database():
    conn = create_connection()
    cursor = conn.cursor()

    # Categories table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS categories (
        category_id INTEGER PRIMARY KEY AUTOINCREMENT,
        category_name TEXT NOT NULL UNIQUE
    )
    """)

    # Products table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS products (
        product_id INTEGER PRIMARY KEY AUTOINCREMENT,
        product_name TEXT NOT NULL,
        price REAL NOT NULL,
        stock INTEGER NOT NULL,
        category_id INTEGER,
        FOREIGN KEY (category_id) REFERENCES categories(category_id)
    )
    """)

    # Orders table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS orders (
        order_id INTEGER PRIMARY KEY AUTOINCREMENT,
        product_id INTEGER,
        quantity INTEGER NOT NULL,
        total_price REAL NOT NULL,
        order_date TEXT,
        FOREIGN KEY (product_id) REFERENCES products(product_id)
    )
    """)

    # Insert sample categories
    sample_categories = ["Electronics", "Clothing", "Footwear", "Accessories"]
    for cat in sample_categories:
        cursor.execute("INSERT OR IGNORE INTO categories (category_name) VALUES (?)", (cat,))

    # Insert sample products if none exist
    cursor.execute("SELECT COUNT(*) FROM products")
    count = cursor.fetchone()[0]
    if count == 0:
        sample_products = [
            ("Laptop", 55000, 10, 1),
            ("Smartphone", 25000, 15, 1),
            ("Headphones", 1500, 25, 1),
            ("T-shirt", 500, 50, 2),
            ("Jeans", 1200, 30, 2),
            ("Shoes", 2000, 20, 3),
            ("Watch", 3000, 10, 4)
        ]
        cursor.executemany("INSERT INTO products (product_name, price, stock, category_id) VALUES (?, ?, ?, ?)", sample_products)

    conn.commit()
    conn.close()

if __name__ == "__main__":
    setup_database()
    print("✅ Database setup completed with sample categories and products!")
