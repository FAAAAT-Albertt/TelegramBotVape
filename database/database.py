"""Database sqlite3 for Telegram Bot"""
import asyncio
import sqlite3

con = sqlite3.connect("database/bot.db")
con.row_factory = lambda C, R: { c[0]: R[i] for i, c in enumerate(C.description) }
cur = con.cursor()

cur.execute("""CREATE TABLE IF NOT EXISTS cities
            (id_city INTEGER, city TEXT)""")
con.commit()

cur.execute("""CREATE TABLE IF NOT EXISTS catalogs
            (id_catalog INTEGER, category TEXT, brand TEXT, image TEXT,
            name TEXT, price REAL, count INTEGER)""")
con.commit()

cur.execute("""CREATE TABLE IF NOT EXISTS users
            (id_user INTEGER, user_id INTEGER, user_name TEXT, id_city INTEGER)""")
con.commit()

cur.execute("""CREATE TABLE IF NOT EXISTS orders
            (id_order INTEGER, id_user INTEGER, id_catalog INTEGER, status TEXT)""")
con.commit()

async def insert_catalogs(mas_goods: list) -> None:
    """Function inserts goods to table catalogs"""
    cur.execute("DELETE FROM catalogs")
    con.commit()

    index = 1
    for goods in mas_goods:
        insert_query = f"""INSERT INTO catalogs VALUES
                    ({index}, "{goods['Категория']}", "{goods['Подкатегория']}", "{goods['Картинка']}",
                    "{goods['Название']}", {goods['Цена']}, {goods['Кол-во']})"""
        cur.execute(insert_query)
        con.commit()
        index += 1

async def get_unique_categories() -> dict:
    """Reterns unique categories"""
    select_query = "SELECT DISTINCT category FROM catalogs"
    return cur.execute(select_query).fetchall()

async def get_unique_brand(category) -> dict:
    """Reterns unique categories"""
    select_query = f"SELECT DISTINCT brand FROM catalogs WHERE category = '{category}'"
    return cur.execute(select_query).fetchall()

async def get_first_of_goods(category, brand) -> dict:
    """Reterns goods by brand and category"""
    select_query = f"""SELECT
                    id_catalog, image, name, price, count
                    FROM catalogs WHERE category = '{category}' and brand = '{brand}'"""
    return cur.execute(select_query).fetchall()

async def get_goods_by_id(id_catalog) -> dict:
    """Reterns goods by id_catalog"""
    select_query = f"""SELECT category, brand
                    FROM catalogs WHERE id_catalog = {id_catalog}"""
    select = cur.execute(select_query).fetchone()
    select_query = f"""SELECT
                    id_catalog, image, name, price, count FROM catalogs
                    WHERE category = '{select['category']}' and brand = '{select['brand']}'"""
    return cur.execute(select_query).fetchall(), select['category']

async def insert_cities(mas_city) -> None:
    """Function inserts cities to table cities"""
    cur.execute("DELETE FROM cities")
    con.commit()

    index = 1
    for city in mas_city:
        insert_query = f"""INSERT INTO cities VALUES
                    ({index}, "{city['Город']}")"""
        cur.execute(insert_query)
        con.commit()
        index += 1

async def get_cities() -> list:
    """Function reterns list of city"""
    select_query = "SELECT * FROM cities"
    return cur.execute(select_query).fetchall()

async def check_user(tg_id) -> bool:
    """Function checks whether there is a user in the database"""
    select_query = f"SELECT * FROM users WHERE user_id = {tg_id}"
    select = cur.execute(select_query).fetchone()
    if select is None:
        return False
    return True

async def insert_user(user_id, user_name, id_city) -> None:
    """Function inserts user to the database"""
    select_query = "SELECT * FROM users"
    select = cur.execute(select_query).fetchall()
    if select == []:
        index = 1
    else:
        index = len(select)
    insert_query = f"""INSERT INTO users VALUES
                    ({index}, {user_id}, "{user_name}", {id_city})"""
    cur.execute(insert_query)
    con.commit()

if __name__ == "__main__":
    asyncio.run(get_unique_categories())
