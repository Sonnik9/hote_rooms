def create_tables():
    import mysql.connector
    from mysql.connector import connect, Error 
    from . import config_real

    config = {
        'user': config_real.user,
        'password': config_real.password,
        'host': config_real.host,
        'port': config_real.port,
        'database': config_real.database,      
    }

    try:
        conn = mysql.connector.connect(**config)      
        print("Connection2 established")
    except Error as e:
        print(f"Error connecting to MySQL: {e}")
    
    try:
        cursor = conn.cursor() 
    except Error as e:
        print(f"Error connecting to MySQL: {e}")

    # try:
    #    cursor.execute("DROP TABLE upz_hotels_photos_test1")
    # except:
    #     pass 

    # try:
    #     cursor.execute("DROP TABLE upz_hotels_description_test1")
    # except:
    #     pass 

    # try:
    #    cursor.execute("DROP TABLE upz_hotels_facilityties_test1")
    # except:
    #     pass 
    # try:
    #     cursor.execute("DROP TABLE upz_hotels_rooms")
    # except:
    #     pass 
    # try:
    #     cursor.execute("DROP TABLE upz_hotels_rooms_blocks")
    # except:
    #     pass
    # try:
    #    cursor.execute("DROP TABLE black_list_test2")
    # except:
    #     pass

    create_table_query1 = '''
    CREATE TABLE upz_hotels_photos_test1 (
        id INT AUTO_INCREMENT PRIMARY KEY,
        hotelid INT(11),
        photo_id INT(11),
        tags VARCHAR(255),
        url_square60 VARCHAR(255),
        url_max VARCHAR(255)
    )
    '''
    alert_table_query1 = '''
    ALTER TABLE result_photos_test2
    MODIFY tags TEXT

'''
    create_table_query2 = '''
    CREATE TABLE upz_hotels_description_test1 (
        id INT AUTO_INCREMENT PRIMARY KEY,
        hotelid INT(11),
        runame TEXT,
        dename TEXT,
        frname TEXT,
        enusname TEXT,
        esname TEXT,
        ptptname TEXT,
        itname TEXT,
        trname TEXT,
        arname TEXT,
        zhcnname TEXT,
        idname TEXT
    )
    '''

    create_table_query3 = '''
    CREATE TABLE upz_hotels_facilityties_test1 (
        id INT AUTO_INCREMENT PRIMARY KEY,
        hotelid INT(9),
        facilitytype_id MEDIUMINT(6),
        name VARCHAR(255),
        facilitytype_name VARCHAR(255),
        hotelfacilitytype_id MEDIUMINT(5),
        uniq VARCHAR(100)    
    )
    '''
    create_table_query4 = '''
    CREATE TABLE upz_hotels_rooms (
        id INT AUTO_INCREMENT PRIMARY KEY,
        hotelid INT(15),
        roomid INT(15),
        endescription TEXT,
        allow_children TINYINT(1),
        photo1 VARCHAR(255),
        photo2 VARCHAR(255),
        photo3 VARCHAR(255),
        photo4 VARCHAR(255),
        photo5 VARCHAR(255),
        photo6 VARCHAR(255),
        photo7 VARCHAR(255),
        photo8 VARCHAR(255),
        photo9 VARCHAR(255),
        photo10 VARCHAR(255),
        private_bathroom_highlight VARCHAR(255),
        bed_configurations TINYINT(3),
        UNIQUE (roomid) 
    )
    '''

    alert_table_query2 = '''
    ALTER TABLE upz_hotels_rooms
    MODIFY bed_configurations INT
    '''

    
    create_table_query5 = '''
    CREATE TABLE upz_hotels_rooms_blocks (
        id INT AUTO_INCREMENT PRIMARY KEY,
        hotelid INT(15),
        room_id INT(15),
        gross_price FLOAT,
        currency VARCHAR(15),
        room_name VARCHAR(255),
        nr_children TINYINT(3),
        max_occupancy SMALLINT(4),
        mealplan VARCHAR(255),
        room_surface_in_m2 FLOAT,
        nr_adults SMALLINT(4),
        all_inclusive TINYINT(1),
        UNIQUE (room_id)
           
    )
    '''
    # cursor.execute(create_table_query1)
    # cursor.execute(create_table_query2)
    # cursor.execute(create_table_query3)
    # cursor.execute(create_table_query4)
    # cursor.execute(create_table_query5)
    cursor.execute(alert_table_query2)

    cursor.close()
    conn.close()
    
    return print("the tables was created successfully")


create_tables()


# python create_tables_db.py
# python -m db_all.create_tables_db


# sudo mysql -u root -p

# CREATE USER 'sonnik12'@'localhost' IDENTIFIED BY '6687vono';
# CREATE DATABASE upz_hotels_copy1;
# GRANT ALL PRIVILEGES ON upz_hotels_copy1.* TO 'sonnik12'@'localhost';

# FLUSH PRIVILEGES;
# EXIT;
