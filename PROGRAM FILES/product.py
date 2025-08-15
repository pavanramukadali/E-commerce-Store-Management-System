import sqlite3

def view_products():
    conn = sqlite3.connect("store.db")
    cursor = conn.cursor()
    cursor.execute("""
        SELECT p.product_id, p.product_name, p.price, p.stock, c.category_name
        FROM products p
        LEFT JOIN categories c ON p.category_id = c.category_id
    """)
    rows = cursor.fetchall()
    conn.close()

    print("\n--- Products ---")
    print("ID | Name | Price | Stock | Category")
    for row in rows:
        print(f"{row[0]} | {row[1]} | {row[2]} | {row[3]} | {row[4]}")
