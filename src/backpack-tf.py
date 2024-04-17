from pricestf_py import PricesTF

def getItemPrice(itemName, itemQuality, craftable, australium, killstreak):
    ptf = PricesTF()
    response = ptf.price_by_name(itemName, itemQuality, craftable, australium, killstreak)
    print(response)

