import sqlite3
from random import randint
from datetime import datetime, timedelta

# Connect to the SQLite database (creates a new file if not exists)
conn = sqlite3.connect('/Volumes/Samsung 1TB/baby_food.db')
cursor = conn.cursor()

# Create Products table
cursor.execute('''CREATE TABLE IF NOT EXISTS Products (
                    ProductID INTEGER PRIMARY KEY AUTOINCREMENT,
                    Name TEXT NOT NULL,
                    Brand TEXT,
                    Description TEXT,
                    Category TEXT,
                    AgeGroup TEXT
                )''')

# Create ExpirationDates table
cursor.execute('''CREATE TABLE IF NOT EXISTS ExpirationDates (
                    ExpirationID INTEGER PRIMARY KEY AUTOINCREMENT,
                    ProductID INTEGER NOT NULL,
                    ExpirationDate DATE NOT NULL,
                    Quantity INTEGER,
                    FOREIGN KEY (ProductID) REFERENCES Products(ProductID)
                )''')

# Sample data for Products
products_data = [
    ("Cereal", "Gerber", "Oatmeal cereal for infants", "Cereal", "6-12 months"),
    ("Fruit Puree", "Beech-Nut", "Banana puree", "Puree", "6-9 months"),
    ("Baby Snack", "Plum Organics", "Organic rice crackers", "Snack", "9-12 months"),
]

# Insert sample data into Products table
for product in products_data:
    cursor.execute('''INSERT INTO Products (Name, Brand, Description, Category, AgeGroup)
                      VALUES (?, ?, ?, ?, ?)''', product)

# Sample data for ExpirationDates
expiration_dates_data = []

# Generate random expiration dates for each product
for product_id in range(1, len(products_data) + 1):
    for _ in range(3):  # Generate 3 random expiration dates for each product
        expiration_date = datetime.now() + timedelta(days=randint(30, 365))
        expiration_dates_data.append((product_id, expiration_date.strftime('%Y-%m-%d'), randint(1, 100)))

# Insert sample data into ExpirationDates table
for expiration_date in expiration_dates_data:
    cursor.execute('''INSERT INTO ExpirationDates (ProductID, ExpirationDate, Quantity)
                      VALUES (?, ?, ?)''', expiration_date)

# Commit changes and close connection
conn.commit()
conn.close()

print("Sample database created successfully.")
