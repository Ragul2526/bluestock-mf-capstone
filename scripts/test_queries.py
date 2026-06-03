#This  python program is to check if the queries.sql are working perfectly
import sqlite3
import pandas as pd

conn = sqlite3.connect("../data/db/bluestock_mf.db")

with open("../sql/queries.sql", "r") as f:
    sql_text = f.read()

queries = sql_text.split(";")

for i, query in enumerate(queries, start=1):

    query = query.strip()

    if not query:
        continue

    lines = [
        line
        for line in query.splitlines()
        if not line.strip().startswith("--")
    ]

    query = "\n".join(lines).strip()

    if not query:
        continue

    print(f"\n{'='*60}")
    print(f"QUERY {i}")
    print(f"{'='*60}")

    try:
        result = pd.read_sql_query(query, conn)
        print(result.head())
    except Exception as e:
        print("ERROR:", e)

conn.close()