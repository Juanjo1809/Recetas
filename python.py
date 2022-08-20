
import sqlite3
from sqlite3 import Error


def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)

    return conn


def create_table(conn, create_table_sql):
    """ create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)



def create_recipe(conn, recipe):
    """
    Create a new project into the projects table
    :param conn:
    :param project:
    :return: project id
    """
    sql = ''' INSERT INTO recipes(name,type,category)
              VALUES(?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, recipe)
    conn.commit()
    return cur.lastrowid


def create_ingredient(conn, ingredient):
    """
    Create a new task
    :param conn:
    :param task:
    :return:
    """

    sql = ''' INSERT INTO ingredients(name,real,recipes_id)
              VALUES(?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, ingredient)
    conn.commit()
    return cur.lastrowid


def main():
    database = r"C:\users\marta\sqlite\db\pythonsqlite.db"

    sql_create_recipes_table = """ CREATE TABLE IF NOT EXISTS recipes (
                                    id integer PRIMARY KEY,
                                    name text NOT NULL,
                                    type text NOT NULL,
                                    category text NOT NULL
                                    ); """

    sql_create_ingredients_table = """CREATE TABLE IF NOT EXISTS ingredients (
                                        id integer PRIMARY KEY,
                                        name text NOT NULL,
                                        real BOOLEAN,
                                        recipes_id integer NOT NULL,
                                    FOREIGN KEY (recipes_id) REFERENCES recipes (id)
                                );"""

    # create a database connection
    conn = create_connection(database)

    # create tables
    if conn is not None:
        # create projects table
        create_table(conn, sql_create_recipes_table)

        # create tasks table
        create_table(conn, sql_create_ingredients_table)
    else:
        print("Error! cannot create the database connection.")

# Insert Data in tables
    if conn is not None:
        # create projects table
        recipe = ('canelones', 'primero', 'tradicional')
        recipeID = create_recipe(conn, recipe)

        # create tasks table
        ingredient = ('tomate', 1, recipeID)
        create_ingredient(conn, ingredient)
    else:
        print("Error! cannot create the database connection.")

print("hola")
if __name__ == '__main__':
    main()