from itertools import islice
seed = __import__('seed')

connection = seed.connect_db()
if connection:
    seed.create_database(connection)
    connection.close()
    print(f"connection successful")

    connection = seed.connect_to_prodev()

'''
    if connection: 
        seed.create_table(connection)
        # seed.insert_data_from_csv(connection, 'user_data.csv')
        cursor = connection.cursor()
        cursor.execute(f"SELECT SCHEMA_NAME FROM INFORMATION_SCHEMA.SCHEMATA WHERE SCHEMA_NAME = 'ALX_prodev';")
        result = cursor.fetchone()
        if result:
            print(f"Database ALX_prodev is present ")
        cursor.execute(f"SELECT * FROM user_data LIMIT 5;")
        rows = cursor.fetchall()
        print(rows)
        cursor.close()
'''

'''
streamer = __import__('0-stream_users')

# iterate over the generator function and print only the first 6 rows
for user in islice(streamer.stream_users(), 6):
    print(user)
'''

batcher = __import__('1-batch_processing')
for user in islice(batcher.stream_users_in_batches(2), 6):
    print(user)
batcher.stream_users_in_batches(2)
# batcher.batch_processing(2)