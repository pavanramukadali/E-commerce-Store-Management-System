import sqlite3
from datetime import datetime

# Ensure table exists and has order_date column
def ensure_orders_table():
    conn = sqlite3.connect("store.db")
    cursor = conn.cursor()

    # Create table if not exists
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS orders (
            order_id INTEGER PRIMARY KEY AUTOINCREMENT,
            product_id INTEGER,
            quantity INTEGER,
            total_price REAL,
            order_date TEXT,
            FOREIGN KEY (product_id) REFERENCES products(product_id)
        )
    """)

    # Check if order_date column exists, add if missing
    cursor.execute("PRAGMA table_info(orders)")
    columns = [col[1] for col in cursor.fetchall()]
    if "order_date" not in columns:
        cursor.execute("ALTER TABLE orders ADD COLUMN order_date TEXT")

    conn.commit()
    conn.close()

def place_order():
    ensure_orders_table()

    conn = sqlite3.connect("store.db")
    cursor = conn.cursor()

    try:
        product_id = int(input("Enter Product ID: "))
        quantity = int(input("Enter Quantity: "))
    except ValueError:
        print("❌ Invalid input! Please enter numbers.")
        conn.close()
        return

    cursor.execute("SELECT price, stock FROM products WHERE product_id=?", (product_id,))
    product = cursor.fetchone()

    if not product:
        print("❌ Product not found!")
        conn.close()
        return

    price, stock = product
    if quantity > stock:
        print("❌ Not enough stock!")
        conn.close()
        return

    total_price = price * quantity
    order_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    cursor.execute("""
        INSERT INTO orders (product_id, quantity, total_price, order_date)
        VALUES (?, ?, ?, ?)
    """, (product_id, quantity, total_price, order_date))

    cursor.execute("UPDATE products SET stock = stock - ? WHERE product_id=?", (quantity, product_id))

    conn.commit()
    conn.close()
    print(f"✅ Order placed! Total: ₹{total_price}")

def view_orders():
    ensure_orders_table()

    conn = sqlite3.connect("store.db")
    cursor = conn.cursor()
    cursor.execute("""
        SELECT o.order_id, p.product_name, o.quantity, o.total_price, o.order_date
        FROM orders o
        JOIN products p ON o.product_id = p.product_id
    """)
    rows = cursor.fetchall()
    conn.close()

    print("\n--- Orders ---")
    print("ID | Product | Quantity | Total | Date")
    for row in rows:
        print(f"{row[0]} | {row[1]} | {row[2]} | ₹{row[3]} | {row[4]}")
