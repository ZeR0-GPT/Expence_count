from database import create_connection

def add_expense(category, amount, date, description=""):
    conn = create_connection()
    conn.execute("INSERT INTO expenses (category, amount, date, description) VALUES (?, ?, ?, ?)",
                 (category, amount, date, description))
    conn.commit()
    conn.close()

def get_all_expenses():
    conn = create_connection()
    cursor = conn.execute("SELECT * FROM expenses ORDER BY date DESC")
    rows = cursor.fetchall()
    conn.close()
    return rows

def get_total_by_category():
    conn = create_connection()
    cursor = conn.execute("SELECT category, SUM(amount) FROM expenses GROUP BY category")
    rows = cursor.fetchall()
    conn.close()
    return rows