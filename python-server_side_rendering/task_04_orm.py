#!/usr/bin/python3
"""
task_04_orm.py

Extends the Flask application's /products route to support a third
data source, 'sql', which reads product data from a SQLite database
(products.db) using Python's sqlite3 module.
"""
import csv
import json
import sqlite3
from flask import Flask, render_template, request

app = Flask(__name__)


def read_json(filepath):
    """Read and parse product data from a JSON file.

    Args:
        filepath (str): Path to the JSON file.

    Returns:
        list: A list of product dictionaries.
    """
    with open(filepath, 'r') as file:
        return json.load(file)


def read_csv(filepath):
    """Read and parse product data from a CSV file.

    Args:
        filepath (str): Path to the CSV file.

    Returns:
        list: A list of product dictionaries with 'id' as int and
            'price' as float.
    """
    products = []
    with open(filepath, 'r', newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            products.append({
                'id': int(row['id']),
                'name': row['name'],
                'category': row['category'],
                'price': float(row['price']),
            })
    return products


def read_sql(filepath):
    """Read and parse product data from a SQLite database.

    Args:
        filepath (str): Path to the SQLite database file.

    Returns:
        list: A list of product dictionaries.
    """
    conn = sqlite3.connect(filepath)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    cursor.execute('SELECT id, name, category, price FROM Products')
    rows = cursor.fetchall()
    conn.close()
    return [dict(row) for row in rows]


@app.route('/')
def home():
    """Render the home page."""
    return render_template('index.html')


@app.route('/about')
def about():
    """Render the about page."""
    return render_template('about.html')


@app.route('/contact')
def contact():
    """Render the contact page."""
    return render_template('contact.html')


@app.route('/items')
def items():
    """Read the list of items from items.json and render items.html."""
    with open('items.json', 'r') as file:
        data = json.load(file)
    items_list = data.get('items', [])
    return render_template('items.html', items=items_list)


@app.route('/products')
def products():
    """Display product data from JSON, CSV, or SQL, optionally
    filtered by id.

    Query Parameters:
        source (str): 'json', 'csv', or 'sql'. Determines which data
            source the product data is read from.
        id (int, optional): If provided, only the product with this
            id is displayed.

    Renders:
        product_display.html with either the product list or an
        error message ("Wrong source" / "Product not found").
    """
    source = request.args.get('source')

    if source == 'json':
        data = read_json('products.json')
    elif source == 'csv':
        data = read_csv('products.csv')
    elif source == 'sql':
        try:
            data = read_sql('products.db')
        except sqlite3.Error:
            return render_template(
                'product_display.html', error="Error retrieving data"
            )
    else:
        return render_template('product_display.html', error="Wrong source")

    product_id = request.args.get('id')
    if product_id is not None:
        try:
            product_id = int(product_id)
        except ValueError:
            return render_template(
                'product_display.html', error="Product not found"
            )

        data = [product for product in data if product['id'] == product_id]
        if not data:
            return render_template(
                'product_display.html', error="Product not found"
            )

    return render_template('product_display.html', products=data)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
