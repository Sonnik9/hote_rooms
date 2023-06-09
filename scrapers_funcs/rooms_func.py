from bs4 import BeautifulSoup
import re
from . import facilities_data

def page_scraper_room(resHtml, hotelid):
    # print('hello room')
    result_room_upz = []
    try:
        soup1 = BeautifulSoup(resHtml, "lxml")  
        # print(resHtml)     
    except Exception as ex:
        # print(f"str102___{ex}") 
        # pass
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
                endescription = ''
                allow_children = ''
                private_bathroom_highlight = ''
                beds = ''
                bed_config = 0
                bed_index = []
                apartament_photo_list = []
                try:
                    room_id_pre = item.find('a').get('href')            
                    room_id = re.findall('\d+', room_id_pre)[0]                
                except:
                    room_id = ''
                    continue

                try:
                    pattern_bed = r'\b\d.*?(?:bed|beds)'
                    all_bed_text = item.get_text(strip=True, separator="\n").split('\n')
                    for i, item in enumerate(all_bed_text):
                        matches_bed = re.search(pattern_bed, item)
                        if matches_bed:
                           bed_index.append(i) 
                    try:
                        beds = ' '.join(all_bed_text[bed_index[0]:bed_index[-1]+1])                        
                    except:
                        try:
                            beds  = ' '.join(all_bed_text[bed_index[0]])
                        except:
                            beds = ''
                except:
                    beds = ''           

                try:
                    flagOr = False
                    bedOr = beds.split(' ')

                    for orr in bedOr:
                        if orr == 'or':
                            orFind = beds.split('or')[1]
                            flagOr = True
                            break
                    if flagOr == True:
                        for fnd in orFind:
                            try:
                                bed_config += int(fnd)
                            except:
                                continue
                    else:
                        for orr in bedOr:
                            try:
                                bed_config += int(orr)
                            except:
                                continue
                except:
                    pass

                try:                
                    pattern1 = f'"roomId":{room_id}.*__typename":"RTRoomCard".*"description".*"hasRoomInventory".*' 
                            
                    for fr in scripts_fraction_list:
                        match1 = re.search(pattern1, fr)                   
                        if match1:
                            match_general_block = match1.group()
                        
                            try:
                                match_allow_children = re.search(r'"maxChildren":\d', match_general_block)
                                count_allow_children = match_allow_children.group().split(':')[1].strip() 
                            except:
                                pass
                                # allow_children = 'not found'
                            try:
                                allow_children = int(count_allow_children)
                                if allow_children and allow_children >0:
                                    allow_children = 1
                                else:
                                    allow_children = 0
                            except:
                                allow_children = 0                          
                            try:
                                private_bathroom_highlight = ''
                                try:
                                    bathroom_facilities_list = []
                                    try:
                                        bathroom_facilities_pre = re.search(r'"BATHROOM_PRIVATE","facilities":\[[^]]*?\]', match_general_block)
                                        bathroom_facilities_match = bathroom_facilities_pre.group()
                                        bathroom_facilities_list = int(eval(bathroom_facilities_match.split('"BATHROOM_PRIVATE"')[1].split(':')[1].strip()))
                                    except:
                                        try:
                                            bathroom_facilities_list = int(eval(match_general_block.split('"BATHROOM_PRIVATE"')[1].split('"facilities"')[1].split('"__typename"')[0][1:-3].strip()))
                                            
                                        except:
                                            pattern3 = r'\[(.*?)\]'
                                            match_facilities = re.search(pattern3, bathroom_facilities_match)
                                            bathroom_facilities_list = eval(match_facilities.group())
                                except:
                                    bathroom_facilities_list = []
                                try:
                                    for fs in bathroom_facilities_list:
                                        private_bathroom_highlight += facilities_data.roomfacility[str(fs)] +'\n'
                                        
                                except:                                
                                    pass 
                            except:
                                private_bathroom_highlight = ''
                            try:
                                endescription = match_general_block.split('"description":')[1].split('","hasRoomInventory"')[0][1:]                        
                            except Exception as ex:
                                # print(f"202____{ex}") 
                                endescription = ''

                            try:
                                match_photos_block = match_general_block.split('"photos":[')[1].split(',"isSmoking"')[0]
                                photo_id_list_pre = eval(f"[{match_photos_block}")                     
                                for ind in photo_id_list_pre:
                                    indInd = ind['__ref'].split(':')[1].strip()
                                    subInd =  indInd[:3]
                                    room_photo_link = f"https://cf.bstatic.com/images/hotel/max1024x768/{subInd}/{indInd}.jpg"
                                    apartament_photo_list.append(room_photo_link)
                            except Exception as ex:
                                apartament_photo_list = ''
                                # print(f"215____{ex}") 
                    try:
                        photo1 = apartament_photo_list[0]
                    except:
                        photo1 = ''
                    try:
                        photo2 = apartament_photo_list[1]
                    except:
                        photo2 = ''
                    try:
                        photo3 = apartament_photo_list[2]
                    except:
                        photo3 = ''
                    try:
                        photo4 = apartament_photo_list[3]
                    except:
                        photo4 = ''
                    try:
                        photo5 = apartament_photo_list[4]
                    except:
                        photo5 = ''
                    try:
                        photo6 = apartament_photo_list[5]
                    except:
                        photo6 = ''
                    try:
                        photo7 = apartament_photo_list[6]
                    except:
                        photo7 = ''
                    try:
                        photo8 = apartament_photo_list[7]
                    except:
                        photo8 = ''
                    try:
                        photo9 = apartament_photo_list[8]
                    except:
                        photo9 = ''
                    try:
                        photo10 = apartament_photo_list[9]
                    except:
                        photo10 = ''
                except Exception as ex:
                    # print(f"140____{ex}")  
                    pass
                # try:
                result_room_upz.append({
                    "hotelid": int(hotelid),
                    'room_id': int(room_id),                    
                    'endescription': str(endescription), 
                    'allow_children': int(allow_children),
                    'photo1': photo1,
                    'photo2': photo2,
                    'photo3': photo3,
                    'photo4': photo4,
                    'photo5': photo5,
                    'photo6': photo6,
                    'photo7': photo7,
                    'photo8': photo8,
                    'photo9': photo9,
                    'photo10': photo10,                  
                    'private_bathroom_highlight': private_bathroom_highlight,
                    'bed_configurations': int(bed_config)
                })

                # except Exception as ex:
                    # print(f"150____{ex}") 
                    # pass
                    # return None 
            except:
                continue

    except Exception as ex:
        # print(f"154____{ex}")
        # pass
        return None
    try:
        # print(result_room_upz)
        return result_room_upz
    except:
        return None


# python rooms_func.py

 