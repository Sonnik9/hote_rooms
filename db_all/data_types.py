def db_types():
    import mysql.connector
    from mysql.connector import connect, Error 
    from . import config_real
    print('hello db_writerr')

    config = {
        'user': config_real.user,
        'password': config_real.password,
        'host': config_real.host,
        'port': config_real.port,
        'database': config_real.database,      
    }

    try:
        conn = mysql.connector.connect(**config)      
        print("Writerr connection established2")
    except Error as e:
        print(f"Error connecting to MySQL: {e}")
    
    try:
        cursor = conn.cursor() 
    except Error as e:
        print(f"Error connecting to MySQL: {e}")


    resPhoto = []
    # Столбец: id, Тип данных: int(11)
    # Столбец: hotelid, Тип данных: int(11)
    # Столбец: photo_id, Тип данных: int(11)
    # Столбец: tags, Тип данных: varchar(255)
    # Столбец: url_square60, Тип данных: varchar(255)
    # Столбец: url_max, Тип данных: varchar(255)
    resDescription = []
    # Столбец: id, Тип данных: int(11)
    # Столбец: hotelid, Тип данных: int(11)
    # Столбец: runame, Тип данных: text
    # Столбец: dename, Тип данных: text
    # Столбец: frname, Тип данных: text
    # Столбец: enusname, Тип данных: text
    # Столбец: esname, Тип данных: text
    # Столбец: ptptname, Тип данных: text
    # Столбец: itname, Тип данных: text
    # Столбец: trname, Тип данных: text
    # Столбец: arname, Тип данных: text
    # Столбец: zhcnname, Тип данных: text
    # Столбец: idname, Тип данных: text
    resFacilities = []
    # Столбец: id, Тип данных: int(11)
    # Столбец: hotelid, Тип данных: int(9)
    # Столбец: facilitytype_id, Тип данных: mediumint(6)
    # Столбец: name, Тип данных: varchar(255)
    # Столбец: facilitytype_name, Тип данных: varchar(255)
    # Столбец: hotelfacilitytype_id, Тип данных: mediumint(5)
    # Столбец: uniq, Тип данных: varchar(100)
    resRooms = []
    # hotelid, Тип данных: int(11)
    # roomid, Тип данных: int(11)
    # endescription, Тип данных: text
    # allow_children, Тип данных: tinyint(1)
    # photo1, Тип данных: varchar(255)
    # photo2, Тип данных: varchar(255)
    # photo3, Тип данных: varchar(255)
    # photo4, Тип данных: varchar(255)
    # photo5, Тип данных: varchar(255)
    # photo6, Тип данных: varchar(255)
    # photo7, Тип данных: varchar(255)
    # photo8, Тип данных: varchar(255)
    # photo9, Тип данных: varchar(255)
    # photo10, Тип данных: varchar(255)
    # private_bathroom_highlight, Тип данных: varchar(255)
    # bed_configurations, Тип данных: tinyint(3)
    resRoomsBlock = []
    # hotelid, Тип данных: int(11)
    # room_id, Тип данных: int(11)
    # gross_price, Тип данных: float
    # currency, Тип данных: varchar(15)
    # room_name, Тип данных: varchar(255)
    # nr_children, Тип данных: tinyint(3)
    # max_occupancy, Тип данных: smallint(4)
    # mealplan, Тип данных: varchar(255)
    # room_surface_in_m2, Тип данных: float
    # nr_adults, Тип данных: smallint(4)
    # all_inclusive, Тип данных: tinyint(1)

 
    try:
        # query = "DESCRIBE upz_hotels_photos;"
        # query = "DESCRIBE upz_hotels_description;"
        # query = "DESCRIBE upz_hotels_facilityties;"
        # query = "DESCRIBE upz_hotels_review;"
        # query = "DESCRIBE upz_hotels_rooms;"
        # query = "DESCRIBE upz_hotels_rooms_blocks;"
       
        
        
        cursor.execute(query)

        # Извлечение первой строки результата
        row = cursor.fetchone()

        # Вывод информации о столбцах
        while row is not None:
            column_name = row[0]
            data_type = row[1]
            print(f"{column_name} {data_type.upper()},")
            row = cursor.fetchone()

    except Exception as ex:
        print(ex)
        pass


    try:
        cursor.close()
        conn.close()
    except Error as e:
        print(f"Error connecting to MySQL: {e}")

    return 


db_types()

# total = None
# db_opener(total)

# python db_writerrr.py
# python -m db_all.data_types

