def db_opener(n1, n2):
    import mysql.connector
    from mysql.connector import connect, Error 
    from . import config_real
    print(n1, n2)
    data_DB = []
    config = {
        'user': config_real.user,
        'password': config_real.password,
        'host': config_real.host,
        'port': config_real.port,
        'database': config_real.database,      
    }

    try:
        conn = mysql.connector.connect(**config)      
        print("REader connection established")
    except Error as e:
        print(f"Error connecting to MySQL: {e}")
    
    try:
        cursor = conn.cursor() 
    except Error as e:
        print(f"Error connecting to MySQL: {e}")

    try:
        # query_last_item = "SELECT COUNT(*) FROM upz_hotels;"
        # cursor.execute(query_last_item)
        # # # Извлечение результата запроса
        # last_item = cursor.fetchone()[0]
        # # p2 = int(last_item) - n1
        # # p1 = int(last_item) - n2
        # p2 = int(last_item) - 150
        # p1 = int(last_item) - 160
        # # # n1 = n2 - 50
        # # # n1, n2 = 0, 2
        # # print(n1, n2)

        select_query  = ("SELECT id, hotel_id, url, room FROM upz_hotels "
        f"WHERE id BETWEEN {n1} AND {n2} "
        )
        cursor.execute(select_query)
        hotels_data = cursor.fetchall()
    except Exception as e:
        print(f"db_reader___str46: {e}")

    try:
        for id, hotel_id, url, room in hotels_data:
            data_DB.append({
                'id': id,
                'hotel_id': hotel_id,
                'url': url,
                'room': room
            })
            # print(hotel_id)
    except Exception as ex:
        print(f"source_DB_hotel_46str___{ex}")    

    try:
        cursor.close()
        conn.close()
        # print(result[100000:100002])
    except Error as e:
        print(f"Error connecting to MySQL: {e}")
    print(f"data_DB _____{data_DB[0]}")
    print(f"data_DB _____{data_DB[-1]}")
    # print(f"data_DB _____{data_DB[-1]}")
    return data_DB





# n1, n2 = 0, 0
# db_opener(n1, n2)

# python db_reader.py
# python -m db_all.db_reader



# select_query  = ("SELECT id, hotel_id, url, fotos, description, room, facility, otziv FROM upz_hotels ")
