from collections import OrderedDict
ordered_dictionary = OrderedDict()
N = int(input())
for i in range(N):
    *item_name, net_price = input().split()
    item_name = " ".join(item_name)
    net_price = int(net_price)
    if item_name in ordered_dictionary:
        ordered_dictionary[item_name] += net_price
    else:
        ordered_dictionary[item_name] = net_price
for key, val in ordered_dictionary.items():
    print(key, val)
