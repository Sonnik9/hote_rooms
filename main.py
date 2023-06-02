import requests
from fake_useragent import UserAgent
import random 
from random import choice
import time
import math
import re
import atexit
import shutil
import tempfile
import sys
from joblib import Parallel, delayed
from scrapers_funcs import rooms_func, rooms_block_func
from db_all import db_reader, db_writerrr

uagent = UserAgent()

# //////////////spart headers start///////////////////////////////

def random_headers():
    
    desktop_accept = [
        'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',     
        'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',     
        'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',     
        'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',     
        'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',     
        'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',     
        'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',                
        ]
    device_memoryHelper = [2,4,8,16,32]
    sett = set()
    finHeaders = []    
    finfinH = {}   
 
    headFront = [{
            'authority': 'www.booking.com',
            'accept': choice(desktop_accept), 
            'User-Agent': uagent.random,  
            'accept-language': 'en-US,en;q=0.8',
            # 'accept-language': 'ru-RU,ru;q=0.9',         
            # 'accept-language': f"'en-US,en;q=0.8', 'ru-RU,ru;q=0.9', 'uk-Uk,uk;q=0.5'",       
            'origin': 'https://www.booking.com/',
            'device-memory': f'{choice(device_memoryHelper)}'                  
            }
    ]

    headersHelper = [       
            {"sec-fetch-dest": "empty"},
            {"sec-fetch-mode": "cors"},
            {"sec-fetch-site": "same-origin"},
            {"accept-ch": "sec-ch-ua-model,sec-ch-ua-platform-version,sec-ch-ua-full-version"},
            {'cache-control': 'no-cache'},
            {'content-type': 'application/json'},
            {'rtt': '200'},
            {"ect": "4g"},
            {'sec-fetch-user': '?1'},
            {"viewport-width": "386"},            
            {'sec-ch-ua': '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"'},
            {'upgrade-insecure-requests': '1'}
    ]
    headersHelperFormated = []
    strr = ''
    for i in headersHelper[0:len(headersHelper)-random.randrange(0,len(headersHelper))]:
        strr += ((str(choice(headersHelper)))[1:-1]).strip() + ',' + ' '  
         
    sett.add(strr)    
    headersHelperFormated = list(sett)    
    finHeaders = headFront + headersHelperFormated
    finHeaders[1] = eval("{" + finHeaders[1] + "}")    
    finfinH.update(finHeaders[0])
    finfinH.update(finHeaders[1])   
    return finfinH

# //////////////smart headers start///////////////////////////////

# ////////// grendMather_controller block/////////////////////////////////////

