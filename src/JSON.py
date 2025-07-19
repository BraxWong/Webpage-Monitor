import json
import os
import subprocess
from concurrent.futures import ThreadPoolExecutor
import backpacktf
from sys import platform
from Enum import Site_Classifications
import mouse_movement

temp_map = {}

def load_database_to_map(file_data):
    for item in file_data["items"]:
        temp_map[item["item name"]] = item["price"]

def check_profitability(item_name, price, url, marketplace_key_price, marketplace_seller_fee, selenium_config):
    print(f"Item Name: {item_name}")
    future1 = ThreadPoolExecutor().submit(backpacktf.getItemPrice, item_name, selenium_config)
    # future2 = ThreadPoolExecutor().submit(mouse_movement.jiggle_mouse)
    buy_order_price = future1.result()
    if buy_order_price != '':
        link_info = backpacktf.getUnusualIndex(item_name)
        if len(link_info) >= 2:
            bpft_url = backpacktf.getLink(link_info[0], link_info[1])
            print(price)
            print(marketplace_key_price)
            print(marketplace_seller_fee)
            print(buy_order_price)
            if backpacktf.calculate_profit(float(price), float(marketplace_key_price), float(marketplace_seller_fee), float(buy_order_price)) > 0.0:
                if platform == "linux":
                    subprocess.run(f'cd src && ./DiscordWebhook "{url}" "{item_name}" "{price}" "{bpft_url}" "{buy_order_price}" "{marketplace_key_price * marketplace_seller_fee}"', shell=True, capture_output=True, text=True)
                else:
                    subprocess.run(f'cd src && .\\DiscordWebhook.exe "{url}" "{item_name}" "{price}" "{bpft_url}" "{buy_order_price}" "{marketplace_key_price * marketplace_seller_fee}"', shell=True, capture_output=True, text=True)
    else:
        print("This item does not have a buy order. Ignore")

def add_to_json(item_list, price_list, item_link_list, f, file_data, marketplace_seller_fee, marketplace_key_price, selenium_config):
    for index in range(len(item_list)):
        file_data["items"].append({"item name": item_list[index], 
                                    "price": price_list[index],
                                    "url": item_link_list[index]})
        f.seek(0)
        json.dump(file_data, f, indent = 2, ensure_ascii=False)
        print(price_list[index])
        check_profitability(item_list[index], float(price_list[index].replace("£","")), item_link_list[index], marketplace_key_price, marketplace_seller_fee, selenium_config)

def edit_to_json(item_name, price, f, file_data, item_link, marketplace_key_price, marketplace_seller_fee, selenium_config):
    for item in file_data["items"]:
        if item["item name"] == item_name:
            item["price"] = price
            f.seek(0)
            json.dump(file_data, f, indent = 2, ensure_ascii=False)
            f.truncate()
            check_profitability(item_name, float(price.replace("£","")), item_link, marketplace_key_price, marketplace_seller_fee, selenium_config)
            return


def get_database_file_name(site_classification):
    file_name = ""
    if site_classification == Site_Classifications.SKINPORT:
        file_name = "src/skinport_database.json"
    else:
        file_name = "src/mannco_database.json"
    return file_name

def check_database(item_list, price_list, item_link_list, marketplace_seller_fee, marketplace_key_price, site_classification, selenium_config):

    file_name = get_database_file_name(site_classification)

    if not os.path.exists(file_name):
        with open(file_name,"w",encoding='utf-8') as file:
            file.write("{\n\t\"items\":[\n\t]\n}")
            file.close()

    with open(file_name, 'r+', encoding='utf-8') as file:
        file_data = json.load(file)
        load_database_to_map(file_data)
        if len(file_data["items"]) == 0:
            add_to_json(item_list, price_list, item_link_list, file, file_data, marketplace_seller_fee, marketplace_key_price)
        else:
            load_database_to_map(file_data)
            for i in range(len(item_list)): 
                if item_list[i] in temp_map and temp_map[item_list[i]] != price_list[i]:
                    edit_to_json(item_list[i], price_list[i], file, file_data, item_link_list[i], marketplace_key_price, marketplace_seller_fee, selenium_config)
                elif item_list[i] not in temp_map:
                    add_to_json([item_list[i]], [price_list[i]], [item_link_list[i]], file, file_data, marketplace_seller_fee, marketplace_key_price, selenium_config)
        file.truncate()
        file.close()