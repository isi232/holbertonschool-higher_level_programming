#!/usr/bin/python3
"""
create_db.py

Creates and populates the products.db SQLite database used by
task_04_orm.py. Run this script once before starting the Flask app
so the 'sql' data source has data to read from.
"""
import sqlite3


def create_database():
    """Create the Products table in products.db and seed it with data."""
    conn = sqlite3.connect('products.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Products (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            category TEXT NOT NULL,
            price REAL NOT NULL
        )
    ''')
    cursor.execute('DELETE FROM Products')
    cursor.execute('''
        INSERT INTO Products (id, name, category, price)
        VALUES
        (1, 'Laptop', 'Electronics', 799.99),
        (2, 'Coffee Mug', 'Home Goods', 15.99),
        (3, 'Desk Lamp', 'Home Goods', 24.99),
        (4, 'Wireless Mouse', 'Electronics', 29.99)
    ''')
    conn.commit()
    conn.close()


if __name__ == '__main__':
    create_database()
