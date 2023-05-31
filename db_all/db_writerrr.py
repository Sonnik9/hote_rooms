def db_wrtr(total, n2):
    try:
        import time
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
        for _ in range(3):
            try:
                conn = mysql.connector.connect(**config)      
                print("Writerr connection established rooms")
                break
            except Error as e:
                print(f"Error connecting to MySQL: {e}")
                time.sleep(3)
                continue
            
        try:
            cursor = conn.cursor() 
        except Error as e:
            print(f"Error connecting to MySQL: {e}")
                # time.sleep(3)
                # continue
            
        try:
            print(len(total))
            resRooms = []
            resRoomsBlock = []
            whiteList = []
            n = int(int(n2)/1000)
        except:
            pass
        try:            
            for t in total:
                try:
                    resRooms += t[0]
                except:
                    continue
            for t in total:
                try:
                    resRoomsBlock += t[1]
                except:
                    continue            
            try:
                resRooms = list(filter(None, resRooms))
                resRoomsBlock = list(filter(None, resRoomsBlock))
            except:
                pass
            if len(resRooms) == 0 and len(resRoomsBlock) == 0:
                try:
                    semaforr(conn, cursor, n)
                except:
                    pass 
                return print('len_=0, len_=0')
            print(f"len_resRooms_before___{len(resRooms)}")
            resRooms = remove_repetitions(resRooms)
            print(f"len_resRooms_arter___{len(resRooms)}")  
            print(f"len_resRoomsBlock_before___{len(resRoomsBlock)}")  
            resRoomsBlock = remove_repetitions(resRoomsBlock)
            print(f"len_resRooms_arter___{len(resRoomsBlock)}")      

        except:
            pass  

        try:
            whiteList = writerr_table(conn, cursor, resRooms, resRoomsBlock)
        except:
            pass
        try:
            changing_hotelsCritery(cursor, conn, whiteList)   
        except:
            pass
        try:
           semaforr(conn, cursor, n)
        except:
            pass 
        try:
            cursor.close()
            conn.close()
        except Error as e:
            print(f"Error connecting to MySQL: {e}")
    except:
        pass
    return

def writerr_table(conn, cursor, resRooms, resRoomsBlock):
    whiteList = []
    room_white = []
    room_white_add = []
    room_white_set = set()
    roomBlock_white = []
    roomBlock_white_add = []
    roomBlock_white_set = set() 
    try:
        query4 = "INSERT INTO upz_hotels_rooms (hotelid, roomid, endescription, allow_children, photo1, photo2, photo3, photo4, photo5, photo6, photo7, photo8, photo9, photo10, private_bathroom_highlight, bed_configurations) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"

        batch_size = 250
        batch_values = []

        for item in resRooms:
            try:
                values = (item["hotelid"], item["room_id"], item["endescription"], item["allow_children"], item["photo1"], item["photo2"], item["photo3"], item["photo4"], item["photo5"], item["photo6"], item["photo7"], item["photo8"], item["photo9"], item["photo10"], item["private_bathroom_highlight"], item["bed_configurations"])
                batch_values.append(values)
                room_white_set.add(item["hotelid"])

                if len(batch_values) >= batch_size:
                    try:
                        cursor.executemany(query4, batch_values)
                        conn.commit()
                        batch_values = []
                    except Exception as ex:
                        print(f"117___{ex}")                        
                        room_white_add = insert_rows_individually_room(conn, cursor, query4, batch_values)
                        room_white += room_white_add
                        batch_values = []
                        continue                   

            except Exception as ex:
                print(f"122___{ex}")
                continue

        if batch_values:
            try:
                cursor.executemany(query4, batch_values)
                conn.commit()
            except Exception as ex:
                print(f"130___{ex}")
                room_white_add = insert_rows_individually_room(conn, cursor, query4, batch_values)
                room_white += room_white_add
    except Exception as ex:
        print(f"123___{ex}")
        pass

    try:
        query5 = "INSERT INTO upz_hotels_rooms_blocks (hotelid, room_id, room_name, nr_children, max_occupancy, nr_adults) VALUES (%s, %s, %s, %s, %s, %s)"

        batch_size = 250
        batch_values = []

        for item in resRoomsBlock:
            try:
                values = (item["hotelid"], item["room_id"], item["room_name"], item["nr_children"], item["max_occupancy"], item["nr_adults"])
                batch_values.append(values)
                roomBlock_white_set.add(item["hotelid"])

                if len(batch_values) >= batch_size:
                    try:
                        cursor.executemany(query5, batch_values)
                        conn.commit()
                        batch_values = []
                    except Exception as ex:
                        print(f"153___{ex}")
                        roomBlock_white_add = insert_rows_individually_block(conn, cursor, query5, batch_values)
                        roomBlock_white += roomBlock_white_add
                        batch_values = []
                        continue

            except Exception as ex:
                print(f"159___{ex}")
                continue

        if batch_values:
            try:
                cursor.executemany(query5, batch_values)
                conn.commit()
            except Exception as ex:
                print(f"167___{ex}")
                roomBlock_white_add = insert_rows_individually_block(conn, cursor, query5, batch_values)
                roomBlock_white += roomBlock_white_add
            
    except Exception as ex:
        print(f"170___{ex}")
 
    try:
        room_white += list(room_white_set)
        roomBlock_white += list(roomBlock_white_set)                   
        whiteList = [item for item in roomBlock_white if item in room_white]
    except Exception as ex:
        print(ex)

    return whiteList


