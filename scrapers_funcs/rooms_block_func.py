from bs4 import BeautifulSoup
import re

def page_scraper_room_block(resHtml, hotelid):
    # meal_facilities_const = [1, 166, 167, 168, 169, 170, 171, 217, 218, 219, 220]
    result_room_block_upz = []
    # print('hello room block')

    try:   
        soup1 = BeautifulSoup(resHtml, "lxml")      
    except Exception as ex:
        # print(f"str102___{ex}") 
        return None 

    try:
        all_sripts_list = []
        scripts_fraction_list = []
        all_scripts_str = ''
        all_sripts_list = soup1.find_all('script')
        for fr in all_sripts_list:
            all_scripts_str += str(fr) + '\n'
        scripts_fraction_list = all_scripts_str.split('{}')           
        section = soup1.find('section', class_='roomstable')
        list_elements = section.find_all('div', recursive=False)
        for i, item in enumerate(list_elements):
            try:
                room_id = ''
                name_room = ''
                gross_price = 'api info'
                currency = 'api info'
                max_occupancy = 0
                nr_children = 0
                nr_adults = 0
                mealplan = ''
                all_inclusive = ''
                room_surface_in_m2 = '' 
                # all_facilities_of_room = ''            
                try:
                    room_id_pre = item.find('a').get('href')            
                    room_id = re.findall('\d+', room_id_pre)[0]                
                except:
                    room_id = ''
                    continue
    
                try:
                    name_room_pre = item.find('a')
                    name_room = name_room_pre.get_text(strip=True, separator="\n")
                except:
                    name_room = ''
                    continue

                try:            
                    pattern1 = f'"roomId":{room_id}.*__typename":"RTRoomCard".*"description".*"hasRoomInventory".*' 
                       
                    for fr in scripts_fraction_list:
                        match1 = re.search(pattern1, fr)                                   
                        if match1:
                            match_general_block = match1.group()

                            try:
                                match_allow_children = re.search(r'"maxChildren":\d', match_general_block)
                                # print(match_allow_children.group())
                                nr_children = match_allow_children.group().split(':')[1].strip() 
                            except:
                                nr_children = 0
                            try:
                                match_nr_adults = re.search(r'"maxPersons":\d', match_general_block)
                                # print(match_nr_adults.group())
                                nr_adults = match_nr_adults.group().split(':')[1].strip() 
                            except:
                                nr_adults = 0
                           
                    try:
                        max_occupancy = int(nr_children) + int(nr_adults)
                    except:
                        max_occupancy = 0  
                    # print(max_occupancy)          
                except:
                    pass
    
                try:
                    result_room_block_upz.append({
                        "hotelid": int(hotelid),
                        'room_id': int(room_id),                    
                        # 'gross_price': float(gross_price), 
                        # 'currency': currency,  
                        'room_name': name_room,                  
                        'nr_children': nr_children,
                        'max_occupancy': max_occupancy,
                        # 'mealplan': mealplan,
                        # 'room_surface_in_m2': float(room_surface_in_m2),
                        'nr_adults': nr_adults,
                        # 'all_inclusive': int(all_inclusive),

                    })
                except Exception as ex:
                    # print(f"150____{ex}") 
                    pass
                    # return None 
            except:
                continue
    except:
        # print(f"154____{ex}")
        # pass
        return None
    try:
        # print(result_room_block_upz)
        return result_room_block_upz
    except:
        return None

# python rooms_block_func.py






# try:
#     for fs in meal_facilities_set_list:
#         all_facilities_of_room += facilities_data.roomfacility[str(fs)] +'\n'
# except:
#     all_facilities_of_room = "not found"    
#                     # 'all_facilities_of_room': str(all_facilities_of_room),  