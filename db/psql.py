import psycopg2

conn = psycopg2.connect(
    database="pos", user="postgres", password="chris", host="127.0.0.1", port="5432"
)
cur = conn.cursor()

# cur.execute(
#     "CREATE TABLE stocks (id serial PRIMARY KEY NOT NULL,\
#     product_code VARCHAR (10) NOT NULL, \
#     product_name VARCHAR(255) NOT NULL,\
#     product_weight float NOT NULL,\
#     product_price float NOT NULL,\
#     in_stock INT NOT NULL, \
#     sold INT NOT NULL, \
#     ordered DATE NOT NULL, \
#     last_purchase TIMESTAMPTZ, \
#     discount float DEFAULT NULL );"
# )  # create table
cur.execute("CREATE TABLE users(id serial PRIMARY KEY, \
        first_name VARCHAR(255),\
        second_name VARCHAR(255), \
        user_name VARCHAR(255),\
        passwords VARCHAR(255),\
        designation VARCHAR(255))")

# cur.execute("INSERT INTO stocks (id, product_code, product_name, product_weight, product_price, in_stock, ordered, discount)\
#     VALUES (1, 'chris', 'chris','chris','chris','hr')");

# cur.execute("INSERT INTO users (id, first_name, second_name, user_name, passwords, designation )\
#     VALUES (2, 'cathy', 'cathy','cathy','cathy','acc')");

conn.commit()
conn.close()

# selecting all
# conn = psycopg2.connect(database="pos", user="postgres", password="chris", host="127.0.0.1", port="5432")
# cur = conn.cursor()
# cur.execute("SELECT id, first_name, second_name, user_name, passwords, designation  from users")

# rows = cur.fetchall()
# for row in rows:
#     print(row[0],' ',str(row[1]).strip(),' ',row[2].strip(),' ',row[3].strip(),' ',row[4].strip(),' ',row[5].strip())

# conn.close()
