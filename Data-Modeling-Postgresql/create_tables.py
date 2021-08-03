import psycopg2
from sql_queries import create_table_queries, drop_table_queries

def create_database():
    """
    Description: Creates and connects to the sparkifydb,

    Arguments:
        None 

    Returns:
        the connection and cursor to sparkifydb
    """
    
    # connect to default database
    conn = psycopg2.connect("host=127.0.0.1 dbname=student_randy user=postgres password=datapassword")
    conn.set_session(autocommit=True)
    cur = conn.cursor()
    print("connecting to student_randy db")
    # create sparkify database with UTF8 encoding
    cur.execute("DROP DATABASE IF EXISTS sparkifydb2")
    cur.execute("CREATE DATABASE sparkifydb2 WITH ENCODING 'utf8' TEMPLATE template0")
    print("sparkifydb created")
    # close connection to default database
    conn.close()    
    # connect to sparkify database
    conn = psycopg2.connect("host=127.0.0.1 dbname=sparkifydb2 user=postgres password=datapassword")
    cur = conn.cursor()
    print("connected to sparkifydb")
    return cur, conn


def drop_tables(cur, conn):
    """
    Description: Drops each table using the queries in `drop_table_queries` list.
    Arguments:
        Cursor to the connection and database connection

    Returns:
        None
    """
    for query in drop_table_queries:
        cur.execute(query)
        conn.commit()


def create_tables(cur, conn):
    """
    Description: Creates each table using the queries in `create_table_queries` list. 
    
    Arguments:
        Cursor to the connection and database connection

    Returns:
        None
    """
    for query in create_table_queries:
        cur.execute(query)
        conn.commit()


def main():
    """
    Description:
    - Drops (if exists) and Creates the sparkify database. 
    - Establishes connection with the sparkify database and gets cursor to it.  
    - Drops all the tables.  
    - Creates all tables needed. 
    - Finally, closes the connection. 

    Arguments: None

    Return: None
    """
    cur, conn = create_database()
    
    drop_tables(cur, conn)
    create_tables(cur, conn)

    conn.close()


if __name__ == "__main__":
    main()