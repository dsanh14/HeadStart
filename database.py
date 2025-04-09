import mysql.connector
from mysql.connector import Error
from config import DB_CONFIG

def create_connection():
    """Create a database connection"""
    try:
        connection = mysql.connector.connect(**DB_CONFIG)
        return connection
    except Error as e:
        print(f"Error connecting to MySQL: {e}")
        return None

def create_tables():
    """Create necessary tables if they don't exist"""
    connection = create_connection()
    if connection:
        try:
            cursor = connection.cursor()
            
            # Create expenses table
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS expenses (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    date DATE NOT NULL,
                    category VARCHAR(50) NOT NULL,
                    amount DECIMAL(10, 2) NOT NULL,
                    description TEXT,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            """)
            
            # Create income table
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS income (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    date DATE NOT NULL,
                    source VARCHAR(50) NOT NULL,
                    amount DECIMAL(10, 2) NOT NULL,
                    description TEXT,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            """)
            
            connection.commit()
            print("Tables created successfully")
        except Error as e:
            print(f"Error creating tables: {e}")
        finally:
            cursor.close()
            connection.close()

def add_expense(date, category, amount, description):
    """Add a new expense record"""
    connection = create_connection()
    if connection:
        try:
            cursor = connection.cursor()
            query = """
                INSERT INTO expenses (date, category, amount, description)
                VALUES (%s, %s, %s, %s)
            """
            cursor.execute(query, (date, category, amount, description))
            connection.commit()
            print("Expense added successfully")
        except Error as e:
            print(f"Error adding expense: {e}")
        finally:
            cursor.close()
            connection.close()

def add_income(date, source, amount, description):
    """Add a new income record"""
    connection = create_connection()
    if connection:
        try:
            cursor = connection.cursor()
            query = """
                INSERT INTO income (date, source, amount, description)
                VALUES (%s, %s, %s, %s)
            """
            cursor.execute(query, (date, source, amount, description))
            connection.commit()
            print("Income added successfully")
        except Error as e:
            print(f"Error adding income: {e}")
        finally:
            cursor.close()
            connection.close()

def get_expenses_by_category():
    """Get total expenses grouped by category"""
    connection = create_connection()
    if connection:
        try:
            cursor = connection.cursor()
            query = """
                SELECT category, SUM(amount) as total
                FROM expenses
                GROUP BY category
            """
            cursor.execute(query)
            return cursor.fetchall()
        except Error as e:
            print(f"Error fetching expenses: {e}")
            return []
        finally:
            cursor.close()
            connection.close()

def get_income_vs_expenses():
    """Get monthly income and expenses"""
    connection = create_connection()
    if connection:
        try:
            cursor = connection.cursor()
            query = """
                SELECT 
                    DATE_FORMAT(date, '%Y-%m') as month,
                    SUM(CASE WHEN table_name = 'income' THEN amount ELSE 0 END) as income,
                    SUM(CASE WHEN table_name = 'expenses' THEN amount ELSE 0 END) as expenses
                FROM (
                    SELECT date, amount, 'income' as table_name FROM income
                    UNION ALL
                    SELECT date, amount, 'expenses' as table_name FROM expenses
                ) as combined
                GROUP BY DATE_FORMAT(date, '%Y-%m')
                ORDER BY month
            """
            cursor.execute(query)
            return cursor.fetchall()
        except Error as e:
            print(f"Error fetching income vs expenses: {e}")
            return []
        finally:
            cursor.close()
            connection.close() 