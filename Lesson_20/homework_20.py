"""Homework  # 20. SQL."""

# Create a database for an online store with the following tables:
# products: a table for storing information about products, including name,
# description, price, etc.
# categories: a table for product categories.
# products must have a foreign key to the categories table.
# Write an SQL script to create the specified tables.
# Insert several rows of data into each table
# Execute a JOIN query that returns information about products
# and their category names
# Submit the assignment in the format of screenshots to the assignment:
# Screenshots of executing queries to create tables
# Screenshot of executing a join query

import csv
import sqlite3


def create_tables(conn):
    """Create the 'categories' and 'products' tables in the SQLite database.

    Args:
        conn (sqlite3.Connection): The connection object for the SQLite3 db.
    """
    cursor = conn.cursor()
    # Create tables
    cursor.execute("""
                   CREATE TABLE IF NOT EXISTS categories (
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   name TEXT NOT NULL UNIQUE
                   )
                   """)
    cursor.execute("""
                   CREATE TABLE IF NOT EXISTS products (
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   category_id INTEGER NOT NULL,
                   name TEXT NOT NULL,
                   description TEXT,
                   price REAL NOT NULL CHECK(price >= 0),
                   FOREIGN KEY (category_id) REFERENCES categories(id)
                   )
                   """)
    conn.commit()


# Function to load CSV data into the tables
def load_data(conn, encoding='utf-8'):
    """Load data from CSV files into the 'categories' and 'products' tables.

    Args:
        conn(sqlite3.Connection): The connection object for the SQLite3 db.
        encoding(str, optional): The encoding of the CSV files.
    """
    cursor = conn.cursor()

    # Load Categories data
    with open('categories.csv', newline='', encoding=encoding) as category_fl:
        reader = csv.DictReader(category_fl)
        for row in reader:
            # Only insert the category name, SQLite will handle the ID
            cursor.execute("""
                INSERT INTO categories (name) VALUES (?)
            """, (row['name'],))

    # Load Orders data
    with open('products.csv', newline='', encoding=encoding) as products_file:
        reader = csv.DictReader(products_file)
        for row in reader:
            cursor.execute("""
                INSERT INTO products (category_id, name, description, price)
                VALUES (?, ?, ?, ?)
            """, (row['category_id'], row['name'],
                  row['description'], row['price']))

    conn.commit()


# Function to search for orders by customer name
def search_products_by_category(conn):
    """JOIN query to retrieve product details along with their category.

    Args:
        conn(sqlite3.Connection): The connection object for the SQLite3 db.
    """
    cursor = conn.cursor()
    query = """
    SELECT
        Categories.name AS category_name,
        Products.name AS Product_name,
        Products.description,
        Products.price
    FROM Categories
    JOIN Products ON Products.category_id = Categories.id
    ORDER BY categories.name, products.price;
    """
    cursor.execute(query)
    results = cursor.fetchall()

    # Display results
    for row in results:
        print(f'Category: {row[0]}, Product: {row[1]}, '
              f'Description: {row[2]}, Price: {row[3]}')


if __name__ == '__main__':
    # Connect to SQLite database (or create it)
    connection = sqlite3.connect('online_store.db')

    # Create tables
    create_tables(connection)

    # Load data from CSV files
    load_data(connection)

    # JOIN query that returns information about products and their category
    search_products_by_category(connection)

    # Close connection
    connection.close()
