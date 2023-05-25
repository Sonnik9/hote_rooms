def db_wrtr(total, n2):
    try:
        import mysql.connector
        from mysql.connector import connect, Error 
        from . import config_real
        print('hello db_writerr room')

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

        print(len(total))
        resRooms = []
        resRoomsBlock = []
        set_id_list = set()
        room_white_set = set()
        roomBlock_white_set = set()
        whiteList = []
        n = n2/1000
        try:
            for t in total:
                try:
                    resRooms += t[0]
                except:
                    continue

            resRooms = list(filter(None, resRooms))
            if len(resRooms) == 0:
                return

            try:
                query4 = "INSERT INTO upz_hotels_rooms_test1 (hotelid, roomid, endescription, allow_children, photo1, photo2, photo3, photo4, photo5, photo6, photo7, photo8, photo9, photo10, private_bathroom_highlight, bed_configurations) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"

                for item in resRooms:
                    try:
                        values = (item["hotelid"], item["roomid"], item["endescription"], item["allow_children"], item["photo1"], item["photo2"], item["photo3"], item["photo4"], item["photo5"], item["photo6"], item["photo7"], item["photo8"], item["photo9"], item["photo10"], item["private_bathroom_highlight"], item["bed_configurations"])
                        cursor.execute(query4, values)
                        room_white_set.add(item["hotelid"])
                        set_id_list.add(item["hotelid"])
                    except Exception as ex:
                        print(ex)
                        continue

                conn.commit()
            except:
                pass

            try:
                query4 = "INSERT INTO upz_hotels_rooms (hotelid, roomid, endescription, allow_children, photo1, photo2, photo3, photo4, photo5, photo6, photo7, photo8, photo9, photo10, private_bathroom_highlight, bed_configurations) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"

                for item in resRooms:
                    try:
                        values = (item["hotelid"], item["roomid"], item["endescription"], item["allow_children"], item["photo1"], item["photo2"], item["photo3"], item["photo4"], item["photo5"], item["photo6"], item["photo7"], item["photo8"], item["photo9"], item["photo10"], item["private_bathroom_highlight"], item["bed_configurations"])
                        cursor.execute(query4, values)
                        room_white_set.add(item["hotelid"])
                        set_id_list.add(item["hotelid"])
                    except Exception as ex:
                        print(ex)
                        continue

                conn.commit()
            except:
                pass

            for t in total:
                try:
                    resRoomsBlock += t[1]
                except:
                    continue

            resRoomsBlock = list(filter(None, resRoomsBlock))

            try:
                query5 = "INSERT INTO upz_hotels_rooms_blocks_test1 (hotelid, room_id, room_name, nr_children, max_occupancy, nr_adults) VALUES (%s, %s, %s, %s, %s, %s)"

                for item in resRoomsBlock:
                    try:
                        values = (item["hotelid"], item["room_id"], item["room_name"], item["nr_children"], item["max_occupancy"], item["nr_adults"])
                        cursor.execute(query5, values)
                        roomBlock_white_set.add(item["hotelid"])
                        set_id_list.add(item["hotelid"])
                    except Exception as ex:
                        print(ex)
                        continue

                conn.commit()
            except Exception as ex:
                print(ex)  

            try:
                query5 = "INSERT INTO upz_hotels_rooms_blocks (hotelid, room_id, room_name, nr_children, max_occupancy, nr_adults) VALUES (%s, %s, %s, %s, %s, %s)"

                for item in resRoomsBlock:
                    try:
                        values = (item["hotelid"], item["room_id"], item["room_name"], item["nr_children"], item["max_occupancy"], item["nr_adults"])
                        cursor.execute(query5, values)
                        roomBlock_white_set.add(item["hotelid"])
                        set_id_list.add(item["hotelid"])
                    except Exception as ex:
                        print(ex)
                        continue

                conn.commit()
            except Exception as ex:
                print(ex)  

            try:
                room_white = list(room_white_set)
                roomBlock_white = list(roomBlock_white_set)                   
                whiteList = [item for item in roomBlock_white if item in room_white]
            except Exception as ex:
                print(ex)
            # print(whiteList)
            try:
                query9 = "UPDATE upz_hotels SET room = %s WHERE hotel_id = %s"

                for item in whiteList:
                    try:
                        try:
                            find_query = "SELECT hotel_id FROM upz_hotels WHERE hotel_id = %s"
                            # print("true1")
                            cursor.execute(find_query, (item,))
                            # print("true2")
                            row = cursor.fetchone()
                            # print("true3")
                        except Exception as ex:
                            print(f"db_writerr__str87__{ex}")

                        if row:
                            try:
                            #    print('true4')
                                cursor.execute(query9, (1, item))
                            #    print('true5')
                            except Exception as ex:
                                print(f"db_writerr__str90__{ex}")

                    except Exception as ex:
                        print(f"db_writerr__str95__{ex}")
                        continue

                conn.commit()
            except Exception as ex:
                print(ex)
            
            try:
                select_queryF = "SELECT room_flag FROM hotels_simafor WHERE id = %s"
                cursor.execute(select_queryF, (n,))
                row = cursor.fetchone()

                if row:
                    update_query = "UPDATE hotels_simafor SET room_flag = %s WHERE id = %s"
                    cursor.execute(update_query, (1, n))
                    conn.commit()        

            except Exception as ex:
                print(ex)

        except Exception as ex:
            print(ex)

        try:
            cursor.close()
            conn.close()
        except Error as e:
            print(f"Error connecting to MySQL: {e}")
    except:
        pass

    return 

# total = None
# db_opener(total)

# python db_writerrr.py



# resRoomHighlights = []
# with open('result_description__interval_0__1120__Items_982.json', 'r') as f:
#     data_result_descript = json.load(f)
# with open('photos__12_05_2023__16_32__443.json', 'r') as f:
#     resPhoto = json.load(f) 
# with open('facilities__12_05_2023__16_32__1030.json', 'r') as f:
#     resFacilities = json.load(f) 
# with open('room__12_05_2023__16_31__62.json', 'r') as f:
#     resRooms = json.load(f) 
# with open('room_block__12_05_2023__16_31__62.json', 'r') as f:
#     resRoomsBlock = json.load(f)
    # print(resRoomsBlock)


            # query = "UPDATE result_description_test1 SET hotelid = %s, enusname = %s"
