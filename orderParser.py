import re
from wafflesList import waffle_list

def parse_order(order):
    waffles = []

    for name in waffle_list:
        waffles.append(name['name'])