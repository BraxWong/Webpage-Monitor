import json
import os
import backpacktf

def add_to_json(item_list, price_list, item_link_list, f, file_data):
    for index in range(len(itemList))
        file_data["items"].append({"item name": item_list[index], 
                                    "price": price_list[index],
                                    "url": item_link_list[index]})
        index+=1
        if backpacktf.getItemPrice(item_list[index], price_list[index]):
            print("TESTING")
            #itemInfo = backpacktf.getUnusualIndex(itemList[index])
            #url = backpacktf.getLink(itemInfo[0], itemInfo[1])
        #TODO: Implement a function that checks for profit potential
    f.seek(0)
    json.dump(file_data, f, indent = 2, ensure_ascii=False)

def check_database(itemList, priceList, item_link_list):
    with open("database.json", 'r+', encoding='utf-8') as file:
        index = 0
        fileWiped = False
        itemString = ""
        file_is_empty = os.stat("database.json").st_size == 0 
        if file_is_empty:
            f.write("{\n\t\"items\":[\n\t]\n}")

        file_data = json.load(file)
        if len(file_data["items"]) == 0:
            add_to_json(itemList, priceList, item_link_list, file, file_data)
        else:
            for item in file_data["items"]:
                if item["item name"] != itemList[index] and index == 0:
                    file_data["items"].clear()
                    file.seek(0)
                    file.truncate()
                    json.dump(file_data, file, indent = 2, ensure_ascii=False)
                    fileWiped = True
                    break
                index +=1

            if fileWiped:
                add_to_json(itemList, priceList, item_link_list, file, file_data)
        file.truncate()
        file.close()

