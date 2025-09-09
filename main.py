# from fetchComments import *
from fetchHotels import *
from fetchDetail import fetchInfo1, fetchInfo2
import json
from tqdm import tqdm  # Import tqdm for progress bar
import os  # Import os module for directory operations
from concurrent.futures import ThreadPoolExecutor  # Import ThreadPoolExecutor for multithreading

# config
cityId = 30  # 1: Beijing, 2: Shanghai, 3: Guangzhou, 4: Shenzhen
numHotelPages = 400  # the number of hotels fetched is about numHotelPages * 10, unless there are not enough hotels

# # Ensure 'outputs' directory exists
# if not os.path.exists('outputs'):
#     os.makedirs('outputs')

# # fetch hotels
# print(f"Fetching hotels for city {cityId}...")
# fetchHotels(cityId, numHotelPages, savePath="hotels.json")
# print("Hotels fetched and saved to hotels.json")

with open('D:\\Desktop\\xiecheng\\ctrip-review-crawler-master\\hotels_400_page.json', 'r', encoding='utf-8') as f:
    hotels_dict = json.load(f)
# hotels_dict = hotels_dict[:10]
# hotels_dict = dict(list(hotels_dict.items())[:10])  # 只取前10个酒店用于测试
print(f"Loaded {len(hotels_dict)} hotels from JSON file.")
base = 'D:\\Desktop\\xiecheng\\data'
for hotel_id, hotel_data in hotels_dict.items():
    # 我们首先给每个酒店都建立一个文件夹
    hotel_info_dir = os.path.join(base, str(hotel_id))
    if not os.path.exists(hotel_info_dir):
        os.makedirs(hotel_info_dir)
print("Fetching details for each hotel...")

# Function to process a single hotel
def process_hotel(hotel_id, hotel_data):
    save_path = os.path.join(base, str(hotel_id))
    # 存在就跳过
    if os.path.exists(os.path.join(save_path, f"page_{hotel_id}.html")):
        print(f"Hotel {hotel_id} already processed, skipping.")
        return
    fetchInfo1(hotel_id, save_path=save_path)
    import time
    time.sleep(1)  # 避免请求过于频繁
    fetchInfo2(hotel_id, save_path=save_path)

with ThreadPoolExecutor(max_workers=20) as executor:
    futures = [
        executor.submit(process_hotel, hotel_id, hotel_data)
        for hotel_id, hotel_data in hotels_dict.items()
    ]
    for future in tqdm(futures, desc="Processing hotels", unit="hotel"):
        future.result()  # Wait for each thread to complete

# # Function to process a single hotel
# def process_hotel(hotel_id, hotel_data, numCommentPages):
#     comments = fetchHotelComments(hotel_id, numCommentPages)
#     hotel_data['comments'] = comments
#     with open(f'outputs/hotel_{hotel_id}.json', 'w', encoding='utf-8') as hotel_file:
#         json.dump(hotel_data, hotel_file, ensure_ascii=False, indent=4)

# # read hotels from json and process each hotel
# print("Fetching comments for each hotel...")
# with open('hotels.json', 'r', encoding='utf-8') as f:
#     hotels_dict = json.load(f)  # Load the entire JSON object

#     # Use ThreadPoolExecutor for multithreading
#     with ThreadPoolExecutor(max_workers=2) as executor:
#         futures = [
#             executor.submit(process_hotel, hotel_id, hotel_data, numCommentPages)
#             for hotel_id, hotel_data in hotels_dict.items()
#         ]
#         for future in tqdm(futures, desc="Processing hotels", unit="hotel"):
#             future.result()  # Wait for each thread to complete