def insert_rows_individually_room(conn, cursor, query, data):
    room_white_set = set()
    room_white = []
    try:
        data = eval(data)
    except:
        data = data
    for hotelid, room_id, endescription, allow_children, photo1, photo2, photo3, photo4, photo5, photo6, photo7, photo8, photo9, photo10, private_bathroom_highlight, bed_configurations in data:
        try:
            values = (hotelid, room_id, endescription, allow_children, photo1, photo2, photo3, photo4, photo5, photo6, photo7, photo8, photo9, photo10, private_bathroom_highlight, bed_configurations)
            cursor.execute(query, values)            
            room_white_set.add(hotelid)
        except Exception as ex:
            print(f"204___: {ex}")
            continue
    try:
        conn.commit()
    except:
        room_white = []
    room_white = list(room_white_set)
    return room_white

def insert_rows_individually_block(conn, cursor, query, data):
    roomBlock_white_set = set()
    roomBlock_white = []
    try:
        data = eval(data)
    except:
        data = data
    for hotelid, room_id, room_name, nr_children, max_occupancy, nr_adults in data:
        try:
            values = (hotelid, room_id, room_name, nr_children, max_occupancy, nr_adults)
            cursor.execute(query, values)            
            roomBlock_white_set.add(hotelid)
        except Exception as ex:
            print(f"226___: {ex}")
            continue
    try:
        conn.commit()
    except:
        roomBlock_white = []

    roomBlock_white = list(roomBlock_white_set)
    return roomBlock_white


def changing_hotelsCritery(cursor, conn, whiteList):
    try:       
        query12 = "UPDATE upz_hotels SET room = %s WHERE hotel_id = %s"

        for item in whiteList:
            try:
                try:
                    find_query = "SELECT hotel_id FROM upz_hotels WHERE hotel_id = %s"                     
                    cursor.execute(find_query, (item,))                      
                    row = cursor.fetchone()                      
                except Exception as ex:
                    print(f"db_writerr__str87__{ex}")

                if row:
                    try:                      
                        cursor.execute(query12, (1, item))                      
                    except Exception as ex:
                        print(f"db_writerr__str90__{ex}")

            except Exception as ex:
                print(f"db_writerr__str95__{ex}")
                continue
        conn.commit()           

    except Exception as ex:
        print(ex)

    return

def semaforr(conn, cursor, n):
    print(n)
    try:
        select_queryF = "SELECT room_flag FROM hotels_simafor WHERE id = %s"
        cursor.execute(select_queryF, (n,))
        row = cursor.fetchone()

        if row:
            update_query = "UPDATE hotels_simafor SET room_flag = %s WHERE id = %s"
            cursor.execute(update_query, (1, n))
            conn.commit()  
            print('hello simafor commit!')      

    except Exception as ex:
        print(ex)

def remove_repetitions(data):
    unique_values = set()
    result = []
    for item in data:
        unil_value = item.get("room_id")
        if unil_value not in unique_values:
            result.append(item)
            unique_values.add(unil_value)
    return result


