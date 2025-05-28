import mysql.connector

def connect_db():
    """
    connects to the mysql database server.

    Returns:
        MySQLConnection: A connection object to interact with the specified
        MySQL database.
    """
    return mysql.connector.connect(
        host="localhost",
        user="kevin",
        passwd="kevin"
    )

connection = connect_db()

def create_database(connection):
    """
    Creates the ALX_prodev database if it does not already exist.

    Args:
        connection (MySQLConnection): A connection object to interact with the
        specified MySQL database.
    """
    cursor = connection.cursor()
    cursor.execute("CREATE DATABASE IF NOT EXISTS ALX_prodev;")
    cursor.close()

def connect_to_prodev():
    """
    Connects to the ALX_prodev database.

    Returns:
        MySQLConnection: A connection object to interact with the specified
        MySQL database.
    """
    return mysql.connector.connect(
        host="localhost",
        user="kevin",
        passwd="kevin",
        database="ALX_prodev"
    )

def create_table(connection):
    """
    Creates the user_data table with the required fields if it does not already exist.

    Args:
        connection (MySQLConnection): A connection object to interact with the
        specified MySQL database.
    """
            # user_id UUID PRIMARY KEY INDEXED,
    cursor = connection.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS user_data (
            user_id INT PRIMARY KEY AUTO_INCREMENT,
            name VARCHAR(255) NOT NULL,
            email VARCHAR(255) NOT NULL,
            age DECIMAL NOT NULL,
            gender VARCHAR(255)
        )
    """)
    cursor.close()

def insert_data_from_csv(connection, data):
    cursor = connection.cursor()
    cursor.execute(f"LOAD DATA LOCAL INFILE '{data}' INTO TABLE user_data FIELDS TERMINATED BY ',' ENCLOSED BY '\"' LINES TERMINATED BY '\\n' IGNORE 1 LINES;")
    cursor.close()