def grendMather_controller(data):
    # print('hello controler')
    flagTest = True
    flag_room = True 
    roomInd = 0

    try:
        data_upz_hotels_item = data.split('SamsonovNik')[1]
    except Exception as ex:
        # print(f"48____{ex}")
        pass

    try:
        data_upz_hotels_item_dict = eval(data_upz_hotels_item)
    except Exception as ex:
        # print(f"53____{ex}")
        data_upz_hotels_item_dict = data_upz_hotels_item 
    try:
        hotelid = data_upz_hotels_item_dict["hotel_id"] 
    except Exception as ex:
        # print(f"61____{ex}")
        hotelid = 'not found'
    # print(hotelid)
    try:
        prLi_str = data.split('SamsonovNik')[0]
        try:
            prLi = eval(prLi_str)
        except Exception as ex:
            # print(f"str68___{ex}")
            prLi = prLi_str
            pass
    except Exception as ex:
        # print(f"str72___{ex}")
        pass 
    try:
        link = ''
        link = data_upz_hotels_item_dict["url"] 
        try:
            fixed_url = re.sub(r'\\/', '/', link)  
        except Exception as ex:
            # print(f"74____{ex}")
            fixed_url = data_upz_hotels_item_dict["url"]
        # print(fixed_url)
        # return
    except Exception as ex:
        # print(f"str83___{ex}")
        return [None, None] 
    try:
        roomInd = data_upz_hotels_item_dict["room"]
    except:
        pass
    
    try:
        if roomInd == "1" or roomInd == 1:
            flag_room = False
           
    except:
        pass
    if flag_room == False:  
        return [None, None]     
    else:
        # n_range = 2
        for _ in range(2):
            try:
                result_rooms_upz, upz_hotels_rooms_blocks = '', ''

                proxy_item = {       
                    "https": f"http://{choice(prLi)}"          
                }
                # print(fixed_url)
                try:
                   headerss=random_headers()
                   
                except Exception as ex:
                    print(f"headers281____{ex}")
                # print(headerss)
                
                # k = 2 / random.randrange(1, 5)
                # m = 1 / random.randrange(1, 11)
                # g = random.randrange(1, 5)
                # n = round(g + k + m, 2) 
                # time.sleep(n)  
                try:     
                    r = requests.get(fixed_url, headers=headerss, allow_redirects=False, proxies=proxy_item, timeout=(6.15, 21.15))
                    r.raise_for_status()               
                    if r.status_code == 404: 
                        return [None, None]
                    if r.status_code == 200 and r.text is not None and r.text != '':
                        try:                      
                            try:
                                result_rooms_upz = rooms_func.page_scraper_room(r.text, hotelid)
                            except:
                                result_rooms_upz = None
                        
                            try:
                                upz_hotels_rooms_blocks = rooms_block_func.page_scraper_room_block(r.text, hotelid)
                            except:
                                upz_hotels_rooms_blocks = None

                            if result_rooms_upz or upz_hotels_rooms_blocks is None:
                                continue                             

                        except Exception as ex:
                            # print(f"str225___{ex}")
                            # continue
                            pass
                        break
                    else:
                        continue
                except requests.exceptions.HTTPError as ex:
                    print(f"str44___HTTP error occurred: {ex}") 
                    continue

            except Exception as ex:
                # print(f"237____{ex}")
                continue
                # return [[None], black_list] 
      
        try:
            # print(result_description_upz)
            return [result_rooms_upz, upz_hotels_rooms_blocks] 
        
        except Exception as ex:
            # print(f"220____{ex}")

            return [None, None] 
        
# ////////// grendMather_controller block end/////////////////////////////////////
#         
def proxy_reader():
    with open("proxy_booking.txt", encoding="utf-8") as f1:    
        prLi = ''.join(f1.readlines()).split('\n')
        prLi= list(i.strip() for i in prLi)
        prLi = list(filter(lambda item: item != '', prLi))
    return prLi

def father_multiprocessor(data_upz_hotels, cpu_count):    
    try:
        data_upz_hotels_new = eval(data_upz_hotels)
    except Exception as ex:
        data_upz_hotels_new = data_upz_hotels
    try:
        prLi = proxy_reader()
    except Exception as ex:
        pass

    try:
        data_upz_hotels_args = [f"{prLi}SamsonovNik{item}" for item in data_upz_hotels_new]
    except Exception as ex:
        pass

    def call_grendMather_controller(item):
        return grendMather_controller(item)

    try:
        finRes = Parallel(n_jobs=cpu_count, prefer="threads")(delayed(call_grendMather_controller)(item) for item in data_upz_hotels_args)
    except Exception as ex:
        print(f"284STR__Error: {ex}")
        return None

    return finRes

def pattern_cycles(data, cpu_count, n2):
    # print('helo pattern_cycles')
    finRes = []
    try:
        finRes = father_multiprocessor(data, cpu_count)
    except Exception as ex:
        print(f"250____{ex}")
        pass
    try:
        db_writerrr.db_wrtr(finRes, n2)
    except Exception as ex:
        print(f"255____{ex}")
        pass

