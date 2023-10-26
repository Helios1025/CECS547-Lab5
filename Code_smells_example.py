#Code Smells Example for long method
def get_discount_rate(price):
    if price > 100
        return 0.9
    else    
        return 0.95

def calculate_total_price(items):
    total = 0
    for item in items:
        if item.quantity > 0:
            discount_rate = get_discount_rate(item.price)
            total += item.price * discount_rate
    return total
