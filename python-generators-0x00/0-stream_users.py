
db = __import__('seed')
# Function that uses a generator to fetch rows one by one from the user's table
# def stream_users(connection):
def stream_users():
    connection = db.connect_to_prodev()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM user_data;")
    while True:
        row = cursor.fetchone()
        if row is None:
            break
        yield row