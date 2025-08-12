import re
from wafflesList import waffle_list

def parse_order(order):
    waffles = []

    for name in waffle_list:
        waffles.append(name['name'])

    order = order.lower()
    waffle_pattern = r'\b(' + '|'.join(re.escape(name.lower()) for name in waffles) + r')\b'
    waffle_match = re.search(waffle_pattern, order, re.I)

    if waffle_match:
        return order
    else:
        return "No valid order found"