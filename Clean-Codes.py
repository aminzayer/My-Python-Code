# if-guard-clause 
# Calculate Total Price
def total_price(authenticated: bool, item_price: int, item_quantity: int) -> str | str:
    if not authenticated:
        return "User is not authenticated."
    
    if item_price <= 0:
        return "Price must be greater than 0."
    
    if item_quantity <=0:
        return "Quantity must be greater than 0."
    
    return item_price * item_quantity