import json
import os
import subprocess
import backpacktf
from sys import platform
from Enum import Site_Classifications

temp_map = {}

def add_to_json(item_list, price_list, item_link_list, f, file_data, marketplace_seller_fee, marketplace_key_price):
    for index in range(len(item_list)):
        file_data["items"].append({"item name": item_list[index], 
                                    "price": price_list[index],
                                    "url": item_link_list[index]})
        buy_order_price = backpacktf.getItemPrice(item_list[index])
        if buy_order_price != '':
            link_info = backpacktf.getUnusualIndex(item_list[index])
            bpft_url = backpacktf.getLink(link_info[0], link_info[1])
            f.seek(0)
            json.dump(file_data, f, indent = 2, ensure_ascii=False)
            if backpacktf.calculate_profit(float(price_list[index].replace("£","")), float(marketplace_key_price), float(marketplace_seller_fee), float(buy_order_price)) > 0.0:
                if platform == "linux":
                    subprocess.run(f'cd src && ./DiscordWebhook "{item_link_list[index]}" "{item_list[index]}" "{price_list[index]}" "{price_list[index]}" "{bpft_url}" "{buy_order_price}" "{marketplace_key_price * marketplace_seller_fee}"', shell=True, capture_output=True, text=True)
                else:
                    subprocess.run(f'cd src && .\\DiscordWebhook.exe "{item_link_list[index]}" "{item_list[index]}" "{price_list[index]}" "{price_list[index]}" "{bpft_url}" "{buy_order_price}" "{marketplace_key_price * marketplace_seller_fee}"', shell=True, capture_output=True, text=True)
        else:
            print("This item does not have a buy order")

def check_database(item_list, price_list, item_link_list, marketplace_seller_fee, marketplace_key_price, site_classification):

    file_name = get_database_file_name(site_classification)

    if not os.path.exists(file_name):
        with open(file_name,"w",encoding='utf-8') as file:
            file.write("{\n\t\"items\":[\n\t]\n}")
            file.close()

    with open(file_name, 'r+', encoding='utf-8') as file:
        index = 0
        fileWiped = False
        file_data = json.load(file)
        if len(file_data["items"]) == 0:
            print("Adding to file")
            add_to_json(item_list, price_list, item_link_list, file, file_data, marketplace_seller_fee, marketplace_key_price)
        else:
            for item in file_data["items"]:
                if item["item name"] != item_list[index] and index == 0:
                    file_data["items"].clear()
                    file.seek(0)
                    file.truncate()
                    json.dump(file_data, file, indent = 2, ensure_ascii=False)
                    fileWiped = True
                    break
                index +=1
            if fileWiped:
                add_to_json(item_list, price_list, item_link_list, file, file_data, marketplace_seller_fee, marketplace_key_price)
        file.truncate()
        file.close()

def get_database_file_name(site_classification):
    file_name = ""
    if site_classification == Site_Classifications.SKINPORT:
        file_name = "skinport_database.json"
    else:
        file_name = "mannco_database.json"
    return file_name

def load_database_to_map():
    pass