def cycles_worker(**args_cycles):

    try:        
        n1=int(args_cycles["n1"])
        n2=int(args_cycles["n2"])
        interval=int(args_cycles["interval"])
        from_item=int(args_cycles["from_item"])
        len_items=int(args_cycles["len_items"])
        counter=int(args_cycles["counter"])
        flag_end_cycles=args_cycles["flag_end_cycles"]
        cpu_count = int(args_cycles["cpu_count"])
    except Exception as ex:
        print(f"441____{ex}")

    try:
        if flag_end_cycles == True:
           return print('Finish')
        else:            
            try:
                counter +=1
                n1 = (counter * interval) - interval + 1 + from_item
                n2 = (counter * interval) + from_item
                interval_chekcer = len_items - n2
                if interval_chekcer <= interval:
                    n2 = len_items
                    flag_end_cycles = True
                    # print(f"362___{n2}")
            except Exception as ex:
                # print(f"343____{ex}")
                pass

            try:  
                print('hello')                
                const_data = db_reader.db_opener(n1, n2)
                # print(const_data)
            except Exception as ex:
                print(f"443____{ex}")
            try:
                pattern_cycles(const_data, cpu_count, n2)
            except:
                pass
            try:
                cleanup_cache()
            except:
                pass
            args_cycles = {              
                'n1': n1,
                'n2': n2,
                'interval': interval,
                'from_item': from_item,
                'len_items': len_items,
                'counter': counter,
                'flag_end_cycles': flag_end_cycles,
                'cpu_count': cpu_count
            }
            try:
                cycles_worker(**args_cycles) 
            except Exception as ex:
                # print(f"408____{ex}")
                pass           

    except Exception as ex:
        # print(f"334____{ex}")
        pass

def cleanup_cache():
    try:
        import os
        try:
            cache_dir = tempfile.mkdtemp()
        except Exception as ex:
            # print(f"386____{ex}")
            pass    
        try:
            if os.path.exists("__pycache__"):
                shutil.rmtree("__pycache__")
        except Exception as ex:
            # print(f"392____{ex}")
            pass  
        try:
            if os.path.exists("./utilsss/__pycache__"):
                shutil.rmtree("./utilsss/__pycache__")
        except Exception as ex:
            print(f"445____{ex}")
            pass 
        try:
            if os.path.exists("./scrapers_funcs/__pycache__"):
                shutil.rmtree("./scrapers_funcs/__pycache__")
        except Exception as ex:
            print(f"451____{ex}")
            pass 
        try:
            if os.path.exists("./db_all/__pycache__"):
                shutil.rmtree("./db_all/__pycache__")
        except Exception as ex:
            print(f"457____{ex}")
            pass   
        try:
            if os.path.exists(cache_dir):
                shutil.rmtree(cache_dir)
        except Exception as ex:
            # print(f"396____{ex}")
            pass
    except Exception as ex:
        print(f"551____{ex}") 

def main():
    args_cycles = {       
        'n1': 0,
        'n2': 0,
        'interval': 1000,
        'from_item': 57000,
        'len_items': 326859,
        'counter': 0,
        'flag_end_cycles': False,
        'cpu_count': 64
    }  

    try:
        cycles_worker(**args_cycles)
    except Exception as ex:
        print(f"454____{ex}")

if __name__ == "__main__":
    try:
        atexit.register(cleanup_cache)
    except Exception as ex:
        print(f"461____{ex}")
    start_time = time.time() 
    main() 
    finish_time = time.time() - start_time
    print(f"Total time:  {math.ceil(finish_time)} сек")
    try:
        sys.exit()
    except Exception as ex:
        print(f"467______{ex}")



# u9FSEvF3:igzQ94p1@212.6.36.101:62362
# u9FSEvF3:igzQ94p1@77.90.155.134:63018
# u9FSEvF3:igzQ94p1@154.7.210.206:60790
# u9FSEvF3:igzQ94p1@87.247.143.202:63698
# u9FSEvF3:igzQ94p1@62.3.3.131:62764
# u9FSEvF3:igzQ94p1@193.58.178.71:63514
# u9FSEvF3:igzQ94p1@193.232.42.59:63076
# u9FSEvF3:igzQ94p1@193.232.41.147:62566
# u9FSEvF3:igzQ94p1@149.104.228.17:63370
# u9FSEvF3:igzQ94p1@149.104.229.30:64744



  

