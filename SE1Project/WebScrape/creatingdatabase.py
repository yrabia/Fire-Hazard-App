import sqlite3
conn = sqlite3.connect("dataformap.db")
cur = conn.cursor()

sql = """
    CREATE TABLE DataForMap (
        latitude DOUBLE,
        longitude DOUBLE,
        contained STRING,
        name STRING,
        website STRING
    ) """

cur.execute(sql)
print("DataForMaps has been created.")

conn.commit()
conn.close()