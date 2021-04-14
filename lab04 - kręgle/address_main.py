def format_addresses(addresses):
    x = 0
    for address in addresses:
        ad = address.replace("-", " ")
        addresses[x] = ad
        x = x + 1

    return addresses




#x = ['34-Czerwona', '23-Biala', '85 Pogodna']
#format_addresses(x)