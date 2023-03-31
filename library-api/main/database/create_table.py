import psycopg2

def create_tables(params):
    """ create tables in the PostgreSQL database """
    commands = (
        """
        CREATE TABLE IF NOT EXISTS library (
            library_id SERIAL PRIMARY KEY,
            name VARCHAR(1000) NOT NULL,
            author VARCHAR(1000) NOT NULL,
            type VARCHAR(50) NOT NULL,
            isbn_13 INT,
            isbn_10 INT,
            published INT,
            publisher VARCHAR(200),
            copies INT
        )
        """,)
    conn = None
    try:
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        # create table one by one
        for command in commands:
            cur.execute(command)
        cur.close()
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
