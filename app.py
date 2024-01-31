from flask import Flask, render_template, request, redirect
import psycopg2
import math

app = Flask(__name__)

# Database connection parameters
db_params = {
    'dbname': 'your_database_name',
    'user': 'your_username',
    'password': 'your_password',
    'host': 'your_host',
    'port': 'your_port'
}

def connect_to_database():
    try:
        # Establish a connection to the database
        connection = psycopg2.connect(**db_params)
        cursor = connection.cursor()
        return connection, cursor
    except psycopg2.Error as e:
        # Print an error message if unable to connect to the database
        print("Unable to connect to the database")
        print(e)
        return None, None

def create_customer_table():
    connection, cursor = connect_to_database()

    if connection is not None and cursor is not None:
        # Create a 'customers' table if it doesn't exist
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS customers (
                id SERIAL PRIMARY KEY,
                name VARCHAR(100),
                email VARCHAR(100),
                phone VARCHAR(15),
                notes TEXT
            )
        ''')
        connection.commit()
        connection.close()
    else:
        # Print an error message if database connection fails during table creation
        print("Database connection failed. Unable to create the table.")

def insert_sample_data():
    connection, cursor = connect_to_database()

    if connection is not None and cursor is not None:
        try:
            # Clear existing data and insert sample data into the 'customers' table
            cursor.execute('DELETE FROM customers')
            
            for i in range(1, 101):
                cursor.execute('''
                    INSERT INTO customers (name, email, phone, notes)
                    VALUES (%s, %s, %s, %s)
                ''', (f'Customer {i}', f'customer{i}@example.com', f'555-1000{i:02d}', 'Lorem ipsum dolor sit amet, consectetur adipiscing elit.'))

            connection.commit()
        except Exception as e:
            # Print an error message if there's an issue inserting sample data
            print("Error while inserting sample data:", e)
            connection.rollback()
        finally:
            connection.close()
    else:
        # Print an error message if database connection fails during data insertion
        print("Database connection failed. Unable to insert sample data.")

def get_customer_list(order_by=None, filter_by=None, page=1, limit=10):
    connection, cursor = connect_to_database()

    if connection is not None and cursor is not None:
        # Get the total count of customers for pagination
        query = 'SELECT COUNT(*) FROM customers'

        if filter_by:
            query += f" WHERE name LIKE '%%{filter_by}%%' OR email LIKE '%%{filter_by}%%' OR phone LIKE '%%{filter_by}%%' OR notes LIKE '%%{filter_by}%%'"

        cursor.execute(query)
        total_customers_count = cursor.fetchone()[0]

        # Retrieve customer data with pagination and optional filtering and sorting
        query = 'SELECT * FROM customers'

        if filter_by:
            query += f" WHERE name LIKE '%%{filter_by}%%' OR email LIKE '%%{filter_by}%%' OR phone LIKE '%%{filter_by}%%' OR notes LIKE '%%{filter_by}%%'"

        if order_by:
            query += f" ORDER BY {order_by}"

        query += f" LIMIT {limit} OFFSET {(page - 1) * limit}"

        cursor.execute(query)
        customers = cursor.fetchall()
        connection.close()
        return customers, total_customers_count
    else:
        # Print an error message if database connection fails during data retrieval
        print("Database connection failed. Unable to fetch data.")
        return [], 0
    
    
@app.route('/')
def customer_list():
    order_by = request.args.get('order_by', 'id')
    filter_by = request.args.get('filter_by', '')
    page = request.args.get('page', 1, type=int)
    limit = 10

    # Retrieve customer list with pagination, filtering, and sorting
    customers, total_customers = get_customer_list(order_by=order_by, filter_by=filter_by, page=page, limit=limit)
    total_pages = math.ceil(total_customers / limit)

    return render_template('customer_list.html', customers=customers, order_by=order_by, filter_by=filter_by, page=page, total_pages=total_pages)


@app.route('/add_customer', methods=['GET', 'POST'])
def add_customer():
    if request.method == 'POST':
        # Get customer information from the form and add to the 'customers' table
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        notes = request.form['notes']

        connection, cursor = connect_to_database()

        if connection is not None and cursor is not None:
            cursor.execute('''
                INSERT INTO customers (name, email, phone, notes)
                VALUES (%s, %s, %s, %s)
            ''', (name, email, phone, notes))
            connection.commit()
            connection.close()
            return redirect('/')
        else:
            # Print an error message if database connection fails during customer addition
            print("Database connection failed. Unable to add customer.")
    
    return render_template('add_customer.html')

if __name__ == '__main__':
    # Initialize the application, create the 'customers' table, and insert sample data
    create_customer_table()
    insert_sample_data()
    app.run(debug=True)