import psycopg2

def execute_query(query):
    try:
        conn = psycopg2.connect(
            dbname="your_db_name", user="your_user", password="your_password", host="localhost"
        )
        cur = conn.cursor()
        cur.execute(query)
        result = cur.fetchall()
        for row in result:
            print(row)
        cur.close()
        conn.close()
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    queries = [
        "queries/query_1.sql",
        "queries/query_2.sql",
        "queries/query_3.sql",
        "queries/query_4.sql",
        "queries/query_5.sql",
        "queries/query_6.sql",
        "queries/query_7.sql",
        "queries/query_8.sql",
        "queries/query_9.sql",
        "queries/query_10.sql"
    ]
    for query_file in queries:
        with open(query_file, 'r') as file:
            query = file.read()
            print(f"Executing {query_file}...")
            execute_query(query)
            print()
