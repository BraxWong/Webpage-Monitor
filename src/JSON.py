import json
import os
import backpacktf

def add_to_json(item_list, price_list, item_link_list, f, file_data, marketplace_seller_fee, marketplace_key_price):
    for index in range(len(item_list)):
        file_data["items"].append({"item name": item_list[index], 
                                    "price": price_list[index],
                                    "url": item_link_list[index]})
        index+=1
        buy_order_price = backpacktf.getItemPrice(item_list[index])
        if backpacktf.calculate_profit(price_list[index], marketplace_key_price, marketplace_seller_fee, buy_order_price) > 0:
            print("PROFIT LANDDD")
            #TODO: Implement a function that executes DiscordWebhook for notification
    f.seek(0)
    json.dump(file_data, f, indent = 2, ensure_ascii=False)

def check_database(item_list, price_list, item_link_list, marketplace_seller_fee, marketplace_key_price):
    with open("database.json", 'r+', encoding='utf-8') as file:
        index = 0
        fileWiped = False
        file_is_empty = os.stat("database.json").st_size == 0 
        if file_is_empty:
            file.write("{\n\t\"items\":[\n\t]\n}")

        file_data = json.load(file)
        if len(file_data["items"]) == 0:
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