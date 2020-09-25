import datetime
import pymysql.cursors

# Connect to the database
connection = pymysql.connect(host='localhost',
                             user='root',
                             password='',
                             db='shop',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

def insert_customer(name, age, address):
    
    with connection.cursor() as cursor:
    # Create a new record
        sql = f"INSERT INTO customer (name, age, address) VALUES('{name}' , {age}, '{address}')"
        cursor.execute(sql)

    # connection is not autocommit by default. So you must commit to save
    # your changes.
    connection.commit()

def insert_product(name, price, qty, weight):

    with connection.cursor() as cursor:
    # Create a new record
        sql = f"INSERT INTO product (name, price, qty, weight) VALUES('{name}' , {price}, {qty}, '{weight}')"
        cursor.execute(sql)

    # connection is not autocommit by default. So you must commit to save
    # your changes.
    connection.commit()


def insert_order(cust_id, prod_id, qty,price, order_date):
    with connection.cursor() as cursor:

        total_price = qty * price
        uid = str(hash(str(datetime.datetime.now())))
        
    # Create a new record
        sql = f"INSERT INTO purchase (uid, cust_id, prod_id,total_price, qty, order_date) VALUES('{uid}' , {cust_id}, {prod_id},{total_price}, {qty}, '{order_date}')"
        cursor.execute(sql)

    # connection is not autocommit by default. So you must commit to save
    # your changes.
    connection.commit()


# insert_customer("ali", 30, "13, Akinwunmi Cresent, Oniru Estate, Lagos")
# insert_product("sneaker", 5000, 12, 1200)
insert_order(1,1,5,40000, "2020-08-10")