import sqlite3

def init_db():
    conn = sqlite3.connect('price_tracker.db')
    c = conn.cursor()
    
    c.execute('''CREATE TABLE IF NOT EXISTS products
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                  user_id INTEGER,
                  product_url TEXT,
                  product_name TEXT,
                  current_price REAL,
                  target_price REAL,
                  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP)''')
    
    conn.commit()
    conn.close()

def add_product(user_id, product_url, product_name, current_price, target_price):
    conn = sqlite3.connect('price_tracker.db')
    c = conn.cursor()
    
    c.execute('''INSERT INTO products 
                 (user_id, product_url, product_name, current_price, target_price) 
                 VALUES (?, ?, ?, ?, ?)''',
              (user_id, product_url, product_name, current_price, target_price))
    
    conn.commit()
    conn.close()

def get_user_products(user_id):
    conn = sqlite3.connect('price_tracker.db')
    c = conn.cursor()
    
    c.execute('SELECT * FROM products WHERE user_id = ?', (user_id,))
    products = c.fetchall()
    
    conn.close()
    return products
