db = __import__('seed')

# Function that fetches rows in batches
def stream_users_in_batches(batch_size):
    connection = db.connect_to_prodev()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM user_data;")
    while True:
        rows = cursor.fetchmany(batch_size)
        if not rows:
            break
        yield rows

# Function that processes each batch to filter users over the age of25`
def batch_processing(batch_size):
    for batch in stream_users_in_batches(batch_size):
        for user in batch:
            if not user[3] > 25:
                print(user)
                batch.remove(user)